#prerequest is open WS with Project View "projects for clients I am a member of"
import requests
import os
import re
from bs4 import BeautifulSoup
homeurl="http://worldserver9.amazon.com/ws/"
url= "http://worldserver9.amazon.com/ws/assignments_projects?&token=1575042518"
r = requests.get(url)
soup= BeautifulSoup(r.content,"html.parser")


g_data=soup.find_all("tr")
for tr in g_data:
    for td in tr.contents:
        try:
            print td.text
        except:
            pass
    #text_file.write( "["+ homeurl + "%s\t%s]<br>\n" %(trow.get("href"), trow.text))


