import inspect
import subprocess
class MyReporter(ExportReporter):
    def error(self, obj, message):
        print("Error from {0}: {1}".format(obj,message))


    def warning(self, obj, message):
        print("Warning from {0}: {1}".format(obj, message))

    def nonexportable(self, obj):
        print("This object cant be exported: {0}".format(obj.get_name()))

    @property
    def aborting(self):
        """This allows abortion when we report non-exportable objects.

        :rtype: bool

        """
        pass

class MyImportReporter(ImportReporter):
    def error(self, message):
        print("Error from {0}:".format(message))


    def warning(self,  message):
        print("Warning from {0}: {1}".format(obj, message))
        
    @property
    def aborting(self):
        """Gets a boolean value indicating whether importing should be aborted or not.

        :rtype: bool

        """
        print("Something went wrong")



device=projects.primary.find("Device",recursive=True)

tree_obj=device[0].get_children(recursive=True)
exclude_list=["OwenCloud","Buzzer","Drives","Screen","Network","Debug","RTC","Info","Watchdog"]
list_xml=[]
for obj in tree_obj:
    for exclude in exclude_list:
        if obj.get_name() != exclude:
            list_xml.append(obj)
            break
for obj in list_xml:
    print(obj.get_name())
reporter=MyReporter()
projects.primary.export_xml(objects=list_xml,reporter=reporter,path="D://parse//new.xml",recursive=True)
# for item in toplevel_objs:
#
#     #item.export_xml(path="D://parse//{0}.xml".format(item.get_name()),reporter=my_reporter,recursive=True)
#     print(item.type)
#toplevel_objs[15].export_xml(path="D://parse//210_4.xml",reporter=my_reporter,recursive=True)

#items=toplevel_objs[15].get_children()
# for item in items:
#     item.export_xml(path="D://parse//{0}.xml".format(item.get_name()))