import os
import random
import shutil

# Original paths
source_images = os.path.join("bird-dataset", "bird")
source_labels = os.path.join(source_images, "labels")

# Target paths
base_dir = "bird-dataset"
images_train = os.path.join(base_dir, "images", "train")
images_val = os.path.join(base_dir, "images", "val")
labels_train = os.path.join(base_dir, "labels", "train")
labels_val = os.path.join(base_dir, "labels", "val")

# Create target folders
for folder in [images_train, images_val, labels_train, labels_val]:
    os.makedirs(folder, exist_ok=True)

# Get image files
image_files = [f for f in os.listdir(source_images) if f.lower().endswith((".jpg", ".png"))]
random.shuffle(image_files)

# Split files
split_ratio = 0.8
split_index = int(len(image_files) * split_ratio)
train_files = image_files[:split_index]
val_files = image_files[split_index:]

# Move files
def move_files(files, img_dst, lbl_dst):
    for f in files:
        base = os.path.splitext(f)[0]
        label_file = base + ".txt"

        # Move image
        shutil.move(os.path.join(source_images, f), os.path.join(img_dst, f))

        # Move label (if it exists)
        src_label_path = os.path.join(source_labels, label_file)
        if os.path.exists(src_label_path):
            shutil.move(src_label_path, os.path.join(lbl_dst, label_file))

move_files(train_files, images_train, labels_train)
move_files(val_files, images_val, labels_val)

# Cleanup: remove the empty bird folder
shutil.rmtree(source_images, ignore_errors=True)

print(f"Done: {len(train_files)} train, {len(val_files)} val")