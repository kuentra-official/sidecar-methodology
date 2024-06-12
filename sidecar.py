import tkinter as tk
from tkinter import ttk
import os
import tempfile
def replace_file():
    # replace aws or gcp, when aws, using boto3
    source_file = 'stable.exe'  
    target_file = 'app.exe'  
    temp_file = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())  

    try:
        file_size = os.path.getsize(source_file)
        
        progress_bar['value'] = 0
        progress_bar["maximum"] = file_size

        with open(source_file, 'rb') as fsrc, open(temp_file, 'wb') as fdst:
            copied = 0  
            while True:
                buffer = fsrc.read(1024*1024)  
                if not buffer:
                    break
                fdst.write(buffer)
                copied += len(buffer)
                update_progress(copied)

        os.replace(temp_file, target_file)
        print("File replacement completed.")
    except Exception as e:
        print(f"An error occurred: {e}")

def update_progress(copied):
    progress_bar['value'] = copied
    root.update_idletasks()

root = tk.Tk()
root.title("File Replacer")

progress_bar = ttk.Progressbar(root, length=200, mode='determinate')
progress_bar.pack(pady=20)

replace_button = ttk.Button(root, text="Replace File", command=replace_file)
replace_button.pack(pady=10)

root.mainloop()
