# Import the string library. This will give us some ASCII characters.
import json
import time

# Pretty obvious what these functions do.
def letter_to_key_character(character):
    toReturn = None
    for i, v in encryption_characters.items():
        if character == i:
            toReturn = v

    return toReturn        

def key_character_to_letter(key_char):
    toReturn = None
    for i,v in encryption_characters.items():
        if key_char == v:
            toReturn = i

    return toReturn        

def encrypt(stringToEncrypt):
    stringToEncrypt = stringToEncrypt + " "
    messageToReturn = ""
    stringToEncryptAsList = list(stringToEncrypt)
    for i, value in enumerate(stringToEncryptAsList):
        if value == " ":
            messageToReturn = messageToReturn + " "
        else:
            try:
                if stringToEncryptAsList[i + 1] == " ":
                    messageToReturn = messageToReturn + letter_to_key_character(value)
                else:
                    messageToReturn = messageToReturn + letter_to_key_character(value) + "-"   
            except:
                pass        
             
            
               
    # Finally, return the encrypted message.        
    return messageToReturn      
    
# Kind of hard to explain how this function works by words.
def decrypt(stringToDecrypt):
    messageToReturn = ""
    splitMessage = stringToDecrypt.split(" ")


    for value in splitMessage:
        splitVal = value.split("-")
        wordString = ""
        for v2 in splitVal:
            letter = key_character_to_letter(v2)
            wordString = wordString + letter

        messageToReturn = messageToReturn + wordString + " "    

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
        print("What message do you want to encrypt? Only use letters and numbers.")
        stringToEncrypt = input("> ")
        # Call the encrypt function with the string to encrypt. It returns the new encrypted string.
        print("Encrypting string...")
        try:
            returnedString = encrypt(stringToEncrypt)
        except:
            print("ERROR: An error occurred when trying to encrypt. Please try again later.")
            print("Closing in 10 seconds...")
            time.sleep(10)
        # Once the encryption is done, print out the new encrypted string.
        print("Success! The encrypted string is: \n " + returnedString + "\n")
        # The user can press any key, like the space bar, to close the app.
        input("Press any key to close the app.")
    elif choice == "2":
        # If the user chose to decrypt, ask them what message to decrypt.
        print("What message do you want to decrypt?")
        stringToDecrypt = input("> ")
        # Call the decrypt function with the string to dec
        print("Decrypting string...")
        try:
            returnedString = decrypt(stringToDecrypt)
        except:
            print("ERROR: An error occurred when trying to encrypt. Please try again later.")
            print("Closing in 10 seconds...")
            time.sleep(10)
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
    # Open the file named "key_characters.json" and convert it from JSON to a Python Dictionary.
    encryption_character_file = open("key_characters.json", "r")
    encryption_characters = json.load(encryption_character_file)
    # Start the program.
    start()