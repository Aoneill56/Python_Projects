# File Organizer — Step‑by‑Step Breakdown

A tidy, portfolio‑ready explanation of a Python script that organizes files into audio/video/image buckets and collects subfolders.

> **Tip for readers:** This README is structured so you can paste your own explanations under each heading (look for the **“Your notes”** lines) and trim sections you don’t need.

---

## Table of Contents

* [Overview](#overview)
* [Prerequisites](#prerequisites)
* [Imports](#imports)
* [Working Directory Helpers](#working-directory-helpers)
* [Prompt for Target Directory](#prompt-for-target-directory)
* [Change Working Directory](#change-working-directory)
* [Create Destination Folders](#create-destination-folders)
* [File Type Buckets (extensions)](#file-type-buckets-extensions)
* [Folder Registry (dictionary)](#folder-registry-dictionary)
* [Helper Functions](#helper-functions)
* [Main Walk (oswalk)](#main-walk-oswalk)

  * [Handling Files](#handling-files)
  * [Handling Subfolders](#handling-subfolders)
* [Error Handling](#error-handling)
* [Why This Is Portfolio‑Worthy](#why-this-is-portfolio-worthy)
* [How to Run](#how-to-run)
* [Optional Improvements](#optional-improvements)
* [Safety Notes](#safety-notes)

---

## Overview

Organizes a target folder by moving files into destination folders based on extension (audio, video, image) and by collecting subfolders into a single "folders" directory.

**Your notes:** *Explain the problem this solves and the target users (e.g., tidying a downloads folder, photo dump cleanup, etc.).*

---

## Prerequisites

* Python 3.8+
* Windows paths are shown in examples, but the logic is cross‑platform.

**Your notes:** *Mention any virtual environment, IDE, or permissions needed.*

---

## Imports

```python
import os
import shutil
```

* **os** → file paths, directories, environment (cross‑platform).
* **shutil** → high‑level file operations (move/copy/delete).

**Your notes:** *Why these two are sufficient vs. extra dependencies.*

---

## Working Directory Helpers

```python
print(os.getcwd())  # shows current working directory
```

* Prints the current working directory (CWD). Helps you confirm where the script starts.

**Your notes:** *When you’d use this and what to expect.*

---

## Prompt for Target Directory

```python
chdir = input(
    'Enter a dir here for Python to organize\n'
    'such as "C:\\Users\\Example\\Desktop\\Example\\" \n'
    'Enter here : '
)
```

* Prompts the user for the path of the folder to organize and stores it in `chdir`.
* **Windows tip:** In Python string literals, backslashes must be escaped (`\\`) or use raw strings (`r"C:\\path"`). For user input, they can paste the path as‑is.

---

## Change Working Directory

```python
os.chdir(chdir)
print(os.getcwd())  # confirm we changed into the target directory
```

* Changes Python’s CWD to the folder the user entered.
* The print verifies you’re inside the right place before any moves happen.

**Your notes:** *Call out what happens if the path is invalid (consider wrapping in try/except).*

---

## Create Destination Folders

```python
os.makedirs("C:/Users/Example/Documents/audio", exist_ok=True)
os.makedirs("C:/Users/Example/Documents/video", exist_ok=True)
os.makedirs("C:/Users/Example/Documents/img", exist_ok=True)
os.makedirs("C:/Users/Example/Documents/folders", exist_ok=True)
```

* `os.makedirs(path, exist_ok=True)` creates the folder if it doesn’t already exist.
* These are your **destination** folders where items will be sorted.

> **Note:** Consider using a single base path variable to avoid repetition:
>
> ```python
> BASE = "C:/Users/Example/Documents"
> DEST = {"audio": f"{BASE}/audio", "video": f"{BASE}/video", "img": f"{BASE}/img", "folders": f"{BASE}/folders"}
> for p in DEST.values():
>     os.makedirs(p, exist_ok=True)
> ```

**Your notes:** *Explain where you want the destinations to live and why they’re outside the source directory.*

---

## File Type Buckets (extensions)

```python
audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff", "...")
video = (".webm", ".MTS", ".M2TS", ".TS", ".mov", "...")
img   = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png", "...")
```

* Tuples list extensions per category. You’ll check a file’s extension to decide where it goes.
* **Good practice:** Normalize the extension with `.lower()` before checking.

---

## Folder Registry (dictionary)

```python
folders = {}
# Example shape later: {"Music": "C:/Users/.../Music"}
```

* Keeps track of discovered subfolder names and their full paths.

**Your notes:** *How/where you use this registry (e.g., for reporting or skipping known folders).*

---

## Helper Functions

```python
def is_audio(file: str) -> bool:
    return os.path.splitext(file)[1].lower() in audio

# Similar helpers for video and images
def is_video(file: str) -> bool:
    return os.path.splitext(file)[1].lower() in video

def is_img(file: str) -> bool:
    return os.path.splitext(file)[1].lower() in img

# Folder registry helper
def add_folder(category: str, path: str) -> None:
    if os.path.isdir(path):
        folders[category] = path
    else:
        print(f"{path} is not a directory!")
```

* `os.path.splitext(file)[1]` returns the extension (e.g., `.mp3`).
* `add_folder` safely registers known folders.

**About the Functions:** *I've split this into functions / helpers for easier readability, maintability and debugging. splittext seperates the file name from the extension
we then pass the argument of file into the function, this will be the string representing the path to a file or full a full path including the extention the tuple index selctor [1] selects the 2nd part 
i.e the ext and the 'return' returns a tuple seperate from audio tuple and checks the [1] / 2nd index value (so the extension) in the split.text tuple temporarily created, to see if there's a match*

---

## Main Walk (`os.walk`)

```python
for root, dirs, files in os.walk(chdir):
    # root: current directory path being walked
    # dirs: list of subfolder names under root
    # files: list of file names under root
    ...
```

* Recursively traverses the target directory.

**Your notes:** *Briefly explain recursion and what each variable represents.*

### Handling Files

```python
for file in files:
    file_path = os.path.join(root, file)

    try:
        if is_video(file):
            shutil.move(file_path, "C:/Users/Aj-on/Documents/video")
            print(f"Moved {file} to video")
        elif is_img(file):
            shutil.move(file_path, "C:/Users/Aj-on/Documents/img")
            print(f"Moved {file} to img")
        elif is_audio(file):
            shutil.move(file_path, "C:/Users/Aj-on/Documents/audio")
            print(f"Moved {file} to audio")
    except shutil.Error as err:
        print(f"Duplicate? Skipping {file_path} → {err}")
    except PermissionError:
        print(f"Skipping {file_path} (no permission)")
    except Exception as e:
        print(f"Unexpected error with {file_path}: {e}")
```

* Builds absolute file paths and moves them based on category.
* Prints each action for traceability.

**Your notes:** *Mention what happens to unknown file types (e.g., leave in place).*

### Handling Subfolders

```python
for d in dirs:
    folder_path = os.path.join(root, d)
    folders[d] = folder_path  # register it
    try:
        shutil.move(folder_path, "C:/Users/Aj-on/Documents/folders")
        print(f"Moved {d} to folders")
    except shutil.Error as err:
        print(f"Duplicate? Skipping {folder_path} → {err}")
    except PermissionError:
        print(f"Skipping {folder_path} (no permission)")
    except Exception as e:
        print(f"Unexpected error with {folder_path}: {e}")
```

* Records each subfolder then attempts to move it into a consolidated `folders` directory.
* **Important:** Ensure your destination is **outside** the source tree to avoid moving a folder into itself.

**Your notes:** *Discuss whether you want to skip certain system/app folders, or preserve structure.*

---

## Error Handling

* **`shutil.Error`** → a file/folder with the same name may already exist at the destination.
* **`PermissionError`** → OS blocked access (e.g., system files).
* **Generic `Exception`** → catch‑all for unexpected issues so the loop keeps going.

**Your notes:** *How you’d surface a final summary (counts moved, skipped, errored).*

---

## Why This Is Portfolio‑Worthy

* Uses **`os.walk`** to demonstrate recursive traversal.
* Practical **error handling** for real‑world file operations.
* Uses a **dictionary** to register folders (basic data structures in action).
* **Clear separation of concerns** via helper functions.

**Your notes:** *Tie this to problem‑solving, maintainability, and user experience.*

---

## How to Run

1. Save the script as `organize.py`.
2. Run from a terminal:

   ```bash
   python organize.py
   ```
3. Paste the path to the directory you want to organize when prompted.

**Your notes:** *Add sample paths and expected terminal output.*

---

## Optional Improvements

* **Normalize extensions**: compare using `ext.lower()`.
* **Skip destinations**: don’t reprocess `audio/`, `video/`, `img/`, `folders/` if they sit under the source by mistake.
* **Dry‑run mode**: print planned moves without changing anything (`--dry-run`).
* **Conflict strategy**: on name collisions, append a counter/timestamp instead of skipping.
* **Logging**: write actions to a `.log` file with `logging` module.
* **Config file**: load extension lists and destinations from `config.json`.
* **`pathlib`**: cleaner path handling across platforms.
* **Progress & summary**: counts per type, total bytes moved.
* **Unit tests**: for helpers like `is_audio/is_video/is_img`.

**Your notes:** *Pick 2–3 improvements you’ll implement next and why.*

---

## Safety Notes

* **Back up** important data before bulk moves.
* **Permissions**: expect some files/folders to be locked by the OS.
* **Destination location**: keep destinations outside the source tree.
* **Reversibility**: consider logging or a manifest to undo moves if needed.

**Your notes:** *Any organization policies or constraints to respect (e.g., work machine rules).*

---

> **Quick status print**
>
> ```python
> print("\nDone! Total folders found:", len(folders))
> ```
>
> Use this to report how many folders were registered; extend with a final summary if desired.
