from tkinter import *

root = Tk()

root.resizable(False, False)

alpha = ["[", "┤", "╕", "¿", "é", "ö", "º", "F", "ò", "?", "╞", "┌", "a", "├", "j", "ô", "╣", "▌", "┐", "R",
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
monthlabel.grid(row=0, columnspan=2)
monthinput = OptionMenu(root, monthdrop, *months)
monthinput.grid(row=1, columnspan=2)

days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31]
daydrop = IntVar()
daydrop.set(1)
daylabel = Label(root, text="Day")
daylabel.grid(row=2, columnspan=2)
dayinput = OptionMenu(root, daydrop, *days)
dayinput.grid(row=3, columnspan=2)

yearlabel = Label(root, text="Year")
yearlabel.grid(row=4, columnspan=2)
yearinput = Entry(root, width=5, borderwidth=bw)
yearinput.grid(row=5, columnspan=2)

encryptlabel = Label(root, text="Text")
encryptlabel.grid(row=6, column=0)
preencryptedtext = Text(root, width=50, borderwidth=bw)
preencryptedtext.grid(row=7, column=0)

finallabel = Label(root, text="Encrypted Text")
finallabel.grid(row=6, column=1)
encryptedtext = Text(root, width=50, borderwidth=bw)
encryptedtext.grid(row=7, column=1)
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
        encryptedtext.delete(0, "end")
        encryptedtext.insert(0, "Invalid Date")
        checkfail = 1


# Encrypt
def encryption():
    date()
    if checkfail == 0:
        messagetoencrypt = preencryptedtext.get("1.0", END)
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
        encryptedtext.delete(1.0, "end")
        encryptedtext.insert(1.0, encryptedmessage)


enbutton = Button(root, text="Encrypt", padx=width, pady=height, command=encryption, fg="white", bg="black")
enbutton.grid(row=8, column=0)


# Decrypt
def decryption():
    date()
    if checkfail == 0:
        messagetodecrypt = encryptedtext.get("1.0", END)
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
        preencryptedtext.delete(1.0, "end")
        preencryptedtext.insert(1.0, decryptedmessage)


debutton = Button(root, text="Decrypt", padx=width, pady=height, command=decryption)
debutton.grid(row=8, column=1)

root.mainloop()

quit()
