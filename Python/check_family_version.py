import os
import re

# Function to extract and check Revit version from a Revit family file
def get_revit_version_from_rfa(file_path):
    try:
        # Read the .rfa file as binary
        with open(file_path, 'rb') as file:
            content = file.read()

            # Decode to a string for XML parsing (ignoring errors)
            content_str = content.decode('utf-8', errors='ignore')

            # Use regex to search for the <A:product-version> tag
            match = re.search(r'<A:product-version>(.*?)</A:product-version>', content_str)
            if match:
                return match.group(1)  # Return the version number found
            else:
                return "Version info not found"
    except Exception as e:
        return f"Error reading {file_path}: {str(e)}"

# Function to loop through a directory and check all .rfa files
def check_directory_for_revit_versions(directory_path):
    for root_dir, dirs, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith('.rfa'):
                file_path = os.path.join(root_dir, file_name)
                version = get_revit_version_from_rfa(file_path)
                print(f"File: {file_name}, Version: {version}")

# Directory containing the Revit families (.rfa files)
directory_path = "directory/path/here"

# Run the check
check_directory_for_revit_versions(directory_path)