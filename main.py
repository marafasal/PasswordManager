from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import  json


window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
canvass=Canvas(width=200,height=200)
photo=PhotoImage(file="logo.png")
def finder():
    web = entry_web.get()
    try:
        with open("content.json","r") as df:
            pd=json.load(df)

    except FileNotFoundError:
        messagebox.showinfo(title="alert",message="No details for the website exists")
    else:
        for k, v in pd.items():
            if web == k:
                messagebox.showinfo(title="alert",
                                    message=f"The email is {v['email']} and the password is {v['password']}")
            else:
                messagebox.showinfo(title="alert",message=f"{web} does not exist")




def generator():
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
                "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
                "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Z"]
    symbols = ["@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "=", "/", ":"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    alpha = random.randint(8, 10)
    sym = random.randint(2, 4)
    num = random.randint(2, 4)
    passwordlist3 = [random.choice(alphabet) for char in range(alpha)]
    passwordlist1 = [random.choice(symbols) for char1 in range(sym)]
    passwordlist2 = [random.choice(numbers) for char2 in range(num)]
    passwordlist = passwordlist1 + passwordlist2 + passwordlist3
    random.shuffle(passwordlist)
    password = "".join(passwordlist)
    entry_password.insert(0,password)
    pyperclip.copy(password)



def clickme():
    global count
    web=entry_web.get()
    password=entry_password.get()
    user=entry_user.get()
    new_data={web:
                  {"email":user,"password":password}
              }
    if len(web)==0 or len(password)==0:
        messagebox.showinfo(title="alert",message=f"please make sure email or password are not left empty ")

    else:
        try:
            with open("content.json","r") as f:
                data2=json.load(f)
        except FileNotFoundError:
            with open("content.json","w") as f:
                json.dump(new_data,f,indent=4)
        else:
            data2.update(new_data)

            with open("content.json","w") as f:
                json.dump(data2,f,indent=4)
        finally:
            entry_web.delete(0,END)
            entry_password.delete(0,END)
canvass.create_image(100,100,image=photo)
canvass.grid(row=0,column=1)


label1=Label(text="Website")
label1.grid(row=1,column=0)
label2=Label(text="Email/Username")
label2.grid(row=2,column=0)
label3=Label(text="Password")
label3.grid(row=3,column=0)

entry_web=Entry(width=21)
entry_web.grid(row=1,column=1)
entry_web.focus()

entry_user=Entry(width=39)
entry_user.grid(row=2,column=1,columnspan=2)
entry_user.insert(0,"marafasalman@gmail.com")
entry_password=Entry(width=21)
entry_password.grid(row=3,column=1)

find=Button(text="Search",command=finder)
find.grid(row=1,column=2)
generate=Button(text="Generate Password",command=generator)
generate.grid(row=3,column=2)
add=Button(text="add",width=34,command=clickme)
add.grid(row=4,column=1,columnspan=2)


window.mainloop()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #