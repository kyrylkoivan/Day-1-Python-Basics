import os
import shutil

# Define test folder name
test_folder = "dummy_test_folder"

# Create the folder if it doesn't exist
if not os.path.exists(test_folder):
    os.makedirs(test_folder)

# Create dummy files
for i in range(1, 6):
    with open(os.path.join(test_folder, f"test_file_{i}.txt"), "w") as f:
        f.write(f"Sample content for file {i}")

print("Dummy test folder and files created successfully.")

# List files in the directory
print("Files before renaming:", os.listdir(test_folder))

# Rename first file
old_name = os.path.join(test_folder, "test_file_1.txt")
new_name = os.path.join(test_folder, "renamed_file_1.txt")

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"Renamed: {old_name} -> {new_name}")

# Move renamed file to a new subdirectory
destination_folder = os.path.join(test_folder, "sorted_files")
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

shutil.move(new_name, os.path.join(destination_folder, "renamed_file_1.txt"))
print(f"Moved {new_name} to {destination_folder}")

# List files after operations
print("Files after renaming & moving:", os.listdir(test_folder))
