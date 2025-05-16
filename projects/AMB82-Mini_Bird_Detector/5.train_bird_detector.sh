#!/bin/bash

# Move to yolov7 root
cd "$(dirname "$0")/../.."

# Run training from root
python3 train.py \
  --img 416 \
  --batch 8 \
  --epochs 50 \
  --data projects/AMB82-Mini_Bird_Detector/bird.yaml \
  --cfg cfg/training/yolov7-tiny.yaml \
  --weights projects/AMB82-Mini_Bird_Detector/yolov7-tiny.pt \
  --device cpu
