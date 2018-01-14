#!python3 

import webbrowser, sys, pyperclip

if len(sys.arg)  > 1: 
    address = ' '.join(sys.argv[1:])
else:
    addrress = pyperclip.paste()
