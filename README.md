<div align="center">

# 🛰️ EARTHZI
**Cross-Modal Earth Observation Retrieval**

[![Model](https://img.shields.io/badge/Model-RemoteCLIP_ViT--B--32-00D9FF?style=for-the-badge&logo=pytorch&logoColor=white)](#)
[![Backend](https://img.shields.io/badge/Backend-FastAPI-009485?style=for-the-badge&logo=fastapi&logoColor=white)](#)
[![3D Visualization](https://img.shields.io/badge/3D-Three.js-000000?style=for-the-badge&logo=three.js&logoColor=white)](#)
[![Animations](https://img.shields.io/badge/Animations-GSAP-88CE02?style=for-the-badge&logo=greensock&logoColor=black)](#)
[![Deployed](https://img.shields.io/badge/Deployed-HuggingFace_Spaces-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](#)
<br>
[![Try It](https://img.shields.io/badge/🚀_Try_It-Live_Demo-0891B2?style=for-the-badge)](https://relandhruvi.github.io/EARTHZI)

*Fine-tuned RemoteCLIP • Bidirectional SAR↔Optical Retrieval • Cosine Similarity Search • 4,000 Image Gallery • Cinematic Space UI*

</div>

---

TRY IT OUT — https://relandhruvi.github.io/EARTHZI

Backend API — https://relandhruvi-earthzi.hf.space

---

## 📌 System Overview

> **EARTHZI bridges the radar-optical divide.** Upload a Sentinel-1 SAR patch or a Sentinel-2 optical image, and EARTHZI retrieves the five closest cross-modal matches — in either direction — using a fine-tuned RemoteCLIP model and cosine similarity search over a 4,000-image gallery.

Synthetic Aperture Radar penetrates cloud and night, but reads like noise to the eye. Optical imagery is intuitive, but useless after dark or under cloud. Existing remote sensing tools treat these two modalities as entirely separate data streams — requiring analysts to manually correlate SAR and optical scenes of the same location. EARTHZI fixes this by combining **contrastive deep learning, cross-modal embedding alignment, and a cinematic live demo interface** to deliver instant, bidirectional SAR↔Optical retrieval from a single image upload.

---

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| **Bidirectional Retrieval** | Upload SAR → get optical matches. Upload optical → get SAR matches. Both directions fully supported in a single model. |
| **Fine-tuned RemoteCLIP** | ViT-B-32 backbone contrastively trained on paired Sentinel-1/Sentinel-2 patches — pulling true geographic pairs together in shared embedding space. |
| **4,000 Image Gallery** | Pre-computed gallery embeddings spanning agricultural, barren land, grassland, and urban land cover types across multiple seasons. |
| **Cosine Similarity Search** | Query embedding compared against all gallery embeddings via dot product in milliseconds — top-5 matches returned with similarity scores. |
| **Live Demo Interface** | Upload any SAR or optical patch directly in the browser, choose retrieval direction, and see real ranked results with image thumbnails instantly. |
| **Cinematic Space UI** | Three.js animated particle field with 1,400 points, GSAP scroll-triggered animations, pinned pipeline section, and a dark space aesthetic built for impact. |

---

## 🖥️ Platform Walkthrough

### Hero — One satellite sees radar. One sees light.
The homepage opens with a full-viewport Three.js particle field — 1,400 points drifting along an amber-to-cyan gradient, responding to scroll and mouse movement. The EARTHZI wordmark sits front and center with a gradient glow, alongside two CTAs: Run a Retrieval and See How It Works. This is cross-modal Earth observation, reimagined as a product.

<div align="center">
  <img src="https://raw.githubusercontent.com/relandhruvi/EARTHZI/main/screenshots/WhatsApp%20Image%202026-06-14%20at%2021.29.19.jpeg" alt="Two Sensors One Earth" width="800"/>
</div>

---

### The Problem — Two Sensors, One Earth
SAR penetrates cloud and night but looks like noise. Optical is intuitive but fails in darkness and bad weather. EARTHZI learns to recognise the same ground beneath both — pulling true geographic pairs together in embedding space and pushing everything else apart. The mission section surfaces the real evaluation numbers: 35.7% Rank@1 and 68.7% Recall@5 for Optical→SAR, and 32.5% Rank@1 and 63.9% Recall@5 for SAR→Optical, evaluated across 4,000 queries on a held-out test split.

<div align="center">
  <img src="https://raw.githubusercontent.com/relandhruvi/EARTHZI/main/screenshots/WhatsApp%20Image%202026-06-14%20at%2021.29.20.jpeg" alt="Keep It Free Section" width="800"/>
</div>

---

### Pipeline — From Query to Match
A horizontally-pinned scroll section walks through the three-stage retrieval pipeline: Upload a patch → RemoteCLIP encodes it into a 512-dimensional shared embedding → Cosine similarity search returns the five closest cross-modal matches from the gallery. Each stage is labeled with its role (INPUT / ENCODE / COMPARE) and a short technical description.

<div align="center">
  <img src="https://raw.githubusercontent.com/relandhruvi/EARTHZI/main/screenshots/WhatsApp%20Image%202026-06-14%20at%2021.29.20%20(1).jpeg" alt="Pipeline From Query to Match" width="800"/>
</div>

---

### Live Demo — Run a Retrieval
The interactive core of EARTHZI. A drag-and-drop upload zone accepts any SAR or optical image patch. A direction toggle switches between SAR→OPTICAL and OPTICAL→SAR retrieval. Clicking Run Retrieval sends the image to the FastAPI backend on Hugging Face Spaces, which encodes it and returns the top-5 gallery matches. Results appear as animated cards — each showing the matched image thumbnail, rank, and cosine similarity score. The upload zone resets automatically after each query so it's always ready for the next image.

<div align="center">
  <img src="https://raw.githubusercontent.com/relandhruvi/EARTHZI/main/screenshots/WhatsApp%20Image%202026-06-14%20at%2021.29.20%20(2).jpeg" alt="Live Demo Upload Zone" width="800"/>
</div>

---

### Results — Top-5 Cross-Modal Matches
The query image appears on the left. Five ranked result cards appear below — each showing the retrieved image thumbnail from the opposite modality, its rank, and its similarity score with an animated fill bar. Hovering any result thumbnail zooms it in-place for closer inspection. The system retrieves the correct geographic match at Rank 1 roughly one-third of the time, and within the top five nearly seven times out of ten.

<div align="center">
  <img src="https://raw.githubusercontent.com/relandhruvi/EARTHZI/main/screenshots/Screenshot%202026-06-14%20215547.png" alt="EARTHZI Hero Section" width="800"/>
</div>

---

### Keep It Free, Keep It Growing
A dedicated section above the footer makes the mission explicit: EARTHZI is free, open, and built for the research community. Two CTAs — Keep It Free and Get Started — sit beneath a short statement about democratising satellite imagery analysis for science and society.

<div align="center">
  <img src="https://raw.githubusercontent.com/relandhruvi/EARTHZI/main/screenshots/WhatsApp%20Image%202026-06-14%20at%2021.29.20%20(3).jpeg" alt="Top 5 Retrieval Results" width="800"/>
</div>

---

## 📊 Evaluation Results

Evaluated across **4,000 queries** in both directions on a held-out test split from the SEN12MS / BigEarthNet dataset:

| Metric | SAR → Optical | Optical → SAR |
| :--- | :---: | :---: |
| **Rank@1** | 32.5% | 35.7% |
| **Recall@5** | 63.9% | 68.7% |
| **F1@1** | 32.5% | 35.7% |
| **Mean Rank** | 8.79 | 6.91 |
| **Median Rank** | 3 | 3 |
| **Best Rank** | 1 | 1 |
| **Worst Rank** | 174 | 167 |

About 32–36% of queries retrieve the exact correct image at Rank 1. About 64–69% retrieve the correct image within the Top 5. The model works bidirectionally with consistent performance in both directions.

---

## 🛠️ Architecture & Tech Stack

EARTHZI combines contrastive deep learning with a fast inference backend and an immersive animated frontend.

* **Model:** Fine-tuned RemoteCLIP (ViT-B-32) — contrastive learning on paired Sentinel-1/Sentinel-2 patches to align SAR and optical embeddings into a shared 512-dimensional space
* **Backend:** FastAPI (Python) — REST API serving `/search` (retrieval) and `/gallery` (image serving) endpoints with CORS middleware
* **Similarity Search:** PyTorch cosine similarity over pre-computed gallery embeddings (4,000 × 512-dim float32 tensors) — sub-second inference on CPU
* **3D Visualization:** Three.js — animated particle field with 1,400 points colored along amber→cyan gradient by x-position, drifting with scroll and mouse
* **Scroll Animations:** GSAP + ScrollTrigger — pinned horizontal pipeline section, staggered card reveals, scroll-linked particle rotation
* **Frontend:** Single-file HTML with vanilla JS — no build step, no framework, deployable anywhere
* **Deployment:** Hugging Face Spaces (FastAPI backend, CPU Basic, 16GB RAM) + GitHub Pages (static frontend)
* **Model Weights Delivery:** gdown — weights and gallery embeddings downloaded from Google Drive on first startup, cached for subsequent restarts

---

## 🔬 How Retrieval Works

EARTHZI uses contrastive learning to align SAR and optical images in a shared embedding space:

**Training:** The RemoteCLIP model was fine-tuned on paired Sentinel-1/Sentinel-2 patches using contrastive loss. Positive pairs — matching SAR and optical images of the same geographic location — are pulled together. Negative pairs — non-matching images in the same batch — are pushed apart. After fine-tuning, a SAR image and its paired optical image produce embeddings that are close in cosine similarity, while unrelated patches remain distant.

**Inference:**
- User uploads a query image (SAR or optical)
- FastAPI passes it through the fine-tuned RemoteCLIP encoder
- The query embedding is L2-normalized to unit length
- Dot product computed against all gallery embeddings (equivalent to cosine similarity for unit vectors)
- Top-5 highest-scoring gallery images returned with filenames and scores
- Frontend fetches and displays the matched thumbnails via `/gallery/{filename}`

**Gallery:** The gallery contains 4,000 pre-computed Sentinel-2 optical embeddings. For SAR→Optical retrieval, the query (SAR) is matched against this optical gallery. The gallery was built by running all Sentinel-2 patches through the same fine-tuned encoder and saving the resulting embedding matrix.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.10+
* `finetuned_remoteclip.pth` — fine-tuned model weights (~605MB)
* `gallery_embeddings.pt` + `gallery_names.pt` — pre-computed gallery
* Sentinel-1 or Sentinel-2 image patches for querying

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/relandhruvi/EARTHZI.git
   cd EARTHZI
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS/Linux
   pip install -r requirements.txt
   ```

3. **Place model files in the backend folder:**
   ```
   backend/
   ├── finetuned_remoteclip.pth
   ├── gallery_embeddings.pt
   └── gallery_names.pt
   ```

4. **Run the backend:**
   ```bash
   cd backend
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Open the frontend:**
   ```
   http://localhost:8000
   ```
   Or open `index.html` directly in your browser with `BACKEND_URL` pointing to `http://localhost:8000`.

---

## 🎯 How It Works

**Step 1: Upload** → Drop a Sentinel-1 SAR or Sentinel-2 optical patch into the upload zone  
**Step 2: Choose Direction** → Toggle between SAR→OPTICAL or OPTICAL→SAR retrieval  
**Step 3: Run Retrieval** → EARTHZI encodes your image and searches the gallery in milliseconds  
**Step 4: Explore Results** → Five ranked cross-modal matches appear with thumbnails and similarity scores  

---

## 📁 Repository Structure

```
EARTHZI/
├── backend/
│   ├── app.py              # FastAPI server — /search and /gallery endpoints
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile          # HuggingFace Spaces Docker deployment
├── screenshots/            # Platform walkthrough screenshots
├── index.html              # Frontend — Three.js + GSAP single-page app
├── favicon.ico             # EARTHZI logo
└── README.md
```

---

## 👥 Built By

Designed and engineered for cross-modal remote sensing retrieval:

* **Model Training** — Contrastive fine-tuning of RemoteCLIP on paired Sentinel-1/Sentinel-2 patches from the SEN12MS dataset
* **Retrieval Pipeline** — Cosine similarity search over pre-computed gallery embeddings with sub-second CPU inference
* **Backend Architecture** — FastAPI inference server with image serving, CORS middleware, and Google Drive weight delivery
* **Frontend & Visualization** — Three.js particle field, GSAP scroll animations, cinematic dark space UI with live retrieval demo

*Built to bridge the gap between radar and light — one patch at a time.*

---

## 📄 License

MIT License — See LICENSE file for details.

---

**One satellite sees radar. One sees light. EARTHZI sees both.**
