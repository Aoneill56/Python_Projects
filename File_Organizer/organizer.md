# File Organizer Script

This Python script organizes files from the **Downloads** folder into categorized subfolders inside **Documents**.  

## How It Works
1. **Change working directory**  
   The script starts in `/home/aaron/Downloads`.

2. **Create folders if they don't exist**  
   - `/home/aaron/Documents/audio/`  
   - `/home/aaron/Documents/video/`  
   - `/home/aaron/Documents/img/`  
   - `/home/aaron/Documents/Readable/`  

3. **Define file type categories**  
   - **Audio**: `.mp3`, `.wav`, `.flac`, etc.  
   - **Video**: `.mp4`, `.mov`, `.webm`, etc.  
   - **Images**: `.jpg`, `.png`, `.gif`, etc.  
   - **Documents**: `.pdf`, `.txt`, `.docx`  

4. **Walk through Downloads folder**  
   - For each file, check its extension.  
   - If it matches a category, move it to the right folder using `shutil.move()`.  
   - Print a confirmation message.  

5. **Error handling**  
   If a file can’t be moved, the error is printed instead of crashing.

   
## Purpose
This script helps keep your **Downloads** folder clean by automatically sorting files into appropriate folders inside **Documents**.
