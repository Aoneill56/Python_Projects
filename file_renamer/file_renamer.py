import os
import re 
import shutil

#Path to the folder we want to rename
chdir = "/home/aaron/Documents/video/RHCSA9/"
# os.chdir(chdir)

pattern = re.compile(r"^\.+(\d+)*\s*")
for filename in os.listdir(chdir):
    new_name = pattern.sub("", filename)
    if new_name !=  filename:
        old_path = os.path.join(chdir, filename)
        new_path = os.path.join(chdir, new_name)
        
        try: 
                shutil.move(old_path, new_path)
                print(f"Renamed {filename} -> {new_name}")
        except os.error as e:
            print(f"Error renaming {filename}: {e}")
