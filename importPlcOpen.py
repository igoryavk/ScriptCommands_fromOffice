import os
 
# Specify the project file name
project_name = "PLCOpenXMLImport.project"
 
# Define the path where the project should be/is stored
project_path = r"C:\Python"
 
# Define the file where the exported object is stored
file_name = os.path.join(project_path, r"C://json//myexport.xml")
 
# Create the import reporter
class Reporter(ImportReporter):
    def error(self, message):
        system.write_message(Severity.Error, message)
    def warning(self, message):
        system.write_message(Severity.Warning, message)
    def resolve_conflict(self, obj):
        return ConflictResolve.Copy
    def added(self, obj):
        print("added: ", obj)
    def replaced(self, obj):
        print("replaced: ", obj)
    def skipped(self, obj):
        print("skipped: ", obj)
    @property
    def aborting(self):
        return False
 
try:
    # Clean up any open project
    if projects.primary:
        projects.primary.close()
 
    # Create the reporter instance
    reporter = Reporter()
 
    # Create the new project
    project_reference = projects.create(os.path.join(project_path, project_name), True)
 
    # Import the data into the project
    project_reference.import_xml(reporter, file_name)
 
    # Save the project to the specified path
    project_reference.save()
except Exception as exception:
    print("Error: " + str(exception))
    if not system.trace:
       print("Please turn on the 'Script Tracing' function to get detailed information about the script execution.")