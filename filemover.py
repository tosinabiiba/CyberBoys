import os
import time

# Constants for the source and destination folders and the file extensions to classify
SRC_FOLDER = '/Users/tosinabiiba/Downloads'
DST_FOLDER = '/Desktop/backed_up'
CLASSIFICATIONS = {
    'txt': 'text_files',
    'doc': 'document_files',
    'jpg': 'image_files',
}

# Function to classify a file based on its extension
def classify_file(filename):
    # Extract the file extension from the filename
    _, file_extension = os.path.splitext(filename)
    # Return the classification based on the file extension
    return CLASSIFICATIONS.get(file_extension[1:], 'other_files')

# Function to move a file to the appropriate destination folder
def move_file(src_path, dst_folder):
    # Get the filename from the source path
    filename = os.path.basename(src_path)
    # Classify the file based
