import kagglehub
import shutil
import os

# Download dataset (still goes to default cache location)
cached_path = kagglehub.dataset_download("samuelayman/bird-dataset")

# Set your desired destination folder (current folder)
destination = os.path.join(os.getcwd(), "bird-dataset")

# Move the downloaded folder to the current directory
if not os.path.exists(destination):
    shutil.copytree(cached_path, destination)

print("Dataset moved to:", destination)