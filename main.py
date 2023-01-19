alpha = ["[", "┤", "╕", "¿", "é", "ö", "₧", "º", "F", "ò", "?", "[", "╞", "┌", "a", "├", "j", "ô", "╣", "▌", "┐", "R",
         "(", "3", "╧", "Ö", "ú", "Æ", "P", "α", "7", "X", "<", "{", "S", "/", "x", "╡", "I", "ñ", "┬", "!", "╙", "Ü",
         "O", "┘", "í", "o", "A", ",", "¡", "ì", "½", "n", "0", "\'", "╗", "Å", "%", "╩", "E", "┴", "¬", "═", "╖", "9",
         "É", "+", "█", "ê", "æ", "╪", "╥", "Y", "w", "m", ";", ".", "▒", "¢", "@", "¼", "╫", "f", "▄", "h", "─", "░",
         "C", "p", "║", "*", "¥", "=", "»", "i", "|", "#", "&", "~", "â", "1", "└", "y", "u", "s", "û", "╓", "q", "Q",
         "Z", "å", "B", "▀", "-", "N", "e", "╛", "ä", "╝", "V", "d", "╦", "╟", "╔", ")", "ë", "r", "╤", "╬", "_", "W",
         "╒", "á", "ç", "z", "╠", "D", "Ñ", "M", "t", "5", "î", "╜", "Ç", "Ä", "│", "╚", "H", "▓", "]", "«", "ÿ", "ù",
         "ü", "┼", "8", "G", "4", "c", "\"", "}", "ª", "k", "U", "g", "à", "⌐", "\\", "$", "`", ">", "£", "╨", "2", "K",
         "l", "T", "6", "ï", "L", "è", "╢", "ó", "ƒ", "v", ":", "b", "^", "J", "]", " "]


def encryption():
    print("\n->Enter your message")
    messagetoencrypt = input()
    encryptedmessage = "\n"
    for x in messagetoencrypt:
        if x in alpha:
            charhold = alpha.index(x) + shift
            if charhold >= len(alpha):
                charhold -= len(alpha)
            charhold = alpha[charhold]
            encryptedmessage += charhold
        else:
            encryptedmessage += x
    print(encryptedmessage)


def decryption():
    print("\n->What is the message?")
    messagetodecrypt = input()
    decryptedmessage = "\n"
    for x in messagetodecrypt:
        if x in alpha:
            charhold = alpha.index(x) - shift
            if charhold < 0:
                charhold = charhold + len(alpha)
            charhold = alpha[charhold]
            decryptedmessage += charhold
        else:
            decryptedmessage += x
    print(decryptedmessage)


def options():
    global option
    print("Encrypt (e)\n>Decrypt (d)\n>Exit (x)")
    option = input()
    option = option.upper()


cnt = 0

while cnt == 0:
    print("day")
    day = input()
    day = int(day)
    if day in range(0, 32):
        cnt = 1
    else:
        print("Invalid Date")

cnt = 0

while cnt == 0:
    print("month")
    month = input()
    month = int(month)
    if month in range(0, 13):
        cnt = 1
    else:
        print("Invalid Date")

cnt = 0

while cnt == 0:
    print("Year")
    year = input()
    year = int(year)
    if year >= 0:
        cnt = 1
    else:
        print("Invalid Date")

shift = month + day + year
mathhold = shift // len(alpha)
shift = shift - (len(alpha) * mathhold)

option = ""
options()

while option == "E" or "D":
    if option == "E":
        encryption()
        options()
    elif option == "D":
        decryption()
        options()
    else:
        break
print("\n->Have a good day")
