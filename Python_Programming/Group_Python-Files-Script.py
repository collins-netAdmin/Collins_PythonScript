import os
import shutil

# Define the source and destination directories
source_dir = 'C:\Collins_PythonScript'
destination_dir = 'C:\Collins_PythonScript\Python Programming'

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Loop through all files in the source directory
for filename in os.listdir(source_dir):
    # Check if the file has a .py extension
    if filename.endswith('.py'):
        # Construct full file path
        file_path = os.path.join(source_dir, filename)
        # Move the file to the destination directory
        shutil.move(file_path, destination_dir)

print("All .py files have been moved to the destination directory.")
