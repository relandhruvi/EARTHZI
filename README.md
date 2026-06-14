# EARTHZI
<div align="center">

# 🛰️ EARTHZI
**Cross-Modal Earth Observation Retrieval**

[![Model](https://img.shields.io/badge/Model-RemoteCLIP_ViT--B--32-00D9FF?style=for-the-badge&logo=pytorch&logoColor=white)](#)
[![Backend](https://img.shields.io/badge/Backend-FastAPI-009485?style=for-the-badge&logo=fastapi&logoColor=white)](#)
[![Visualization](https://img.shields.io/badge/3D-Three.js-000000?style=for-the-badge&logo=three.js&logoColor=white)](#)
[![Deployed](https://img.shields.io/badge/Deployed-HuggingFace_Spaces-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](#)
<br>
[![Try It](https://img.shields.io/badge/🚀_Try_It-Live_Demo-0891B2?style=for-the-badge)](https://relandhruvi.github.io/EARTHZI)

*Fine-tuned RemoteCLIP • Bidirectional SAR↔Optical Retrieval • Cosine Similarity Search • 4,000 Image Gallery*

</div>

---

TRY IT OUT — https://relandhruvi.github.io/EARTHZI

Backend API — https://relandhruvi-earthzi.hf.space

---

## 📌 System Overview

> **EARTHZI bridges the radar-optical divide.** Upload a Sentinel-1 SAR patch or a Sentinel-2 optical image, and EARTHZI retrieves the five closest cross-modal matches — in either direction — using a fine-tuned RemoteCLIP model and cosine similarity search.

Synthetic Aperture Radar penetrates cloud and night, but reads like noise to the eye. Optical imagery is intuitive, but useless after dark or under cloud. EARTHZI bridges the two — matching a radar patch to its optical counterpart, and back again, by embedding both into a shared space using contrastive learning on paired Sentinel-1 / Sentinel-2 patches.

---

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| **Bidirectional Retrieval** | Upload
