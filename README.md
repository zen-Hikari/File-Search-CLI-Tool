# 🔍 File Search CLI Tool

🚀 **File Search CLI Tool** is a powerful Python-based tool that allows you to search for files by name or extension across all drives or within a specific directory. It features an elegant loading animation and multi-threaded search for faster results.

![Preview](https://raw.githubusercontent.com/zen-Hikari/File-Search-CLI-Tool/refs/heads/main/preview.png)  

# ------------------------------------------------------------
# 🔥 File Search CLI Tool by Noval 🔥
# Please do not remove this credit if you modify the script.
# ------------------------------------------------------------


---

## 📌 Features

✅ Search files by **name** or **extension** (e.g., .txt, .pdf, .png, etc.)  
✅ Scan **all drives (C, D, E, etc.)** or a specific directory  
✅ **Multi-threaded processing** for faster search  
✅ **Loading animation** while searching  
✅ Adjustable **search depth** with `max_depth`  
✅ **Cool ASCII art** on startup 💻  

---

## 🛠️ Installation & Usage

### 1️⃣ **Clone the Repository**
```bash
$ git clone https://github.com/zen-Hikari/File-Search-CLI-Tool.git
$ cd File-Search-CLI-Tool
```

### 2️⃣ **Install Python (If Not Installed)**
Ensure you have **Python 3.6+** installed. If not, download it from [python.org](https://www.python.org/downloads/).

Check your Python version:
```bash
$ python --version
```

### 3️⃣ **Run the Script**
```bash
$ python File_Founder.py
```
Then, enter the file name or extension you want to search for.

#### Example Input:
```
Enter file extension or name file for specific file: .txt
Enter drive D or C (leave empty for all drives): (press Enter)
```

#### Example Output:
```
Looking for files... ⠙
-------------------------------------------------------------
File Found:
-------------------------------------------------------------
D:\Documents\notes.txt
C:\Users\YourName\Desktop\todo.txt
```

---

## ⚙️ Adjusting Search Depth (`max_depth`)
By default, `max_depth = 5`. If you want to increase or limit the search depth, modify the `max_depth` value in `File_Founder.py`:

```python
def find_files(search_term, folder_path=None, max_depth=5):
```
Replace `5` with the desired depth value. A higher number increases search coverage but may slow down the process.

---

## 📜 Code Snippet
```python
def search_in_drive(drive, search_term, is_extension, max_depth=5):
    matching_files = []
    search_term_lower = search_term.lower()
    try:
        for root, _, files in os.walk(drive, topdown=True):
            depth = root.count(os.sep) - drive.count(os.sep)
            if depth > max_depth:
                continue  # Skip if folder depth exceeds the limit
            for file in files:
                if (is_extension and file.lower().endswith(search_term_lower)) or (not is_extension and search_term_lower in file.lower()):
                    matching_files.append(os.path.join(root, file))
    except (PermissionError, FileNotFoundError):
        pass
    return matching_files
```

---

## 📜 License
MIT License. Feel free to use and improve this tool.

If you like this project, don't forget to **⭐ Star the repo!** 😎

