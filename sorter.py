import os
import shutil

# Set the path to the downloads folder
downloads_folder = '/Users/tosinabiiba/Downloads'

# Set the path to the destination folder
destination = '/Users/tosinabiiba/Desktop/backed_up'

# Create a dictionary of file extensions and their corresponding destination folders
extensions = {
    'docx': 'documents',
    'stl': '3Dprints',
    'xlsx': 'spreadsheets',
    'pptx': 'presentations',
    'pdf': 'documents',
    'txt': 'documents',
    'png': 'images',
    'jpg': 'images',
    'jpeg': 'images',
    'gif': 'images',
    'mp3': 'music',
    'mp4': 'videos'
}

# Get a list of all the files in the downloads folder
files = os.listdir(downloads_folder)

# Iterate over the files
for file in files:
    # Get the file extension
    extension = file.split('.')[-1]

    # Check if the extension is in the dictionary
    if extension in extensions:
        # Get the destination folder for the file
        folder = extensions[extension]

        # Set the path to the destination folder for the file
        folder_path = os.path.join(destination, folder)

        # Check if the folder exists
        if not os.path.exists(folder_path):
            # Create the folder if it doesn't exist
            os.makedirs(folder_path)

        # Set the path to the file in the downloads folder
        file_path = os.path.join(downloads_folder, file)

        # Set the path to the destination file
        destination_path = os.path.join(folder_path, file)

        # Move the file to the destination folder
        shutil.move(file_path, destination_path)

""" 
This script will scan the files in the downloads folder, and sort them into subfolders based on their file extension. 
The subfolders are defined in the extensions dictionary, which maps file extensions to destination folder names. 
The script uses the shutil module to move the files to the appropriate destination folders.
"""