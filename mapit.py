#! python2.7
# from video https://www.udemy.com/automate/learn/v4/t/lecture/3465864
# https://www.udemy.com/automate/learn/v4/t/lecture/3470590

import webbrowser, sys, pyperclip
sys.argv #['mapit.py', '870', 'Valencia', 'St.' ]
#check if command line argument were passed
if len(sys.argv) > 1:
    #['mapit.py', '870', 'Valencia', 'St.' ] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
#https://www.google.com/maps/place/870+Valencia+St,+San+Francisco,+CA+94110/
webbrowser.open('https://www.google.com/maps/place/'+address)
