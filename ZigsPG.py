import tkinter as tk
import string
import random
from tkinter import filedialog


# fixed size of application window
heigth = 550
width = 400

#define a fixed style to be used for all the widgets
label_style = {
    "font": ("Arial", 14, "italic"),
    "bg": "#e6e6e6",
    "fg": "#2b2b2b",
    "padx": 8,
    "pady": 8
}

button_style = {
    "font": ("Comic Sans MS", 12, "bold"),
    "bg": "#BBBBBB",
    "fg": "#333333",
    "bd": 3,
    "relief": "ridge"
}

entry_style = {
    "font": ("Times New Roman", 12),
    "bg": "#ffffff",
    "fg": "#000000",
    "bd": 2,
    "relief": "solid"
}

frame_style = {
    "bg": "#e0e0e0",
    "bd": 2,
    "relief": "sunken"
}



#define a funciton which applies the styles to their respective widgets
def apply_styles(widget):
    if isinstance(widget, tk.Button):
        widget.config(**button_style)
    elif isinstance(widget, tk.Label):
        widget.config(**label_style)
    elif isinstance(widget, tk.Entry):
        widget.config(**entry_style)
    elif isinstance(widget, tk.Frame):
        widget.config(**frame_style)

    # Recursively apply styles to all children
    for child in widget.winfo_children():
        apply_styles(child)


# define a command that generates password
def generate_password():
    length = int(length_entry.get())
    
    character_pool = ""
    if var_letters.get() == 1:
        character_pool += string.ascii_letters
    if var_digits.get() == 1:
        character_pool += string.digits
    if var_punctuation.get() == 1:
        character_pool += string.punctuation
    
    # if the user does not select any of the characters to include, use letter only
    if not character_pool:
        character_pool = string.ascii_letters
    
    password = ''.join(random.choice(character_pool) for _ in range(length))
    
    keyword = keyword_entry.get()
    if keyword:
        password = password[:len(password)//2] + keyword + password[len(password)//2:]
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


# define a function that copies the password to the clipboard of the user
def copy_password():
    root.clipboard_clear()
    password = password_entry.get()
    root.clipboard_append(password)

def cut_password():
    root.clipboard_clear()
    copy_password()    
    password_entry.delete(0, tk.END)

def save_password():
    password = password_entry.get()
    if password:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                 filetypes=[("Text files", "*.txt"), 
                                                            ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(password)




# define a function the creates the gui of the application
def create_gui():
    global root, length_entry,keyword_entry, password_entry, var_digits, var_letters, var_punctuation
    root = tk.Tk()
    root.title("Zigla's Password Generator")
    root.geometry(f"{width}x{heigth}")
    root.resizable(False,False)

    content_frame = tk.Frame(root).pack(pady=10)

    length_label = tk.Label(content_frame, text="Enter Password Length:")
    length_label.pack(pady=10)

    length_entry = tk.Entry(content_frame, width=30)
    length_entry.pack(pady=5)

    # set initial state for the characters to be included in the password
    var_letters = tk.IntVar(value=1)
    var_digits = tk.IntVar(value=1)
    var_punctuation = tk.IntVar(value=1)

    letters_checkbox = tk.Checkbutton(content_frame, text="Letters (A-Z, a-z)", variable=var_letters)
    letters_checkbox.pack(pady=3)

    digits_checkbox = tk.Checkbutton(content_frame, text="Digits (0-9)", variable=var_digits)
    digits_checkbox.pack(pady=3)

    punctuation_chechbox = tk.Checkbutton(content_frame, text="Punctuation (!@#$%^&*)", variable=var_punctuation)
    punctuation_chechbox.pack(pady=3)

    keyword_label = tk.Label(content_frame, text="Enter an optional keyword:")
    keyword_label.pack(pady=10)
    keyword_entry = tk.Entry(content_frame, width=30)
    keyword_entry.pack(pady=5)

    generate_button = tk.Button(content_frame, text="Generate Password", command=generate_password)
    generate_button.pack(pady=20)

    # Entry to display the generated password
    password_entry = tk.Entry(content_frame, width=35)
    password_entry.pack(pady=10)

    buttons_frame = tk.Frame(root)
    buttons_frame.pack(pady=10)

    copy_button = tk.Button(buttons_frame, text="Copy", command=copy_password)
    copy_button.pack(side="left", padx=5)

    cut_button = tk.Button(buttons_frame, text="Cut", command=cut_password)
    cut_button.pack(side="left", padx=5)

    save_button = tk.Button(buttons_frame, text="Save", command=save_password)
    save_button.pack(side="left", padx=5)

    apply_styles(root)

    root.mainloop() 


create_gui()

    








