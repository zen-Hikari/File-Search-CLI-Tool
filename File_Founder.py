import os
import sys
import itertools
import threading
from concurrent.futures import ThreadPoolExecutor

def loading_animation(stop_event):
    spinner = itertools.cycle(["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"])
    message = "Looking for files... "
    
    while not stop_event.is_set():
        sys.stdout.write(f"\r{message}{next(spinner)} ")
        sys.stdout.flush()
        stop_event.wait(0.1)

    sys.stdout.write("\r" + " " * (len(message) + 2) + "\r")  # Hapus animasi setelah selesai
    sys.stdout.flush()

def search_in_drive(drive, search_term, is_extension, max_depth=5):
    matching_files = []
    search_term_lower = search_term.lower()
    try:
        for root, _, files in os.walk(drive, topdown=True):
            depth = root.count(os.sep) - drive.count(os.sep)
            if depth > max_depth:
                continue  # Lewati jika kedalaman folder melebihi batas
            
            for file in files:
                file_lower = file.lower()
                if (is_extension and file_lower.endswith(search_term_lower)) or (not is_extension and search_term_lower in file_lower):
                    matching_files.append(os.path.join(root, file))  
    except (PermissionError, FileNotFoundError):
        pass  # Langsung skip tanpa menampilkan error
    return matching_files

def find_files(search_term, folder_path=None, max_depth=5):
    is_extension = search_term.startswith(".")  
    if folder_path:
        if os.path.exists(folder_path):
            if not folder_path.endswith("\\"):  
                folder_path += "\\"
            drives = [folder_path]
        else:
            print(f"The specified path '{folder_path}' does not exist. Searching all drives instead.")
            drives = [f"{chr(d)}:\\" for d in range(65, 91) if os.path.exists(f"{chr(d)}:\\")]
    else:
        drives = [f"{chr(d)}:\\" for d in range(65, 91) if os.path.exists(f"{chr(d)}:\\")]

    stop_event = threading.Event()
    loading_thread = threading.Thread(target=loading_animation, args=(stop_event,))
    loading_thread.start()

    matching_files = []
    with ThreadPoolExecutor(max_workers=5) as executor:  
        results = executor.map(lambda drive: search_in_drive(drive, search_term, is_extension, max_depth), drives)
    
    for result in results:
        matching_files.extend(result)  

    stop_event.set()
    loading_thread.join()  # Hentikan animasi loading setelah pencarian selesai
    print("\n" + "-" * 65)  

    if matching_files:
        print("\nFile Found:\n" + "-" * 65)  # Tambahkan teks "File Found:"
        print("\n".join(matching_files))
    else:
        print(f"No files found matching '{search_term}'.")

if __name__ == "__main__":
    ascii_noval = """
       ███╗   ██╗ ██████╗ ██╗   ██╗ █████╗ ██╗     
       ████╗  ██║██╔═══██╗██║   ██║██╔══██╗██║     
       ██╔██╗ ██║██║   ██║██║   ██║███████║██║     
       ██║╚██╗██║██║   ██║██║   ██║██╔══██║██║     
       ██║ ╚████║╚██████╔╝╚██████╔╝██║  ██║███████╗
   By: ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝
    """
    
    print("\033[1;36m" + "-" * 65)  # Warna Cyan
    print(ascii_noval)
    print("-" * 65 + "\033[0m")  # Reset warna
    
    search_term = input("\nEnter file extension or name file for specific file: ").strip()
    folder_path = input("Enter drive D or C (leave empty for all drives): ").strip()
    
    if folder_path and not folder_path.endswith(":\\"):
        folder_path += ":\\"  

    print("-" * 65)
    find_files(search_term, folder_path if folder_path else None, max_depth=5)
