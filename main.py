import time


alpha = ["A", "1", "B", "2", "C", "3", "D", "4", "E", "5", "F", "6", "G", "7", "H", "8", "I", "9", "J", "0", "K", "!",
         "L", "@", "M", "#", "N", "$", "O", "%", "P", "^", "Q", "&", "R", "*", "S", "(", "T", ")", "U", "_", "V", "+",
         "W", "-", "X", "=", "Y", "`", "Z", "~", "z", "[", "y", "]", "x", "\\", "w", ";", "v", "’", "u", ".", "t", "/",
         "s", "{", "r", "}", "q", "|", "p", ":", "o", "”", "n", ">", "m", "<", "l", "﷽", "k", "?", "j", "䯂", "i", "麤",
         "h", "鸞", "g", "驫", "f", "鬱", "e", "魘", "d", "鷹", "c", "靨", "b", "鑑", "a", "龕", ",", "'", "\""]


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
    time.sleep(1.5)
    print("\n->What would you like to do?\n>Encrypt (e)\n>Decrypt (d)\n>Exit (x)")
    option = input()
    option = option.upper()


print("->Hello!\n->Press Enter To Continue")
input()
print("->What day is/was it?")
day = input()
print("\n->What month is/was it?")
month = input()
print("\n->What year is/was it?")
year = input()

shift = month + day + year
shift = int(shift)
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
