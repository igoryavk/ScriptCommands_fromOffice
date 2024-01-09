import sys,os


projects.primary.export_xml(projects.primary.get_children(recursive=True),path="C://json//myexport.xml",recursive=True,export_folder_structure=True)
print("Executing")
pipe=os.popen("python C://Users//i.yavkin//PycharmProjects//BeautifulSoap//main.py")
print(pipe.read())
#pipe=os.popen("C:\ProgramData\CODESYS\Script Commands\gitcommit.bat")
#print(pipe.read())