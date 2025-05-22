# 🐦 AMB82-MINI Bird Detector – YOLOv7-Tiny on Edge AI Camera

This project demonstrates how to train and deploy a **YOLOv7-Tiny** model to detect birds in real time using the **Realtek AMB82-MINI** AI camera module.  
Everything runs **on-device** — no internet, no cloud — just a camera, an SD card, and an `.nb` model file.

> This branch (`AMB82-Mini_Bird_Detector`) is based on [`WongKinYiu/yolov7`](https://github.com/WongKinYiu/yolov7) and includes all scripts and Arduino files needed to complete the full workflow.

---

## 📦 Features

- Dataset preparation, filtering, and remapping for single-class detection
- YOLOv7-Tiny training pipeline (PyTorch)
- Reparameterization and `.nb` model conversion for AMB82-MINI
- Arduino integration with live object detection
- Fully offline edge AI deployment

---

## 🧠 Workflow Overview

```
.pt (PyTorch YOLOv7) 
   → Reparameterized 
      → .nb (Realtek format) 
         → Run on AMB82-MINI
```

---

## 🚀 Quick Steps

| Step | Description |
|------|-------------|
| 0 | Set up Python VENV & install dependencies (Python 3.8)|
| 1 | Clone this repo and switch to `AMB82-Mini_Bird_Detector` branch |
| 2 | Download dataset from Kaggle |
| 3 | Organize dataset into train/val |
| 4 | Filter for bird class only (remap to class 0) |
| 5 | Confirm most frequent class is now `0` |
| 6 | Train YOLOv7-Tiny model |
| 7 | Test detection with `detect.py` |
| 8 | Reparameterize model using Realtek script |
| 9 | Convert to `.nb` via AI Model Converter |
| 10 | Save model to SD card for AMB82-MINI |
| 11 | Upload Arduino sketch with updated class list |

---

## 📁 Contents

- `1.download_dataset.py` – Downloads dataset from Kaggle
- `2.organize_dataset.py` – Splits data into train/val structure
- `3.filter.py` – Keeps only bird (class 24 → 0)
- `4.most_find.py` – Verifies remapped class counts
- `5.train_bird_detector.sh` – Training scripts
- `6.reparam_bird_detector.sh` – Reparameterization for Realtek (https://www.kaggle.com/code/kevinl00/yolov7-reparameterization-only)
- `yolov7-tiny-deploy.yaml` – Deploy model config
- `bird.yaml` – Dataset config for YOLO training
- Arduino Sketch – Located in `/BirdDetection_SaveAsMP4/` (example: BirdDetection_SaveAsMP4.ino)

---

## ⚙️ Realtek AI Model Converter

Compress `best_reparam.pt` and upload it here:  
[https://www.amebaiot.com/en/amebapro2-ai-convert-model/](https://www.amebaiot.com/en/amebapro2-ai-convert-model/)

**Settings:**
- Model: YOLOv7-Tiny
- Input: 416 × 416
- Quantization: UINT8
- Classes: 1
- Class name: bird

---

## 📷 AMB82-MINI Deployment

Copy the converted `.nb` model file to your SD card.  
Update your Arduino sketch like:

```cpp
ObjectDetectionItem itemList[1] = {
    {0, "bird", 1}
};
```

Then upload to AMB82-MINI and you're ready to detect!

---

## 🎥 Demo Video

Watch the full build and training process on YouTube:  
**[Smart Bird Feeder with Camera – YOLOv7 on AMB82-MINI](https://youtu.be/QwcBwGNJ3PQ)**

---

## 📄 License

This project is under the MIT License.  
Based on [WongKinYiu/yolov7](https://github.com/WongKinYiu/yolov7).

---

## 🙌 Credits

- YOLOv7 by @WongKinYiu  
- Realtek AMB82-MINI SDK  
- Dataset from Kaggle Bird Dataset  
- Scripts and Arduino integration by [ThatProject](https://github.com/0015)
