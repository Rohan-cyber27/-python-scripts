import shutil
import os
from datetime import datetime

def backup(source_dir,backup_dir):
    if not os.path.exists(source_dir):
        print(f"source directory {source_dir}does not exst. ")
        return

    timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir=os.path.join(backup_dir,f"backup_{timestamp}")

    try:
        shutil.copytree(source_dir,backup_dir)
        print(f"back completed : {backup_dir}")
    except Exception as e:
        print(f"failed to backup: {e}")

source_directory=input("enter the source directory: ")
destination_directory=input("enter the destination directory: ")

backup(source_directory,destination_directory)