#! python3
# Sethome.py - This program will record and show you an address that you set it to have.
# ...it is for use with QuickMap.
from getch import getch, pause
import shelve
import pyperclip
import selenium


def eraseaddress():
    # This function is a user option that will erase your shelf file's currently saved ['Address'] value.
    deletion_question = input("\nIf you want to delete your current home address type \"Yes\" or \"Y\". Any other text will return you to the main menu.\n")
    if deletion_question == "yes".lower() or "y".lower():
        shelf_file = shelve.open('sethome')
        shelf_file['address'] = ''
        print("\n********Your saved home address has been erased.********\n")
    else:
        pass


def checkaddress():
    '''This function is a system check that sees if we should load the shelf file's address value 
    or set a value of '' that the program considers an empty address.'''
    shelf_file = shelve.open('sethome')
    if shelf_file['address'] == ['']:
        print("\nYou currently have no home address saved.\n")
        return False
    else:
        print("You currently have a saved home address.\n")
        return True
    shelf_file.close()


def setaddress():
    # This function is a user option that will set you a new home address based on what you input. Zip/Postal code is not needed.
    shelf_file = shelve.open('sethome')
    shelf_file['address'] = input("What is your new home address?\n")
    print("\nYour new QuickMap address is " + shelf_file['address'] + "\n")
    shelf_file.close()
    pause('\nPress any key to return to menu\n')


def showaddress():
    # This function is a user option that will show you what your current home address is set to, without prompting you to set a new one.
    shelf_file = shelve.open('sethome')
    if shelf_file['address'] == '':
        print("\n********You have no QuickMap home address currently set.********\n")
    else:
        print("\n********Your QuickMap home address is " + shelf_file['address'] + "********\n")
    shelf_file.close()
    pause('\nPress any key to return to menu\n')


def main():
    shelf_file = shelve.open('sethome')

    print("""\n *-*-*-* Welcome to QuickMap!*-*-*-*

A quick way to search Google Maps directions from your home 
without ever touching the brower yourself! \n""")

    if checkaddress() == False:
        shelf_file['address'] = ''

    while True:
        choice_option = input("""- QuickMap Menu -\nEither paste an address and hit enter to map directions 
or type another command from the options below:
[Set Address]
[Show Address]
[Erase Address]
[Quit] \n\n""")
        if choice_option.lower() == 'set address':
            setaddress()
            continue
        elif choice_option.lower() == 'show address':
            showaddress()
            continue
        elif choice_option.lower() == 'erase address':
            eraseaddress()
            continue
        elif choice_option.lower() == 'quit':
            break
        else:
            print("Please select an above option or paste an address")
            continue

main()
