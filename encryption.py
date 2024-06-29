def encrypt(text,value):
    encrypted_text=""
    for char in text:
        if(char.isalpha()):
              
              if(char.islower()):
                shiftchar=ord(char)+value
                if(shiftchar>ord('z')):
                    shiftchar-=26
              else:
                shiftchar=ord(char)+value
                if(shiftchar>ord('Z')):
                    shiftchar-=26
              encrypted_text+=chr(shiftchar)    

    return encrypted_text


def decrypt(text,value):
    decrypted_text=""
    for char in text:
        if(char.isalpha()):
              
              if(char.islower()):
                shiftchar=ord(char)-value
                if(shiftchar<ord('a')):
                    shiftchar+=26
              else:
                shiftchar=ord(char)-value
                if(shiftchar<ord('A')):
                    shiftchar+=26
              decrypted_text+=chr(shiftchar)    

    return decrypted_text
                
                        
print("Encryption - 1\tDecryption - 2")
operation=int(input("Enter the value of the process reqired:"))

text=input("Enter text:")

value=int(input("Enter shift value:"))

if(operation==1):
  print(encrypt(text,value))
elif(operation==2):
  print(decrypt(text,value))
else:
    print("Invalid entry")    