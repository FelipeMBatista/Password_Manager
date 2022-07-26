import tkinter as t
from tkinter import messagebox
import pyperclip
import password_gen
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password():
    new_password = password_gen.PasswordGenerator()
    password_entry.insert(0, new_password.random_password_generator())
    pyperclip.copy(new_password.random_password_generator())

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    login = user_entry.get()
    password = password_entry.get()
    new_data = {
        website.title(): {
            "login": login,
            "password": password
        }
    }
    if len(website) and len(login) and len(password) != 0:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        except json.decoder.JSONDecodeError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")
    else:
        messagebox.showinfo(title="Oops", message="Please, don't leave any fields empty!")

# ---------------------------- SEARCH ------------------------------- #
def find_password():
    website = website_entry.get().title()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Login: {data[website]['login']}\n"
                                                   f"Password: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
    finally:
        website_entry.delete(0, "end")
        password_entry.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #

# Create the window.
window = t.Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

# Creating the Canvas.
main_image = t.PhotoImage(file="logo.png")
canvas = t.Canvas(height=200, width=200)
canvas.create_image(100, 100, image=main_image)
canvas.grid(column=1, row=0)

# Creating the Entry.
website_entry = t.Entry(width=34)
website_entry.grid(column=1, row=1, pady=4)
website_entry.focus()
user_entry = t.Entry(width=53)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "my_email@...")
password_entry = t.Entry(width=34)
password_entry.grid(column=1, row=3)

# Creating Buttons.
search_button = t.Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1, pady=2)
password_button = t.Button(text="Generate password",width=14, command=generate_random_password)
password_button.grid(column=2, row=3, pady=2)
add_button = t.Button(text="Add", width=44, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

# Creating Labels.
website_label = t.Label(text="Website:")
website_label.grid(column=0, row=1)
user_label = t.Label(text="Email / Username:")
user_label.grid(column=0, row=2)
password_label = t.Label(text="Password:")
password_label.grid(column=0, row=3)

window.mainloop()