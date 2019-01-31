# Caesar Cipher with User Input
# Developed by ricoen
# Thanks to http://inventwithpython.com/hacking (BSD Licensed) for original source code

chiper = True
while chiper:
    message = input ("Enter your secret message: ")
    key = input ("Enter the key you want to use: ")
    mode = input ("Encrypt or Decrypt? (e for encrypt - d for decrypt) ")

    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    translated = ''

    message = message.upper()

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode == 'e':
                num = num + int(key)
            elif mode == 'd':
                num = num - int(key)
            else:
                break

            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)

            translated = translated + LETTERS[num]

        else:
            translated = translated + symbol
    print(translated)

    again = input("Encrypt again? (Y/n)\n")
    if again == "y":
        continue
    elif again == "Y":
        continue
    elif again == "n":
        break
    else:
        break
