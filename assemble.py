EXPORT_PATH="D://parse//Device-1.xml"
SAVER_PATH="C://Users//i.yavkin//PycharmProjects//PlcParserForTestProject//saveall.py"

from os import system as load
import inspect

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


toplevel_objs=projects.primary.get_children()
my_reporter=MyReporter()
print("This is a list of Codesys Objects:")
projects.primary.find("Device")[0].export_xml(path=EXPORT_PATH,reporter=my_reporter,recursive=True,export_folder_structure=True)

load("python {0}".format(SAVER_PATH))