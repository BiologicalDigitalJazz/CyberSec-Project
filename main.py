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

# Entry Boxes
bw = 5

encryptlabel = Label(root, text="Text")
encryptlabel.grid(row=3, column=0)
encryptinput = Entry(root, borderwidth=bw)
encryptinput.grid(row=3, column=1)

monthlabel = Label(root, text="Month")
monthlabel.grid(row=0, column=0)
monthinput = Entry(root, borderwidth=bw)
monthinput.grid(row=0, column=1)

daylabel = Label(root, text="Day")
daylabel.grid(row=1, column=0)
dayinput = Entry(root, borderwidth=bw)
dayinput.grid(row=1, column=1)

yearlabel = Label(root, text="Year")
yearlabel.grid(row=2, column=0)
yearinput = Entry(root, borderwidth=bw)
yearinput.grid(row=2, column=1)

# Buttons
width = 50
height = 10


# Date
def date():
    global shift
    month = monthinput.get()
    month = int(month)
    day = dayinput.get()
    day = int(day)
    year = yearinput.get()
    year = int(year)
    shift = month + day + year
    mathhold = shift // len(alpha)
    shift = shift - (len(alpha) * mathhold)


# Encrypt
def encryption():
    date()
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
    message.grid(column=0, columnspan=2)


enbutton = Button(root, text="Encrypt", padx=width, pady=height, command=encryption, fg="white", bg="black")
enbutton.grid(row=4, column=0)


# Decrypt
def decryption():
    date()
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


debutton = Button(root, text="Decrypt", padx=width, pady=height, command=decryption)
debutton.grid(row=4, column=1)

root.mainloop()

quit()
