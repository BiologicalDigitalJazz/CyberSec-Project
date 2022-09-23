import time


alpha = ["A", "1", "B", "2", "C", "3", "D", "4", "E", "5", "F", "6", "G", "7", "H", "8", "I", "9", "J", "0", "K", "!",
         "L", "@", "M", "#", "N", "$", "O", "%", "P", "^", "Q", "&", "R", "*", "S", "(", "T", ")", "U", "_", "V", "+",
         "W", "-", "X", "=", "Y", "`", "Z", "~", "z", "[", "y", "]", "x", "\\", "w", ";", "v", "’", "u", ".", "t", "/",
         "s", "{", "r", "}", "q", "|", "p", ":", "o", "”", "n", ">", "m", "<", "l", "﷽", "k", "?", "j", "䯂", "i", "麤",
         "h", "鸞", "g", "驫", "f", "鬱", "e", "魘", "d", "鷹", "c", "靨", "b", "鑑", "a", "龕", ",", "'", "\""]


def encryption():
    print("->Enter your message")
    messagetoencrypt = input()
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
    print(encryptedmessage)


def decryption():
    print("->What is the message?")
    messagetodecrypt = input()
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
    print(decryptedmessage)


print("->Hello!\n->Press Enter To Continue")
input()
print("->What day is/was it?")
day = input()
print("->What month is/was it?")
month = input()
print("->What year is/was it?")
year = input()
shift = month + day + year
shift = int(shift)
mathhold = shift // len(alpha)
shift = shift - (len(alpha) * mathhold)
print("->What would you like to do?\n>Encrypt(en)\n>Decrypt(de)\n>Exit(any key)")
option = input().upper()


while option == "EN" or "DE":
    if option == "EN":
        encryption()
    if option == "DE":
        decryption()
    time.sleep(1)
    print("->What would you like to do?\n>Encrypt(en)\n>Decrypt(de)\n>Exit(any key)")
    option = input().upper()
    if option != "EN" or "DE":
        break
print("->Have a good day")
