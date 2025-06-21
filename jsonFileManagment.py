import json


class jsonFileManagement:
    def __init__(self, file_path):
        if not file_path.endswith('.json'):
            raise ValueError("File path must end with .json")
        self.file_path = file_path

    def searchClasses(self, classLevel, StartDate):
        # Search for a class in the JSON
        try:
            with open("jsonClassData.json", "r") as file:
                importedData = json.load(file)  # This will be a list
        except (FileNotFoundError, json.JSONDecodeError):
            importedData = []

        if isinstance(importedData, dict):
            importedData = [importedData]
        print(importedData)
        importedData.append({
            "ClassName": importedData[0],
            "startDate": importedData[0],
            "amountOfSets": importedData[0],
            "selectedLevel": importedData[0]
        })
        print(importedData[0]["ClassName"])













        
    # def read_json(self):
    #     """Read JSON data from a file."""
    #     try:
    #         with open(self.file_path, 'r') as file:
    #             return json.load(file)
    #     except FileNotFoundError:
    #         return {}
    #     except json.JSONDecodeError:
    #         return {}

    # def write_json(self, data):
    #     """Write JSON data to a file."""
    #     with open(self.file_path, 'w') as file:
    #         json.dump(data, file, indent=4) 