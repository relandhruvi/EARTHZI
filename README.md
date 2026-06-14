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
| **Fine-tuned RemoteCLIP** | ViT-B-32 backbone contrastively trained on paired Sentinel-1/Sentinel-2 patches — pulling true geographic pairs together in shared embedding
