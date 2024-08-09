from tkinter import * # type: ignore
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def find_password():
    web = websiteBox.get()
    try:
        with open("Password Manager\\data.json","r") as passFile :
            data = json.load(passFile)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data File Found")
    else:
        if (web in data):
            user = data[web]["email"]
            passwd = data[web]["password"]
            messagebox.showinfo(title=web, message=f"Email/User: {user} \n Password: {passwd}") 
        else :
            messagebox.showinfo(title="Error", message=f"No details for {web} exists")
            

#Password Generator Project
def generate_password():
    password.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    list1 = [choice(letters) for _ in range(randint(8, 10))]
    list2 = [choice(numbers) for _ in range(randint(2, 4))]
    list3 = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = list1 + list2 + list3
    shuffle(password_list)
    generated_pass = "".join(password_list)

    password.insert(0, generated_pass)
    pyperclip.copy(generated_pass)  

# ---------------------------- SAVE PASSWORD ------------------------------- #

def addPassword():
    web = websiteBox.get()
    user = username.get()
    passwd = password.get()
    new_data = {
        web: {
            "email" : user,
            "password" : passwd,
        }
    }

    if web == "" or user == "" or passwd == "":
        messagebox.showinfo(title="ERROR", message="Please Dont Leave Feilds Empty")
        # return
    # isOk = messagebox.askokcancel(title=web, message=f"These are the details entered: \n Email: {user} \n Password : {passwd} \n Is this correct ?")
    # if isOk :
    else:
        try:
            with open("Password Manager\\data.json","r") as passFile:
                data = json.load(passFile)
        except FileNotFoundError:
            with open("Password Manager\\data.json","w") as passFile:
                json.dump(new_data, passFile, indent=4)
        else :
            data.update(new_data)
            with open("Password Manager\\data.json","w") as passFile:
                # passFile.write(f"{web} | {user} | {passwd}\n")
                json.dump(data,passFile, indent=4)
        finally:
            websiteBox.delete(0,END)
            password.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="Password Manager\\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0,column=1)

websiteLabel = Label(text="Website :")
websiteLabel.grid(row=1,column=0)
websiteBox = Entry(width=21)
websiteBox.focus()
websiteBox.grid(row=1, column=1, sticky="ew")
seachButton = Button(text="Search", command=find_password)
seachButton.grid(row=1, column=2, sticky="ew")

usernameLabel = Label(text="Email/Username :")
usernameLabel.grid(row=2,column=0)
username = Entry(width=35)
username.insert(0,"Dummy@email.com")
username.grid(row=2, column=1, columnspan=2, sticky="ew")

passwordLabel = Label(text="Password :")
passwordLabel.grid(row=3, column=0)
password = Entry(width=21)
password.grid(row=3,column=1, sticky="ew")
generatePasswordButton = Button(text="Generate Password", command=generate_password)
generatePasswordButton.grid(row=3, column=2, sticky="ew")


addButton = Button(width=36, text="Add", command=addPassword)
addButton.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()