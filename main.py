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
checkfail = 0

# Entry Boxes
bw = 5

months = ["[1]January", "[2]February", "[3]March", "[4]April", "[5]May", "[6]June", "[7]July",
          "[8]August", "[9]September", "[10]October", "[11]November", "[12]December"]
monthdrop = StringVar()
monthdrop.set(months[0])
monthlabel = Label(root, text="Month")
monthlabel.grid(row=0)
monthinput = OptionMenu(root, monthdrop, *months)
monthinput.grid(row=1)

days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31]
daydrop = IntVar()
daydrop.set(1)
daylabel = Label(root, text="Day")
daylabel.grid(row=2)
dayinput = OptionMenu(root, daydrop, *days)
dayinput.grid(row=3)

yearlabel = Label(root, text="Year")
yearlabel.grid(row=4)
yearinput = Entry(root, borderwidth=bw)
yearinput.grid(row=5)

encryptlabel = Label(root, text="Text")
encryptlabel.grid(row=6)
encryptinput = Entry(root, borderwidth=bw)
encryptinput.grid(row=7)

# Buttons
width = 50
height = 10


# Date
def date():
    global shift, checkfail
    month = monthdrop.get()
    month = months.index(month) + 1
    day = daydrop.get()
    day = int(day)
    year = yearinput.get()
    year = int(year)
    if year >= 0:
        shift = month + day + year
        mathhold = shift // len(alpha)
        shift = shift - (len(alpha) * mathhold)
        checkfail = 0
    else:
        message = Label(root, text="Invalid Date")
        message.grid(column=0)
        checkfail = 1


# Encrypt
def encryption():
    date()
    if checkfail == 0:
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
        message.grid(column=0)


enbutton = Button(root, text="Encrypt", padx=width, pady=height, command=encryption, fg="white", bg="black")
enbutton.grid(row=8)


# Decrypt
def decryption():
    date()
    if checkfail == 0:
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
        message.grid(column=0)


debutton = Button(root, text="Decrypt", padx=width, pady=height, command=decryption)
debutton.grid(row=9)

root.mainloop()

quit()
