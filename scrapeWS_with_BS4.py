#prerequest is open WS with Project View "projects for clients I am a member of"
import requests
import os
import re
from bs4 import BeautifulSoup
homeurl="http://worldserver9.amazon.com/ws/"
url= "http://worldserver9.amazon.com/ws/assignments_projects?&token=1575042518"
r = requests.get(url)
soup= BeautifulSoup(r.content,"html.parser")

#creat a txt file that the links will be dumped to
text_file=open("dumpLinks4wiki.txt","w")
text_file.write("\n")


g_data=soup.find_all(href=re.compile("assignments_tasks"))
for trow in g_data:
    text_file.write( "["+ homeurl + "%s\t%s]<br>\n" %(trow.get("href"), trow.text))

text_file.close()

