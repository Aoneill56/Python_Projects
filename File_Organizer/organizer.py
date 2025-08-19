import os, shutil  #import

print(os.getcwd())

chdir = input('Enter a dir here for Python to organize\n'
'such as "C/Users/Example/Desktop/Example" \n' \
'Enter here : ')

os.chdir(chdir)

print(os.getcwd())

os.makedirs("C:/Users/Aj-on/Documents/audio", exist_ok=True)
os.makedirs("C:/Users/Aj-on/Documents/video", exist_ok=True)
os.makedirs("C:/Users/Aj-on/Documents/img", exist_ok=True)
os.makedirs("C:/Users/Aj-on/Documents/folders", exist_ok=True)



audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

folders = {}

def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_img(file):
    return os.path.splitext(file)[1] in img

def add_folder(category, path):
    if os.path.isdir(path):   # make sure it's really a folder
        folders[category] = path
    else:
        print(f"{path} is not a directory!")

print("\nDone! Total folders found:", len(folders))


for root, dirs, files in os.walk(chdir):
    for file in files:

        file_path = os.path.join(root, file)

        if is_video(file):
            shutil.move(file_path, "C:/Users/Aj-on/Documents/video")
            print(f"Moved {file} to C:/Users/Aj-on/Documents/video")

        elif is_img(file):
            shutil.move(file_path, "C:/Users/Aj-on/Documents/img")
            print(f"Moved {file} to C:/Users/Aj-on/Documents/img")

        elif is_audio(file):
            shutil.move(file_path, "C:/Users/Aj-on/Documents/audio")
            print(f"Moved {file} to C:/Users/Aj-on/Documents/audio")

    for d in dirs:
        
        folder_path = os.path.join(root, d)

        folders[d] = folder_path

        try:
            shutil.move(folder_path, "C:/Users/Aj-on/Documents/folders")
            print(f"Moved {d} to C:/Users/Aj-on/Documents/folders")

        except shutil.Error as err:
            print(f"Duplicate? Skipping {file_path} → {err}")
        except PermissionError:
            print(f"Skipping {file_path} (no permission)")
        except Exception as e:
            print(f"Unexpected error with {file_path}: {e}")
        
