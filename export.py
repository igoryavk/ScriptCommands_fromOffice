# encoding:utf-8
#from xml.dom.minidom import parse
#from re import search
#from re import sub
import subprocess
from os import system
import sys, os
#from xml.dom.minidom import Document
#import xmltodict

#xml="C:\\Users\\i.yavkin\\Documents\\MyPouRepository\\mypou2.xml"
#dict=xmltodict.parse(xml_input=xml,encoding="utf-8")
#result:Document
#result=parse(xml)
#print(result.firstChild)
#xml=projects.primary.export_xml(projects.primary.get_children(recursive=True))
#projects.primary.export_xml(projects.primary.get_children(recursive=True),path="C:\\Users\\i.yavkin\\Documents\\MyPouRepository\\testing-artifacts\\mypou2.xml")
#projects.primary.import_xml(dataOrPath="C:\\Users\\i.yavkin\\Documents\\MyPouRepository\\mypou2.xml",import_folder_structure=True)
#system('git commit -a -m \"New commit\"')
#system('git push')
#system('C:\\ProgramData\\CODESYS\\Script Commands\\start.bat')
#
# SCRIPT_PATH=r"C:\test\command.py"
# pipe=os.popen('python '+SCRIPT_PATH)
# print(pipe.read())
#xml=prg.export_xml()
#xml=search('<ST\>((.|\n)*)\</ST>',xml)
#xml=sub('<ST>((.|\n)*)<xhtml xmlns="http://www.w3.org/1999/xhtml">','',xml.group(0))

#xml=sub('</xhtml>((.|\n)*)</ST>','',xml)
#print(xml)
#print(xml)

#Block-Описание: Получаем доступ к объекту текущего проекта и экспортируем его содержимое в xml
print("Stage1: Exporting the projects data into xml-file")
ExportPath=r"C:\Users\i.yavkin\Documents\MyPouRepository\testing-artifacts\project.xml"
projects.primary.export_xml(projects.primary.get_children(recursive=True),ExportPath)
#EndOfBlock-

#--Block--Описание: Запускаем сторонний скрипт для парсинга файла проекта и сохранения из него кода ST
print("Stage2: Parsing the project file and saving source code into file")
ScriptPath=r"C:\Users\i.yavkin\Documents\MyPouRepository\testing-artifacts\parser.py"
pipe=os.popen('python '+ScriptPath)
print(pipe.read())
#--EndOfBlock--

#--Block--Описание: Запускаем git для сохранения файлов в репозиторий
SaveFilePath=r"C:\Users\i.yavkin\Documents\MyPouRepository\testing-artifacts\update_repository.bat"
pipe=os.popen(SaveFilePath)
print(pipe.read())
#--EndOfBlock--