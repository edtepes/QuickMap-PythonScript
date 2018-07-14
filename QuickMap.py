#! /usr/bin/env python3
""" QuickMap.py - Fast mapping straight from your OS to automate the Google Maps searching. 

Menu Options:

Paste (Ctrl+V or Cmd+V) + Enter - finds your default browser and prefills Google Maps to
get directions from your saved address to your pasted address.

Set Address - sets a new address, overwriting the old address.

Show Address - shows you the currently saved address. 

Erase Address - erases your old address and sets the current address to ''. This may 
seem redundant as Set Address overwrites files anyways, however on startup the program lets
you know if you have a currently saved address or not and the only way it will say you 
currently have no saved address is if your address is set to ''. """

from getch import getch, pause  # <-- Used to pause for the next keypress in between menu options
import shelve  # <-- Used to store an address for re-use after you close and reopen the program
import pyperclip  # <-- Used store pasted text
import webbrowser  # <-- Used to pull up directions in your default web browser

# TODO: Make this program cross-platform.

# TODO: Make this program runnable from Windows' Run Dialog and OSX's Spotlight Search


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
    if shelf_file['address'] == '':
        print("\nYou currently have no home address saved.\n")
        return False
    else:
        print("You currently have a saved home address.\n")
        return True


def setaddress():
    # This function is a user option that will set you a new home address based on what you input. Zip/Postal code is not needed.
    shelf_file = shelve.open('sethome')
    shelf_file['address'] = input("What is your new home address?\n")
    print("\nYour new QuickMap address is " + shelf_file['address'] + "\n")
    pause('\nPress any key to return to menu\n')


def showaddress():
    # This function is a user option that will show you what your current home address is set to, without prompting you to set a new one.
    shelf_file = shelve.open('sethome')
    if shelf_file['address'] == '':
        print("\n********You have no QuickMap home address currently set.********\n")
    else:
        print("\n********Your QuickMap home address is " + shelf_file['address'] + "********\n")
    pause('\nPress any key to return to menu\n')


def main():
    # Start of QuickMap's procedural execution
    shelf_file = shelve.open('sethome')

    print(shelf_file['address'])

    print("""\n *-*-*-* Welcome to QuickMap!*-*-*-*

A quick way to search Google Maps directions from your home 
without ever touching the browser yourself. \n""")

    if checkaddress() == False:
        shelf_file['address'] = ''

    shelf_file.close()
    while True:
        choice_option = input("""- QuickMap Menu -\nEither paste an address and hit enter to map directions 
or type another command from the options below:
[Set Address]
[Show Address]
[Erase Address]
[Quit]

[Or Just Press Enter to Paste An Address From Clipboard] \n\n""")
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
            shelf_file = shelve.open('sethome')
            webbrowser.open('https://www.google.ca/maps/dir/' + shelf_file['address'] + "/" + pyperclip.paste())
            shelf_file.close()
            break


main()
