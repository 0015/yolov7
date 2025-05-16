from collections import Counter
import os

label_dir = "bird-dataset/labels/train"
class_ids = []

for file in os.listdir(label_dir):
    if file.endswith(".txt"):
        with open(os.path.join(label_dir, file)) as f:
            for line in f:
                parts = line.strip().split()
                if parts:
                    class_ids.append(int(parts[0]))

print("Most common class IDs:", Counter(class_ids).most_common(10))