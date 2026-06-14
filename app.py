from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import torch
import torch.nn.functional as F
from PIL import Image
import io
import open_clip
import glob
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_ROOT = r"D:\dhruvi\archive\v_2"  # ← fixed path

@app.get("/gallery/{filename}")
def serve_gallery_image(filename: str):
    if not filename.endswith(".png"):
        filename = filename + ".png"
    matches = glob.glob(os.path.join(IMAGE_ROOT, "**", filename), recursive=True)
    if not matches:
        print(f"[GALLERY] NOT FOUND: {filename}")
        print(f"[GALLERY] Searched in: {IMAGE_ROOT}")
        return {"error": "not found"}
    print(f"[GALLERY] Serving: {matches[0]}")
    return FileResponse(matches[0], media_type="image/png")

# -----------------------
# DEVICE
# -----------------------
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# -----------------------
# LOAD MODEL
# -----------------------
model, _, preprocess = open_clip.create_model_and_transforms(
    "ViT-B-32",
    pretrained=None
)

checkpoint = torch.load(
    os.path.join(BASE_DIR, "finetuned_remoteclip.pth"),
    map_location=device
)

if isinstance(checkpoint, dict) and "model_state_dict" in checkpoint:
    model.load_state_dict(checkpoint["model_state_dict"])
elif isinstance(checkpoint, dict) and "state_dict" in checkpoint:
    model.load_state_dict(checkpoint["state_dict"])
else:
    model.load_state_dict(checkpoint)

model = model.to(device)
model.eval()
print("Model loaded successfully")

# -----------------------
# LOAD GALLERY
# -----------------------
gallery_embeddings = torch.load(
    os.path.join(BASE_DIR, "gallery_embeddings.pt"),
    map_location=device
).to(device)

gallery_names = torch.load(
    os.path.join(BASE_DIR, "gallery_names.pt"),
    map_location="cpu"
)
print(f"Gallery loaded: {len(gallery_names)} images")

# -----------------------
# SEARCH ENDPOINT
# -----------------------
@app.post("/search")
async def search(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = preprocess(image).unsqueeze(0).to(device)

    with torch.no_grad():
        query_emb = model.encode_image(img)
        query_emb = F.normalize(query_emb, dim=-1)

    scores = torch.matmul(gallery_embeddings, query_emb.squeeze(0))
    topk = torch.topk(scores, 5)

    results = []
    for rank, (score, idx) in enumerate(zip(topk.values, topk.indices), start=1):
        results.append({
            "rank": rank,
            "image": gallery_names[idx],
            "score": round(float(score), 4)
        })

    return {"total_results": len(results), "results": results}

# Serve frontend — MUST be last
app.mount("/", StaticFiles(directory=os.path.join(BASE_DIR, "..", "frontend"), html=True), name="frontend")