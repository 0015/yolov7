import os

def filter_and_remap_labels(label_dir, target_class="24"):
    for file in os.listdir(label_dir):
        if file.endswith(".txt"):
            path = os.path.join(label_dir, file)
            with open(path, "r") as f:
                lines = f.readlines()

            filtered = []
            for line in lines:
                parts = line.strip().split()
                if parts and parts[0] == target_class:
                    parts[0] = "0"  # Remap bird class to 0
                    filtered.append(" ".join(parts) + "\n")

            with open(path, "w") as f:
                f.writelines(filtered)

# Apply to both train and val sets
filter_and_remap_labels("bird-dataset/labels/train")
filter_and_remap_labels("bird-dataset/labels/val")