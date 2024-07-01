# passtool
inspired by @timverbois' passtool, mine made in python, and with some other functions. made for windows 10

A simple GUI application to generate customizable passwords with various options like special characters, capital letters, custom strings, time, date, battery percentage, and Base64 encoding.

## Features

- **Password Length:** Choose a length between 6 and 22 characters.
- **Special Characters:** Option to include special characters in the password.
- **Capital Letters:** Option to include capital letters in the password.
- **Battery Percentage:** Option to include the current battery percentage in the password.
- **Current Time:** Option to include the current time in the password.
- **Current Date:** Option to include the current date in the password.
- **Custom String:** Add a custom string to the password.
- **Replace Vowels:** Option to replace vowels in the custom string with numbers (A -> 4, E -> 3, I -> 1, O -> 0).
- **Base64 Encoding:** Option to Base64 encode the final password.
- **Multiple Passwords:** Generate unlimited passwords at once.
- **Text File:** If generated passwords are +10, they get saved in 'passwords.txt' inside the root folder.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- Psutil library

## Installation

1. **Install Python 3.x**

   Make sure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Psutil**

   Use pip to install the `psutil` library:
   ```sh
   pip install psutil
   ```

## Usage

1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-username/password-generator-app.git
   cd password-generator-app
   ```

2. **Run the Application**
   ```sh
   python password_generator.py
   ```
