def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        #Encrypt uppercase characters in plain text
        if(char.isupper()):
            result += chr((ord(char)+s-65)%26 +65)
            #ord() method returns the unicode of a specific character.
            #char() method returns the string of a specific unicode integer.
        else:
            result += chr((ord(char)+s-97)%26 + 97)
    return result
#check the above function 
text ="HELLO FROM THE TOP OF THE WORLD"
s = 4
cipher=encrypt(text, s)
print(f"Plain-text: {text}")
print(f"Shift-pattern:{s}")
print(f"Cipher-text:",cipher);

#decryption 
def decrypt(result, s):
    plain = ""
    for i in range(len(result)):
        char = result[i]
        if(char.isupper()):
            plain +=chr((ord(char)-s-65)%26+65)
        else:
            plain +=chr((ord(char)-s-97)%26+97)
    return plain
print(f"plain-text-after-decryption:",decrypt(cipher, s))