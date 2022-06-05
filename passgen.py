from tkinter import *
import string
import random
import tkinter.font as tkFont

# Main Window Layout

root = Tk()
root.geometry("600x580")
root.title("Password generator")
root.configure(bg="#06a5b7")
root.resizable(False, False)

# Background and Icon image properties.
bg = PhotoImage(file="backgroundimage.png")
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relheight=1, relwidth=1)
photo = PhotoImage(file = "favicon.png")
root.iconphoto(False, photo)

# Font Sets

font1 = tkFont.Font(family="Calibri", size=24, weight="bold")
font2 = tkFont.Font(family="Calibri", size=20, weight="bold")
font3 = tkFont.Font(family="Calibri", size=14)
font4 = tkFont.Font(family="Calibri", size=16, weight="bold")

# Welcome Message Label

intro = Label(root, text="Hello and welcome to the Password Generator!", font=font2, bg="#06a5b7", fg="black",
              activeforeground="black", activebackground="#06a5b7")
intro.place(relx=0.5, rely=0.056, anchor='center')

# Advance Options Label

advancedopt = Label(root, text="ADVANCE OPTIONS", font=font1, bg="#06a5b7")
advancedopt.place(relx=0.5, rely=0.392, anchor='center')

# Checkbox Variables

fixLength = IntVar()
allowLowercase = IntVar()
allowUppercase = IntVar()
allowDigits = IntVar()
allowSpecialchar = IntVar()

# Checkbox Labels

Labelfixlen = Label(root, text="Enter Fix Length", font=font4, bg="#06a5b7", fg="black",
                    activeforeground="black", activebackground="#06a5b7")
Labelfixlen.place(relx=0.7, rely=0.504, anchor='center')

Labelminlen = Label(root, text="Enter min length", font=font4, bg="#06a5b7", fg="black",
                    activeforeground="black", activebackground="#06a5b7")
Labelminlen.place(relx=0.7, rely=0.660, anchor='center')

Labelmaxlen = Label(root, text="Enter Max Length", font=font4, bg="#06a5b7", fg="black",
                    activeforeground="black", activebackground="#06a5b7")
Labelmaxlen.place(relx=0.7, rely=0.8075, anchor='center')

# Password Length Entries

fixlen = Entry(root, font=font4, justify='center', disabledbackground="#060c08", disabledforeground="grey",
               background="#72bcbe")
fixlen.insert(0, "8")
fixlen.place(relx=0.7, rely=0.582, anchor='center')

minlen = Entry(root, font=font4, justify='center', disabledbackground="#060c08", disabledforeground="grey",
               background="#72bcbe")
minlen.insert(0, "6")
minlen.configure(state="disabled")
minlen.place(relx=0.7, rely=0.728, anchor='center')

maxlen = Entry(root, font=font4, justify="center", disabledbackground="#060c08", disabledforeground="grey",
               background="#72bcbe")
maxlen.insert(0, "20")
maxlen.configure(state="disabled")
maxlen.place(relx=0.7, rely=0.8736, anchor='center')


# Disables enteries in other fields when using fix length and vice versa.

def fixcheck():
    if fixLength.get() == 0:
        fixlen.configure(state="disabled")
        minlen.configure(state="normal")
        maxlen.configure(state="normal")

    else:
        fixlen.configure(state="normal")
        minlen.configure(state="disabled")
        maxlen.configure(state="disabled")


# Checkbox Information

Checklowercase = Checkbutton(root, text="Allow Lower Case",
                             variable=allowLowercase,
                             onvalue=1,
                             offvalue=0,
                             font=font4,
                             bg="#06a5b7", fg="black", activeforeground="black", activebackground="#06a5b7"
                             )
Checklowercase.select()  # Selects the checkbox as default value

Checkuppercase = Checkbutton(root, text="Allow Upper Case",
                             variable=allowUppercase,
                             onvalue=1,
                             offvalue=0,
                             font=font4,
                             bg="#06a5b7", fg="black", activeforeground="black", activebackground="#06a5b7"
                             )

Checkdigits = Checkbutton(root, text="Allow Digits",
                          variable=allowDigits,
                          onvalue=1,
                          offvalue=0,
                          font=font4,
                          bg="#06a5b7", fg="black", activeforeground="black", activebackground="#06a5b7"
                          )

Checkspecialchar = Checkbutton(root, text="Allow Symbols",
                               variable=allowSpecialchar,
                               onvalue=1,
                               offvalue=0,
                               font=font4,
                               bg="#06a5b7", fg="black", activeforeground="black", activebackground="#06a5b7"
                               )

Checkfixlength = Checkbutton(root, text="Fix Length Mode",
                             variable=fixLength,
                             onvalue=1,
                             offvalue=0,
                             command=fixcheck,
                             font=font4,
                             bg="#06a5b7", fg="black", activeforeground="black", activebackground="#06a5b7"
                             )
Checkfixlength.select()

Checkfixlength.place(relx=0.193, rely=0.504, anchor='center')
Checklowercase.place(relx=0.2, rely=0.593, anchor='center')
Checkuppercase.place(relx=0.2, rely=0.683, anchor='center')
Checkdigits.place(relx=0.16, rely=0.773, anchor='center')
Checkspecialchar.place(relx=0.18, rely=0.862, anchor='center')

# Password graphic properties

password_val = Entry(root, state="normal", font=font1, justify='center', width=25, fg="white",
                     highlightbackground="#217fdd", highlightthickness=2, readonlybackground="#060c08")
password_val.delete(0, END)
password_val.insert(0, "Click Generate!!")
password_val.configure(state="readonly")
password_val.place(relx=0.5, rely=0.168, anchor='center')


def genPassclick():  # Generates password when the button is clicked

    # Checks if entries in length fields are valid.
    # Checking start
    if fixlen.get().isdigit() == 0:
        fixlen.configure(state="normal")
        fixlen.delete(0, END)
        fixlen.insert(0, "8")
        if fixLength.get() == 0:
            fixlen.configure(state="disabled")

    if minlen.get().isdigit() == 0:
        minlen.configure(state="normal")
        minlen.delete(0, END)
        minlen.insert(0, "6")
        if fixLength.get() == 1:
            minlen.configure(state="disabled")

    if maxlen.get().isdigit() == 0:
        maxlen.configure(state="normal")
        maxlen.delete(0, END)
        maxlen.insert(0, "20")
        if fixLength.get() == 1:
            minlen.configure(state="disabled")

    if fixlen.get().isdigit() == 1 and int(fixlen.get()) < 4:
        fixlen.delete(0, END)
        fixlen.insert(0, "4")

    if int(minlen.get()) < 4:
        minlen.delete(0, END)
        minlen.insert(0, "4")

    if int(minlen.get()) > 1000:
        minlen.delete(0, END)
        minlen.insert(0, "1000")

    if int(maxlen.get()) > 1000:
        maxlen.delete(0, END)
        maxlen.insert(0, "1000")

    if int(fixlen.get()) > 1000:
        fixlen.delete(0, END)
        fixlen.insert(0, "1000")

    if int(maxlen.get()) < int(minlen.get()):
        maxlen.delete(0, END)
        maxlen.insert(0, minlen.get())
    # Checking end

    # Cases which are to be inclulded in password

    lowerCase = 26 * [allowLowercase.get()]
    upperCase = 26 * [allowUppercase.get()]
    digits = 10 * [allowDigits.get()]
    spChar = 32 * [allowSpecialchar.get()]
    ExactLength = int(fixlen.get())
    minLength = int(minlen.get())
    maxLength = int(maxlen.get())

    # Checks if atleast one case is selected

    allowed = allowLowercase.get() + allowUppercase.get() + allowDigits.get() + allowSpecialchar.get()

    if fixLength.get() != 0:        # If fixed length mode is enabled it sets both min and max to that fixed length
        minLength = ExactLength
        maxLength = ExactLength

    password = "SELECT ATLEAST 1 ARGUMENT"

    if allowed != 0:
        containsAll = 0
        while containsAll == 0:
            containsAll = 1
            password = ''.join(
                random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation,
                               weights=
                               lowerCase + upperCase + digits + spChar, k=random.randint(minLength, maxLength)))

            # Makes sure that the password contains all required cases

            if containsAll == 1 and allowLowercase.get() == 1 and any(
                    elem in password for elem in string.ascii_lowercase
            ) == 0:
                containsAll = 0

            if containsAll == 1 and allowUppercase.get() == 1 and any(
                    elem in password for elem in string.ascii_uppercase
            ) == 0:
                containsAll = 0

            if containsAll == 1 and allowDigits.get() == 1 and any(elem in password for elem in string.digits
                                                                   ) == 0:
                containsAll = 0

            if containsAll == 1 and allowSpecialchar.get() == 1 and any(elem in password for elem in string.punctuation
                                                                        ) == 0:
                containsAll = 0

    # Putting password in entry field after generating its value.

    password_val.configure(state="normal")
    password_val.delete(0, END)
    password_val.insert(0, password)
    password_val.configure(state="readonly")

# Functions to allow copying the password to clipboard.

def copy_button():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(password_val.get())
    clip.destroy()

# Buttons for password generation and copy to clipboard.

copyButton = Button(root, text="Copy", command=copy_button, font=font4, bg="#06a5b7", fg="black",
                    activeforeground="black", activebackground="#06a5b7")
copyButton.place(relx=0.91, rely=0.168, anchor='center')

genpassButton = Button(root, text="Generate Password", command=genPassclick, font=font2, bg="#06a5b7", fg="black",
                       activebackground="#06a5b7", activeforeground="black")
genpassButton.place(relx=0.5, rely=0.28, anchor='center')

root.mainloop()
