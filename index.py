# Import the string library. This will give us some ASCII characters.
import string


def encrypt(stringToEncrypt):
    # Set up the variable that will be returned.
    messageToReturn = ""
    # Loop through the string to encrypt.
    for index in range(len(stringToEncrypt)):
        value = stringToEncrypt[index]
        # If the value is a space, leave a space in messageToReturn
        # Otherwise, get the index of the letter from stringToEncrypt in list_ascii_characters, then add the amount set in encryption_incrementer
        if value == " ":
            messageToReturn = messageToReturn + " "
        else:
            #print(list_ascii_characters[index + encryption_incrementer])
            messageToReturn = messageToReturn + list_ascii_characters[list_ascii_characters.index(value) + encryption_incrementer]

    # Finally, return the encrypted message.        
    return messageToReturn      
    

def decrypt(stringToDecrypt):
    # This is basically the same thing as the encrypt function, but you take away the number set in encryption_incrementer, rather than adding it.
    messageToReturn = ""
    for index in range(len(stringToDecrypt)):
        value = stringToDecrypt[index]
        if value == " ":
            messageToReturn = messageToReturn + " "
        else:
            #print(list_ascii_characters[index + encryption_incrementer])
            messageToReturn = messageToReturn + list_ascii_characters[list_ascii_characters.index(value) - encryption_incrementer]

    return messageToReturn       

def start():
    # Print out the options that can be used.
    print("""
A very simple cipher script
===================================
Select from one of the following options:

1. Encrypt
2. Decrypt
3. Exit
    """)
    # Prompt the user to choose.
    choice = input("> ")
    if choice == "1":
        # If the user chose to encrypt, ask them what message to encrypt.
        print("What message do you want to encrypt?")
        stringToEncrypt = input("> ")
        # Call the encrypt function with the string to encrypt. It returns the new encrypted string.
        returnedString = encrypt(stringToEncrypt)
        print("Encrypting string...")
        # Once the encryption is done, print out the new encrypted string.
        print("Success! The encrypted string is: \n " + returnedString + "\n")
        # The user can press any key, like the space bar, to close the app.
        input("Press any key to close the app.")
    elif choice == "2":
        # If the user chose to decrypt, ask them what message to decrypt.
        print("What message do you want to decrypt?")
        stringToDecrypt = input("> ")
        # Call the decrypt function with the string to dec
        returnedString = decrypt(stringToDecrypt)
        print("Decrypting string...")
        # Once the decryption is done, print out the decrypted string.
        print("Success! The message was: \n " + returnedString + "\n")
        # The user can press any key, like the space bar, to close the app
        input("Press any key to close the app.")
    elif choice == "3":
        # The user can press any key, like the space bar, to close the app
        input("Press any key to close the app.")
    else:
        print("Invalid option.")   
        input("Press any key to exit the application. You may relaunch it if you want to try again.")
        exit()

# Check if this script is the entry point.        
if __name__ == "__main__":
    # Get the ASCII characters and put them in a list. Include numbers as well.
    list_ascii_characters = list(string.ascii_letters)
    list_ascii_characters.extend(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
    print(list_ascii_characters)
    # This is kinda hard to explain with words. Basically, this is the variable used to get the letter after this number. Feel free to change.
    encryption_incrementer = 2
    # Start the program.
    start()