import os
import shutil

# Use absolute path to Downloads folder in home directory
source_folder = os.path.expanduser('~/Downloads')
destination_folders = {
    'Images': ['.jpg', '.png', '.gif', '.jpeg', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.doc'],
    'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
    'Zip Files': ['.zip', '.rar', '.tar.xz', '.tar.gz'],
    'Sql Files': ['.sql'],
    'Debian File': ['.deb'],
    'Iso Files': ['.iso'],
    'Ova Files': ['.ova']
}

print(f"Scanning folder: {source_folder}")
if not os.path.exists(source_folder):
    print("Error: Downloads folder not found!")
    exit(1)

files_moved = 0
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)
    if os.path.isfile(file_path):
        print(f"Found file: {file}")
        for folder, extensions in destination_folders.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                dest_folder = os.path.join(source_folder, folder)
                os.makedirs(dest_folder, exist_ok=True)
                dest_path = os.path.join(dest_folder, file)
                
                try:
                    shutil.move(file_path, dest_path)
                    print(f"Moved {file} to {folder}")
                    files_moved += 1
                except shutil.Error as e:
                    print(f"Error moving {file}: {e}")
                except OSError as e:
                    print(f"OS error moving {file}: {e}")
                break  # Exit inner loop after moving file

print(f"Finished! Moved {files_moved} files. /n Works like a  charm!")