import os
from art import logo
from engine import encrypt, decrypt, alphabet

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

machine_running = True
while machine_running:
    
    print(logo)

    direction = input("Type 'encode' to encrypt, 'decode' to decrypt, 'exit' to exit the programme:\n").lower()

    if direction == "encode":
        text = input("Type your message: \n").lower()
        shift = int(input("Type the shift number: \n"))
        encrypt(message=text, shiftamt=shift)

    elif direction == "decode":
        text = input("Type your message: \n").lower()
        shift = int(input("Type the shift number: \n"))        
        decrypt(message=text, shiftamt=shift)

    elif direction == "exit":
        machine_running = False

    else:
        print("Please enter a valid direction")

    
    if input("press enter to keep using the machine, type 'exit' to stop using: \n") == "exit":
        machine_running = False
    else:
        cls()



print("Thank you for using the Caesar Cipher Machine")
