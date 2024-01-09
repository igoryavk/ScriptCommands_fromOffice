from os import system as load
import os
list=""

for level1 in projects.primary.get_children():
    list=list+"{0} ".format(level1.get_name())
    #list.append(level1.get_name())
    # for level2 in level1.get_children():
    #     list=list+"{0} ".format(level2.)
# for obj in projects.primary.get_children(False):
#     list=list+"{0} ".format(obj.find("AI4_PRG").get_name())


with os.popen("C://Python//Objects//CodesysListObjects.exe {0}".format(list),"r") as pipe:
    data=pipe.read()
    pipe.close()
print(data)
print("Hello here i am")