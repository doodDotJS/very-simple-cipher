import string
import random
import json

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def start():
    list_ascii_characters = list(string.ascii_letters)
    list_ascii_characters.extend(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
    
    for letter in list_ascii_characters:
        exportdict[letter] = id_generator()

    json_obj = json.dumps(exportdict, indent=4)

    file = open("key_characters.json", "w")
    file.write(json_obj)
    file.close()

if __name__ == "__main__":
    exportdict = {
        
    }
    start()