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



toplevel_objs=projects.primary.get_children()
print(toplevel_objs)
# for item in toplevel_objs:
#
#     #item.export_xml(path="D://parse//{0}.xml".format(item.get_name()),reporter=my_reporter,recursive=True)
#     print(item.type)
#toplevel_objs[15].export_xml(path="D://parse//210_4.xml",reporter=my_reporter,recursive=True)

#items=toplevel_objs[15].get_children()
# for item in items:
#     item.export_xml(path="D://parse//{0}.xml".format(item.get_name()))