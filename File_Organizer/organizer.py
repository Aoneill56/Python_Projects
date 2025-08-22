import os, shutil
chdir = '/home/aaron/Downloads/'

os.chdir(chdir)

print(os.getcwd())

os.makedirs("/home/aaron/Documents/audio/", exist_ok=True)
os.makedirs("/home/aaron/Documents/video/", exist_ok=True)
os.makedirs("/home/aaron/Documents/img/", exist_ok=True)
os.makedirs("/home/aaron/Documents/Readable/", exist_ok=True)



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

documents = (".pdf", ".txt", ".docx")

def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_img(file):
    return os.path.splitext(file)[1] in img

def is_document(file):
    return os.path.splitext(file)[1] in documents

for root, dirs, files in os.walk(chdir):
    for x in files:

        file_path = os.path.join(root, x)
        
        try:
            if is_video(x):
                shutil.move(file_path, "/home/aaron/Documents/video/")
                print(f"Moved {x} to /home/aaron/Documents/video/")
            

            if is_img(x):
                shutil.move(file_path, "/home/aaron/Documents/img/")
                print(f"Moved {x} to /home/aaron/Documents/img/")


            if is_audio(x):
                shutil.move(file_path, "/home/aaron/Documents/audio/")
                print(f"Moved {x} to /home/aaron/Documents/audio/")

        
            if is_document(x):
                shutil.move(file_path, "/home/aaron/Documents/Readable/")
                print(f"Moved {x} to /home/aaron/Documents/Readable/")
             
        except OSError as err:
            print(err)
