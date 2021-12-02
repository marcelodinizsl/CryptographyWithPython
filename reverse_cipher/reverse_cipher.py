def __reverse_cipher(message):
    translated = ''
    counter = len(message) - 1
    while counter >= 0:
        translated += message[counter]
        counter -= 1

    print("The cipher text is: {}".format(translated))

def main():
    message = input("Informe the message: ")
    __reverse_cipher(message)

if __name__=='__main__':
    main()