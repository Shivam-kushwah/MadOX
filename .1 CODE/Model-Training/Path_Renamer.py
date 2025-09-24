import os

def list_folders_and_subfolders(path, folder_name="Folder_Name"):
    print(f'{folder_name}="{path}"')
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/{}="{}"'.format(indent, folder_name, os.path.basename(root), os.path.abspath(root)))

# Using the provided path
folder_path = r"V:\Radon\Test"
folder_name = os.path.basename(folder_path)
list_folders_and_subfolders(folder_path, folder_name=folder_name)
