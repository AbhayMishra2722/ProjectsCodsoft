import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be positive.")
            return

        characters = ""
        if var_letters.get():
            characters += string.ascii_letters
        if var_numbers.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Please select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))

        result_entry.config(show="")  # Reset visibility when generating new password
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)

        update_strength(password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def update_strength(password):
    # Check for basic strength criteria
    length = len(password)
    has_letters = any(c.isalpha() for c in password)
    has_numbers = any(c.isdigit() for c in password)
    has_symbols = any(c in string.punctuation for c in password)

    if length < 6:
        strength = "Weak"
        color = "red"
    elif length < 10:
        if has_letters and (has_numbers or has_symbols):
            strength = "Medium"
            color = "orange"
        else:
            strength = "Weak"
            color = "red"
    else:
        if has_letters and has_numbers and has_symbols:
            strength = "Strong"
            color = "green"
        else:
            strength = "Medium"
            color = "orange"

    strength_label.config(text=f"Strength: {strength}", fg=color)

def copy_to_clipboard():
    password = result_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy.")

def toggle_password():
    if show_var.get():
        result_entry.config(show="")
    else:
        result_entry.config(show="*")

# Main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x400")
root.configure(bg="#f0f4f7")

# Header
tk.Label(root, text="Advanced Password Generator", font=("Helvetica", 16, "bold"), bg="#f0f4f7").pack(pady=10)

# Password length
tk.Label(root, text="Enter password length:", font=("Arial", 12), bg="#f0f4f7").pack(pady=5)
length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack()

# Options for character types
var_letters = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=var_letters, font=("Arial", 10), bg="#f0f4f7").pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Numbers", variable=var_numbers, font=("Arial", 10), bg="#f0f4f7").pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols, font=("Arial", 10), bg="#f0f4f7").pack(anchor="w", padx=50)

# Generate button
tk.Button(root, text="Generate Password", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=generate_password).pack(pady=10)

# Result entry
result_entry = tk.Entry(root, font=("Arial", 12), width=40)
result_entry.pack(pady=5)

# Show/hide checkbox
show_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Show Password", variable=show_var, command=toggle_password, font=("Arial", 10), bg="#f0f4f7").pack()

# Strength label
strength_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f4f7")
strength_label.pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", font=("Arial", 12, "bold"), bg="#2196F3", fg="white", command=copy_to_clipboard).pack(pady=10)

root.mainloop()
