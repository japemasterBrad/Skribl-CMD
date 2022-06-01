import os

from pip import main
from note import *

clear = os.system("clear")

def load_all_notes():
    directory = os.listdir("notes")
    
    for notes in directory:
        print(notes)


def add_new_note():
    print("Adding new note")


def delete_note():
    print("Deleting note now")


def main_menu():
    print("Welcome to Skribl CMD!")
    print(f"Saved notes:\n")
    load_all_notes()
    print("\n a: Add new note || d: Delete note")
    menu = True
    user_input = input("\n> ")
    
    do:
        if user_input == "a" or user_input == "A":
            add_new_note()
            menu = False
        elif user_input == "d" or user_input == "D":
            delete_note()
            menu = False
        else:
            print("That does not compute, please try again")
            clear
            
        while(menu)
        
if __name__ == "__main__":
    main_menu()