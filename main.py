from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    comp_password = "".join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, comp_password)
    pyperclip.copy(comp_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    password = pass_entry.get()
    email = email_entry.get()
    web_len = len(website)
    pass_len = len(password)
    data_dict = {
        website: {
            "email": email,
            "password": password
        }
    }
    if web_len == 0 or pass_len == 0:
        if web_len == 0 and pass_len == 0:
            messagebox.showinfo(title="OOPS", message=f"U left the email  and pass entry empty")
        elif web_len == 0:
            messagebox.showinfo(title="OOPS", message=f"U left the website entry empty")
        else:
            messagebox.showinfo(title="OOPS", message=f"U left the email entry empty")
    else:
        # with open("data.json", "w") as data_file:
        #     json.dump(data_dict, data_file, indent=4)
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(data_dict)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(data_dict, data_file)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        website_entry.delete(0, END)
        pass_entry.delete(0, END)
        messagebox.showinfo(title=website, message="Successfully Saved")
# -------------------------- SEARCHING SITE NAME ----------------------#


def site_search():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            for site in data:
                website = website_entry.get().lower()
                if site == website:
                    messagebox.showinfo(title=website.title(), message=f"\nemail: {data[site]['email']}"
                                                               f"\npassword: {data[site]['password']}")
                else:
                    messagebox.showerror(title=website.title(), message=f"NO  Details for  {website} found")
    except FileNotFoundError:
        messagebox.showerror(title="OOPS", message="NO DATA FOUND")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
photo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_img)
canvas.grid(row=0, column=1)
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/username:")
email_label.grid(row=2, column=0)
pass_label = Label(text="Password")
pass_label.grid(row=3, column=0)

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)
email_entry = Entry(width=39)
email_entry.insert(END, string="@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

generate_pass = Button(text="Generate password", command=pass_generator)
generate_pass.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=site_search, width=13)
search_button.grid(row=1, column=2)

window.mainloop()


