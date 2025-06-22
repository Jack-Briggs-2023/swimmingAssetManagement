import json


class jsonFileManagement:


    def __init__(self, filePath):
        if not filePath.endswith('.json'):
            raise ValueError("File path must end with .json")
        self.filePath = filePath


    def searchClasses(self, classLevel, StartDate):
        foundClassesList = []
        try:
            with open(self.filePath, "r") as file:
                importedData = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            importedData = []
        if isinstance(importedData, dict):
            importedData = [importedData]
        for classIndex in importedData:
            if classIndex["selectedLevel"] == classLevel and classIndex["startDate"] == StartDate:
                print(f"Class found: {classIndex}")
                foundClassesList.append(classIndex)
        return foundClassesList

    
    def readJson(self):
        """Read JSON data from a file."""
        try:
            with open(self.filePath, 'r') as file:
                importedData = json.load(file)
                return importedData # returns a class list
            # if isinstance(importedData, dict):
            #     return json.load([importedData])
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}


    def writeJson(self, data):
        """Write JSON data to a file."""
        # with open(self.filePath, 'w') as file:
        #     json.dump(data, file, indent=4)
        importedData = self.readJson()
        if isinstance(importedData, dict):
            importedData = [importedData]
        importedData.append(data)
        with open(self.filePath, 'w') as file:
            json.dump(importedData, file, indent=4)
        return importedData


    def findJsonClassAmount(self):
        return len(self.readJson())

FM = jsonFileManagement("jsonClassData.json")
# print(type(FM.readJson()))
# print(FM.searchClasses("Swimmer 2", "2025-06-21"))
# print(FM.findJsonClassAmount())



# Uncomment the following methods if you need to read/write JSON data from/to a file.


# [
#     {
#         "ClassName": "",
#         "startDate": "",
#         "amountOfSets": "",
#         "selectedLevel": ""
#     },
#     {
#         "ClassName": "class 1",
#         "startDate": "2025-06-21",
#         "amountOfSets": "6",
#         "selectedLevel": "Swimmer 2"
#     },
#     {
#         "ClassName": "class 2",
#         "startDate": "2025-05-27",
#         "amountOfSets": "34",
#         "selectedLevel": "Swimmer 2"
#     },
#     {
#         "ClassName": "class 3",
#         "startDate": "2025-05-27",
#         "amountOfSets": "23",
#         "selectedLevel": "Swimmer 1"
#     }
# ]