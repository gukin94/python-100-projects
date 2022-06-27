from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    # print(f"Your password is: {password}")
    if pw_entry.get() != "":
        pw_entry.delete(0, "end")
    pw_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    # get data from entries
    web_info = {
        "url": web_entry.get(),
        "email": email_entry.get(),
        "password": pw_entry.get()
    }
    for value in web_info.values():
        if value == "":
            messagebox.showwarning(title="Oops!", message="Please don't leave any fields empty!")
            return

    is_ok = messagebox.askokcancel(title=web_info["url"], message=f"These are the datails entered: "
                                                                  f"\nEmail: {web_info['email']}"
                                                                  f"\nPassword: {web_info['password']}"
                                                                  f"\nIs it ok to save?")

    if is_ok:
        # upon hitting enter "add" button, save the data as .txt file
        with open("password_list.txt", mode='a') as file:
            info = f"{web_info['url']} | {web_info['email']} | {web_info['password']}\n"
            file.write(info)

        # and removing the populated data
        web_entry.delete(0, "end")
        email_entry.delete(0, "end")
        pw_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=100)

canvas = Canvas(width= 200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img) # position of the image center
canvas.grid(column=1, row=0)

# labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

pw_label = Label(text="Password:")
pw_label.grid(column=0, row=3)

# entries
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "gukin94@gmail.com")

pw_entry = Entry(width=21)
pw_entry.grid(column=1, row=3)

# buttons
pw_button = Button(text="Generate Password", command=generate_password)
pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=5, columnspan=2)


window.mainloop()