# -*- coding: utf-8 -*-
from System import Environment
import os
print("Importing function")

with os.popen("python C:\Users\i.yavkin\PycharmProjects\BeautifulSoap\new_block.py") as pipe:
    print(pipe.read())
filename="C:\\json\\myblock.xml"
file=open(filename,mode="r")
xml=file.read()
application=projects.primary.find("Application",True)
application[0].import_xml(None,xml)
#print(xml)
list_obj=projects.primary.get_children(True)
items=list()
i=0
for obj in list_obj:
    i=i+1
    if i<8:
        items.append(obj.get_name())
selected_item = system.ui.choose("my", items, True)