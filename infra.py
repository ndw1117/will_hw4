import os
import shutil

def setup_folder(old_path, new_parent_path, new_name):
    try:
        new_path = os.path.join(new_parent_path, new_name)

        shutil.move(old_path, new_path)
    except Exception as e:
        return

media_folder_path = '/bin'
new_parent_directory = '/opt'
new_folder_name = 'ct'

setup_folder(media_folder_path, new_parent_directory, new_folder_name)