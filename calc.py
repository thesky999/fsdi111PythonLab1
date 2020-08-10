"""
Program: Simple calculator
Author: Trevor Dotzler
"""

#global vars
import os
# functions

def print_separator():
    print("=" * 35)

def print_menu():
    print("-----------------------")
    print("     Python Calc")
    print("-----------------------")

    print("[1] Sum")
    print("[2] Subtract")
    print("[3] Multiply")
    print("[4] Divide")
    print("[x] Exit")

    print_separator()

def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')
    print('\n\n\n')

# direct instructions
opc = ''


while(opc != 'x'):
    print_menu()
    opc = input("Please choose an option: ")

    if(opc == 'x'):
        break

    num1 = float(input("Provide num 1: "))
    num2 = float(input("Provide num 2: "))
    

    if(opc == '1'):
        print(num1 + num2)
    elif(opc == '2'):
        print(num1 - num2)
    elif(opc == '3'):
        print(num1 * num2)
    elif(opc == '4'):
            if(num2 == 0):
                print("Error: You can't divide by 0")
            else:
                print(num1 / num2)
    else:
        print("Please choose a valid option")

    input("Press enter to continue")
    clear()

print("Goodbye!")