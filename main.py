from tkinter import *

root = Tk()

alpha = ["[", "┤", "╕", "¿", "é", "ö", "₧", "º", "F", "ò", "?", "[", "╞", "┌", "a", "├", "j", "ô", "╣", "▌", "┐", "R",
         "(", "3", "╧", "Ö", "ú", "Æ", "P", "α", "7", "X", "<", "{", "S", "/", "x", "╡", "I", "ñ", "┬", "!", "╙", "Ü",
         "O", "┘", "í", "o", "A", ",", "¡", "ì", "½", "n", "0", "ß", "\'", "╗", "Å", "%", "╩", "E", "┴", "¬", "═", "╖",
         "9", "É", "+", "█", "ê", "æ", "╪", "╥", "Y", "w", "m", ";", ".", "▒", "¢", "@", "¼", "╫", "f", "▄", "h",
         "─", "░", "C", "p", "║", "*", "¥", "=", "»", "i", "|", "#", "&", "~", "â", "1", "└", "y", "u", "s", "û",
         "╓", "q", "Q", "Z", "å", "B", "▀", "-", "ẞ", "N", "e", "╛", "ä", "╝", "V", "d", "╦", "╟", "╔", ")", "ë",
         "r", "╤", "╬", "_", "W", "╒", "á", "ç", "z", "╠", "D", "Ñ", "M", "t", "5", "î", "╜", "Ç", "Ä", "│", "╚", "H",
         "▓", "]", "«", "ÿ", "ù", "ü", "┼", "8", "G", "4", "c", "\"", "}", "ª", "k", "U", "g", "à", "⌐", "\\", "$", "`",
         ">", "£", "╨", "2",
         "K", "l", "T", "6", "ï", "L", "è", "╢", "ó", "ƒ", "v", ":", "b", "^", "J", "]", " "]

shift = 0

# Text Box
encryptinput = Entry(root, borderwidth=5)
encryptinput.grid(row=0, column=2)


# Date
def date():
    global shift
    cnt = 0
    month = 0
    day = 0
    year = 0
    while cnt == 0:
        print("\nMonth:")
        month = input()
        month = int(month)
        if month in range(0, 13):
            cnt = 1
        else:
            print("Invalid Date")
    cnt = 0
    while cnt == 0:
        print("\nDay:")
        day = input()
        day = int(day)
        if day in range(0, 32):
            cnt = 1
        else:
            print("Invalid Date")
    cnt = 0
    while cnt == 0:
        print("\nYear:")
        year = input()
        year = int(year)
        if year >= 0:
            cnt = 1
        else:
            print("Invalid Date")
    shift = month + day + year
    mathhold = shift // len(alpha)
    shift = shift - (len(alpha) * mathhold)


datebutton = Button(root, text="Set Date", padx=50, pady=25, command=date, fg="white", bg="black")
datebutton.grid(row=1, column=1)


# Encrypt
def encryption():
    messagetoencrypt = encryptinput.get()
    encryptedmessage = ""
    for x in messagetoencrypt:
        if x in alpha:
            charhold = alpha.index(x) + shift
            if charhold >= len(alpha):
                charhold -= len(alpha)
            charhold = alpha[charhold]
            encryptedmessage += charhold
        else:
            encryptedmessage += x
    message = Label(root, text=encryptedmessage)
    message.grid(column=2)


enbutton = Button(root, text="Encrypt", padx=50, pady=25, command=encryption)
enbutton.grid(row=1, column=2)


# Decrypt
def decryption():
    messagetodecrypt = encryptinput.get()
    decryptedmessage = ""
    for x in messagetodecrypt:
        if x in alpha:
            charhold = alpha.index(x) - shift
            if charhold < 0:
                charhold = charhold + len(alpha)
            charhold = alpha[charhold]
            decryptedmessage += charhold
        else:
            decryptedmessage += x
    message = Label(root, text=decryptedmessage)
    message.grid(column=2)


debutton = Button(root, text="Decrypt", padx=50, pady=25, command=decryption)
debutton.grid(row=1, column=3)

root.mainloop()

quit()
