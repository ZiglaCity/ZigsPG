import tkinter as tk

# fixed size of application window
heigth = 500
width = 400


# define a function the creates the gui of the application
def create_gui():
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

    generate_button = tk.Button(content_frame, text="Generate Password")
    generate_button.pack(pady=20)

    # Entry to display the generated password
    password_entry = tk.Entry(content_frame, width=35)
    password_entry.pack(pady=10)

    buttons_frame = tk.Frame(root)
    buttons_frame.pack(pady=10)

    copy_button = tk.Button(buttons_frame, text="Copy")
    copy_button.pack(side="left", padx=5)

    cut_button = tk.Button(buttons_frame, text="Cut")
    cut_button.pack(side="left", padx=5)

    save_button = tk.Button(buttons_frame, text="Save")
    save_button.pack(side="left", padx=5)

    root.mainloop()


create_gui()

    








