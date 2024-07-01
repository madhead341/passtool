import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import base64
from datetime import datetime
import os
import psutil

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.resizable(False, False)
        
        # Variables
        self.length_var = tk.IntVar(value=8)
        self.include_special_chars_var = tk.BooleanVar(value=False)
        self.include_capital_letters_var = tk.BooleanVar(value=False)
        self.base64_encode_var = tk.BooleanVar(value=False)
        self.custom_string_var = tk.StringVar(value="")
        self.replace_vowels_var = tk.BooleanVar(value=False)
        self.include_time_var = tk.BooleanVar(value=False)
        self.include_date_var = tk.BooleanVar(value=False)
        self.include_battery_var = tk.BooleanVar(value=False)
        self.num_passwords_var = tk.IntVar(value=1)

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Password Length (6-22):").grid(row=0, column=0, sticky=tk.W)
        ttk.Spinbox(frame, from_=6, to_=22, textvariable=self.length_var, width=5).grid(row=0, column=1, sticky=tk.W)

        ttk.Checkbutton(frame, text="Include Special Characters", variable=self.include_special_chars_var).grid(row=1, column=0, columnspan=2, sticky=tk.W)
        ttk.Checkbutton(frame, text="Include Capital Letters", variable=self.include_capital_letters_var).grid(row=2, column=0, columnspan=2, sticky=tk.W)
        ttk.Checkbutton(frame, text="Include Battery Percentage", variable=self.include_battery_var).grid(row=3, column=0, columnspan=2, sticky=tk.W)
        ttk.Checkbutton(frame, text="Include Time", variable=self.include_time_var).grid(row=4, column=0, columnspan=2, sticky=tk.W)
        ttk.Checkbutton(frame, text="Include Date", variable=self.include_date_var).grid(row=5, column=0, columnspan=2, sticky=tk.W)

        ttk.Label(frame, text="Include Custom String:").grid(row=6, column=0, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.custom_string_var, width=20).grid(row=6, column=1, sticky=tk.W)
        ttk.Checkbutton(frame, text="Replace Vowels in Custom String", variable=self.replace_vowels_var).grid(row=7, column=0, columnspan=2, sticky=tk.W)

        ttk.Checkbutton(frame, text="Base64 Encode Final Password", variable=self.base64_encode_var).grid(row=8, column=0, columnspan=2, sticky=tk.W)

        ttk.Label(frame, text="Number of Passwords:").grid(row=9, column=0, sticky=tk.W)
        ttk.Spinbox(frame, from_=1, to_=100, textvariable=self.num_passwords_var, width=5).grid(row=9, column=1, sticky=tk.W)

        ttk.Button(frame, text="Generate Password", command=self.generate_password).grid(row=10, column=0, columnspan=2, pady=10)

        self.password_text = tk.Text(frame, height=10, width=40, state='disabled')
        self.password_text.grid(row=11, column=0, columnspan=2, sticky=(tk.W, tk.E))

    def get_battery_percentage(self):
        battery = psutil.sensors_battery()
        if battery:
            return f"{battery.percent}%"
        else:
            return ""

    def generate_password(self):
        length = self.length_var.get()
        custom_string = self.custom_string_var.get()
        replace_vowels = self.replace_vowels_var.get()
        include_special_chars = self.include_special_chars_var.get()
        include_capital_letters = self.include_capital_letters_var.get()
        base64_encode = self.base64_encode_var.get()
        include_time = self.include_time_var.get()
        include_date = self.include_date_var.get()
        include_battery = self.include_battery_var.get()
        num_passwords = self.num_passwords_var.get()

        if replace_vowels:
            custom_string = custom_string.replace('A', '4').replace('E', '3').replace('I', '1').replace('O', '0').replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0')

        if len(custom_string) > length:
            messagebox.showerror("Error", "Custom string is too long!")
            return

        characters = string.ascii_lowercase + string.digits
        if include_special_chars:
            characters += string.punctuation
        if include_capital_letters:
            characters += string.ascii_uppercase

        def create_single_password():
            nonlocal length, custom_string, include_time, include_date, include_battery

            password_length = length - len(custom_string)
            password = ''.join(random.choice(characters) for i in range(password_length))

            if include_time:
                time_str = datetime.now().strftime("%H%M%S")
                time_length = min(len(time_str), password_length)
                password = password[:password_length - time_length] + time_str[:time_length]

            if include_date:
                date_str = datetime.now().strftime("%Y%m%d")
                date_length = min(len(date_str), password_length)
                password = password[:password_length - date_length] + date_str[:date_length]

            if include_battery:
                battery_percentage = self.get_battery_percentage().replace("%", "")
                battery_length = min(len(battery_percentage), password_length)
                password = password[:password_length - battery_length] + battery_percentage[:battery_length]

            final_password = custom_string + password

            if base64_encode:
                final_password = base64.b64encode(final_password.encode()).decode()

            return final_password

        passwords = [create_single_password() for _ in range(num_passwords)]

        if num_passwords > 10:
            file_path = os.path.join(os.path.dirname(__file__), 'passwords.txt')
            with open(file_path, 'w') as file:
                for pw in passwords:
                    file.write(pw + '\n')
            messagebox.showinfo("Info", f"Passwords saved to {file_path}")
        else:
            self.password_text.config(state='normal')
            self.password_text.delete(1.0, tk.END)
            for pw in passwords:
                self.password_text.insert(tk.END, pw + '\n')
            self.password_text.config(state='disabled')

        # Resize the text widget based on the number of lines
        num_lines = min(len(passwords), 10)  # Limit to 10 lines initially
        self.password_text.config(height=num_lines + 1)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
