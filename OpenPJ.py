#! python2.7
# from video https://www.udemy.com/automate/learn/v4/t/lecture/3465864
# from video https://www.udemy.com/automate/learn/v4/t/lecture/3470590

import webbrowser, sys, pyperclip
sys.argv #['OpenPJ.py', '543666' ]
#check if command line argument were passed
if len(sys.argv) > 1:
    #['mapit.py', '870', 'Valencia', 'St.' ] -> '870 Valencia St.'
    ID = ' '.join(sys.argv[1:])
else:
    ID = pyperclip.paste()
#http://worldserver9.amazon.com/ws/assignments_tasks?&token=1383336796&project=548699
webbrowser.open('http://worldserver9.amazon.com/ws/assignments_tasks?&token=658111049&project='+ID)
