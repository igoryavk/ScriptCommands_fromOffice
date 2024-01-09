from bs4 import *
from bs4 import Tag
import click
from time import sleep

#open('new','w+')
# print("Script is started")
with open("C:\\Users\\i.yavkin\\Documents\\MyPouRepository\\testing-artifacts\\mypou2.xml",encoding="utf-8") as file:
   src1=file.read()
with open("C:\\Users\\i.yavkin\\Documents\\MyPouRepository\\mypou.xml",encoding="utf-8") as file:
   src2=file.read()
soup1=BeautifulSoup(src1,"lxml")
print("first_____________________________________________________________________________________")
tag1:Tag
tag1=soup1.project.st
print(tag1)
soup2=BeautifulSoup(src2,"lxml")
tag2:Tag
tag2=soup2.project.st
print("second___________________________________________________________________________________")
print(tag2)
#tag1.replaceWith(tag2)

tag1.clear()
tag1.append(tag2.xhtml)
print("third____________________________________________________________________________________")
print(tag1)
#sleep(10)

