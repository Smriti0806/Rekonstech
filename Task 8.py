#Task 8
import tkinter as tk
from tkinter import messagebox

def show_info():
    name = name_entry.get()
    gender = gender_var.get()
    hobbies = ""
    if reading_var.get():
        hobbies += "Reading "
    if gaming_var.get():
        hobbies += "Gaming "
    if coding_var.get():
        hobbies += "Coding"

    messagebox.showinfo("Information", f"Name: {name}\nGender: {gender}\nHobbies: {hobbies}")

def show_custom_dialog():
    custom_dialog = tk.Toplevel(root)
    custom_dialog.title("Custom Dialog")
    dialog_label = tk.Label(custom_dialog, text="This is a custom dialog box.")
    dialog_label.pack()
    close_button = tk.Button(custom_dialog, text="Close", command=custom_dialog.destroy)
    close_button.pack()

root = tk.Tk()
root.title("GUI Example")

# Name label and entry
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

# Gender label and radio buttons
gender_label = tk.Label(root, text="Gender:")
gender_label.grid(row=1, column=0)
gender_var = tk.StringVar()
male_radio = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
male_radio.grid(row=1, column=1)
female_radio = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
female_radio.grid(row=1, column=2)

# Hobbies checkboxes
hobbies_label = tk.Label(root, text="Hobbies:")
hobbies_label.grid(row=2, column=0)
reading_var = tk.BooleanVar()
reading_checkbox = tk.Checkbutton(root, text="Reading", variable=reading_var)
reading_checkbox.grid(row=2, column=1)
gaming_var = tk.BooleanVar()
gaming_checkbox = tk.Checkbutton(root, text="Gaming", variable=gaming_var)
gaming_checkbox.grid(row=2, column=2)
coding_var = tk.BooleanVar()
coding_checkbox = tk.Checkbutton(root, text="Coding", variable=coding_var)
coding_checkbox.grid(row=2, column=3)

# Buttons
info_button = tk.Button(root, text="Show Info", command=show_info)
info_button.grid(row=3, column=0)
custom_dialog_button = tk.Button(root, text="Custom Dialog", command=show_custom_dialog)
custom_dialog_button.grid(row=3, column=1)

root.mainloop()
