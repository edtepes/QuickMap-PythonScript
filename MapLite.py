#! /usr/bin/env python3
""" MapLite.py - Using the set address from QuickMap this script will auto generate 
Google Maps from whatever address is in your clipboard."""

import shelve  # <-- Used to store an address for re-use after you close and reopen the program
import pyperclip  # <-- Used store pasted text
import webbrowser  # <-- Used to pull up directions in your default web browser

shelf_file = shelve.open('sethome')
webbrowser.open('https://www.google.ca/maps/dir/' + shelf_file['address'] + "/" + pyperclip.paste())
