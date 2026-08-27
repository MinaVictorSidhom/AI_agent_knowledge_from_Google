import os
import shutil
# Get the folder name from the user
folder_name = input("Enter the folder name: ")
# Check if the folder exists
if not os.path.isdir(folder_name):
    print("Folder does not exist.")
    exit(1)

# Get a list of all files in the folder
files = os.listdir(folder_name)
# Iterate over the files
for file in files:
    # Create a new file name with the prefix "draft_"
    new_file_name = f"draft_{file}"
# Move the file to the new name
    shutil.move(os.path.join(folder_name, file), 
    os.path.join(folder_name, new_file_name))
# Print a success message
print("Files renamed successfully.")

