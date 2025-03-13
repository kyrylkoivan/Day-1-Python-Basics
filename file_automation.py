import os
import shutil

source_dir = "C:/Users/aikyr/Documents/source_folder"
destination_dir = "C:/Users/aikyr/Documents/destination_folder"
# Ensure source directory exists
if not os.path.exists(source_dir):
    os.makedirs(source_dir)  # Create the directory
    print(f"Created missing folder: {source_dir}")

files = os.listdir(source_dir)
print("Files in source directory:", files)

old_name = os.path.join(source_dir, "old_file.txt")
new_name = os.path.join(source_dir, "renamed_file.txt")

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"Renamed '{old_name}' to '{new_name}'")
else:
    print("File not found!")

file_to_move = os.path.join(source_dir, "renamed_file.txt")
destination_path = os.path.join(destination_dir, "renamed_file.txt")

if os.path.exists(file_to_move):
    shutil.move(file_to_move, destination_path)
    print(f"Moved '{file_to_move}' to '{destination_path}'")
else:
    print("File not found!")

def organize_files(src, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)

    for filename in os.listdir(src):
        src_file = os.path.join(src, filename)
        dest_file = os.path.join(dest, f"renamed_{filename}")

        if os.path.isfile(src_file):
            os.rename(src_file, dest_file)  # Rename
            shutil.move(dest_file, dest)  # Move
            print(f"Renamed and moved: {src_file} -> {dest_file}")

# Example usage
organize_files(source_dir, destination_dir)
