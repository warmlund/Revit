import os
import re

def remove_family_backups(directory):
    # Define a regex pattern to match the file structure: <model_name>.<nnnn>.rfa
    pattern = r"^.*\.\d{4}\.rfa$"
    number_of_families_removed=0

    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        # Find files that match the given pattern
        for file_name in files:
            if re.match(pattern, file_name):
                file_path = os.path.join(root, file_name)
                try:
                    os.remove(file_path)  # Remove the file
                    print(f"Deleted: {file_path}")
                    number_of_families_removed+=1
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
    print(f"Total backups deleted: {number_of_families_removed}")

def get_input():
    print("Please enter directory: ")
    directory = input()
    return directory

directory=""

while(os.path.exists(directory)==False):
    directory=get_input()
    if os.path.exists(str(directory)):
        remove_family_backups(directory)

    else:
        print("Directory is not valid")
