import os
import time

# Define the folder to clean
temp_folder = "/Users/ebarton/Documents/Projects/Automated-IT-Workflow/Python_Clean_Up"

# Get current time
now = time.time()

# Check if folder exists
if not os.path.exists(temp_folder):
    print(f"Error: Folder '{temp_folder}' does not exist.")
    exit()

# Loop through files in the folder
files_deleted = 0
for file_name in os.listdir(temp_folder):
    file_path = os.path.join(temp_folder, file_name)

    # Check if it's a file (not a folder)
    if os.path.isfile(file_path):
        last_modified = os.stat(file_path).st_mtime

        # If the file is older than 7 days, delete it
        if now - last_modified > 7 * 24 * 60 * 60:
            try:
                os.remove(file_path)
                files_deleted += 1
                print(f"✅ Deleted: {file_name}")
            except Exception as e:
                print(f"❌ Error deleting {file_name}: {e}")

print(f"\n🎉 Cleanup complete! {files_deleted} file(s) deleted.")
