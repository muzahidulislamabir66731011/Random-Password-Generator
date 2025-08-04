# Random-Password-Generator
A simple, privacy-focused password generator written in Python.

## 🔐 What It Does

- Generates strong, random passwords of custom length.
- Supports uppercase, lowercase, digits, and punctuation.
- Lets users optionally save passwords to a `.txt` file.
- Fully offline: no internet, cookies, or data tracking.
- Future-ready: planned GUI for PC and Android versions.

## 🛡️ Privacy First

This tool **does not**:
- Store passwords permanently without user permission.
- Use cookies, cache, or tracking.
- Connect to the internet or any server.
- Use secret storage or password managers.

Passwords are generated **locally** and saved only if you choose to.

---

## ✅ Features

- Choose password length.
- Includes all printable character types.
- Optionally save to a custom-named `.txt` file.
- Input validation for clean UX.
- Easy to extend for GUI use (e.g., Tkinter, Kivy, PyQt).

---

## 💻 Example Output

How many characters do you need (or 'q' to quit): 16
Your password is: ^WmKz2G@q9*rV!X#

Do you want to save the password as text file? (Yes/No): yes
What is this password for? (e.g., Facebook, Gmail): Github
Password saved to Github.txt

## 🚀 Future Plans

- Graphical User Interface (GUI)
- Android & PC versions (using Kivy or Electron)
- "Copy to Clipboard" option
- Auto-delete saved files after a timer
- Option to use `secrets` module for cryptographic security
