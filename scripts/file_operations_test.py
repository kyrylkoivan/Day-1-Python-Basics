import os
import shutil

# Define directory paths
SOURCE_DIR = "dummy_test_folder"
DEST_DIR = "organized_files"

# File type categories
FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Archives": [".zip", ".rar", ".tar"],
    "Scripts": [".py", ".sh", ".bat"]
}

# Ensure destination folders exist
for category in FILE_CATEGORIES.keys():
    os.makedirs(os.path.join(DEST_DIR, category), exist_ok=True)


def safe_move(file_path, dest_folder):
    """Moves a file safely, handling exceptions."""
    try:
        shutil.move(file_path, dest_folder)
        print(f"Successfully moved {file_path} → {dest_folder}")
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except PermissionError:
        print(f"Permission denied: {file_path}")
    except Exception as e:
        print(f"Unexpected error moving {file_path}: {e}")

# Use safe_move in move_files_by_extension
def move_files_by_extension(source_dir, dest_dir, categories):
    """Moves files into categorized folders based on their extensions."""
    for file in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file)

        if not os.path.isfile(file_path):
            continue

        file_ext = os.path.splitext(file)[1].lower()
        for category, extensions in categories.items():
            if file_ext in extensions:
                target_folder = os.path.join(dest_dir, category)
                safe_move(file_path, target_folder)
                break
