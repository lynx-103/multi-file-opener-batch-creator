import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
import os

# I just made some BULLSHIT :sob::sob:

def createfile():
    output_text.config(state='normal')
    output_text.delete(1.0, tk.END)
    global filename
    update_filename()
    filename = filename + ".bat"
    output_text.insert(tk.END, f"Creating {filename}...\n")
    with open(filename, "w") as file:
        for command in commands:
            file.write(command)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    output_text.insert(tk.END, f"{filename} created successfully at {file_path}!\n")
    output_text.insert(tk.END, "Resetting...\n")
    commands.clear()
    appstoopen.config(state='normal')
    appstoopen.delete(1.0, tk.END)
    appstoopen.config(state='disabled')
    output_text.insert(tk.END, "Reset Complete!\n")
    output_text.config(state='disabled')

def selectapp():
    global commands
    file = filedialog.askopenfilename(
        title="Select a file to open",
        filetypes=(("Executable files", "*.exe"), ("All files", "*.*"), ("Batch files", "*.bat"), ("Python files", "*.py"))
        )
    if file:
        commands.append(f'start "" "{file}"\n')
    appstoopen.config(state='normal')
    appstoopen.insert(tk.END, file + "\n")
    appstoopen.config(state='readonly')

def update_filename():
    global filename
    filename = filenamebox.get()

root = tk.Tk()
root.title("Multi-File Opener Batch Creator")
root.geometry("400x500")

commands = []
filename = "untitled"

filename_label = tk.Label(root, text="Batch File Name (without extension):")
filename_label.pack(pady=10)

filenamebox = tk.Entry(root)
filenamebox.pack(pady=10)
filenamebox.insert(0, "untitled")

select_button = tk.Button(root, text="Add Files to Open", command=selectapp)
select_button.pack(pady=10)

filestoopen_label = tk.Label(root, text="Files to Open:")
filestoopen_label.pack(pady=5)

appstoopen = scrolledtext.ScrolledText(root, height=10, width=40, state='disabled')
appstoopen.pack(pady=10)

create_button = tk.Button(root, text="Create Batch File", command=createfile)
create_button.pack(pady=10)

output_label = tk.Label(root, text="Output:")
output_label.pack(pady=5)

output_text = scrolledtext.ScrolledText(root, height=5, width=40, state='disabled')
output_text.pack(pady=10)

root.mainloop()