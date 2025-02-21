import os
import time

# Define the folder to clean (you can change this path)
temp_folder = "/home/ebarton/Temp"

# Get the current time
now = time.time()

# Loop through files in the folder
for file_name in os.listdir(temp_folder):
    file_path = os.path.join(temp_folder, file_name)

    # Check if it's a file (not a folder)
    if os.path.isfile(file_path):

        # Get the file's last modified time
        last_modified = os.stat(file_path).st_mtime

        # If the file is older than 7 days, delete it
        if now - last_modified > 7 * 24 * 60 * 60:
            try:
                print(f"Deleting {file_name}...")
                os.remove(file_path)
            except Exception as e:
                print(f"Error deleting {file_name}: {e}")
