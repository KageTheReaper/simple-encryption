def encrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key

    file = open("C647-" + filename,"wb")
    file.write(data)
    file.close()


key = int(input("Choose your private key (from 1 to 255):\n"))
filename = input("Please enter the name of the file you want to encrypt (make sure you copy it to this folder)\n")
print("ENCRYPTING...")
encrypt(filename, key)
