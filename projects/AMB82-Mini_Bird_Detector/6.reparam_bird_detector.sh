#!/bin/bash

# Navigate to this script's directory
cd "$(dirname "$0")"

# Set YOLOv7 root relative to current directory
YOLOV7_ROOT="../../"

# Set PYTHONPATH so that Python can find yolov7 modules
export PYTHONPATH="$YOLOV7_ROOT:$PYTHONPATH"

# Default input/output paths
DEFAULT_WEIGHTS_IN="$YOLOV7_ROOT/runs/train/exp6/weights/best.pt"
DEFAULT_WEIGHTS_OUT="$YOLOV7_ROOT/runs/train/exp6/weights/best_deploy.pt"
CUSTOM_YAML="yolov7-tiny-deploy.yaml"
REPARAM_SCRIPT="reparam_yolov7-tiny.py"

# Allow overriding input/output from command line
WEIGHTS_IN="${1:-$DEFAULT_WEIGHTS_IN}"
WEIGHTS_OUT="${2:-$DEFAULT_WEIGHTS_OUT}"

# Display
echo "Reparameterizing YOLOv7-Tiny model..."
echo "Input weights : $WEIGHTS_IN"
echo "Deploy config : $CUSTOM_YAML"
echo "Output weights: $WEIGHTS_OUT"
echo

# Run reparam
python3 "$REPARAM_SCRIPT" \
  --weights "$WEIGHTS_IN" \
  --custom_yaml "$CUSTOM_YAML" \
  --output "$WEIGHTS_OUT"
