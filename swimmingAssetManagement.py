import math
import tkinter as tk
from tkinter import ttk
import tkcalendar
from tkcalendar import DateEntry
import tkinter.font as tkFont
from datetime import date
import time
import json
import pytest
from jsonFileManagment import jsonFileManagement

# Create main window
tkinterMainAssetRoot = tk.Tk()
tkinterMainAsseFrame = tk.Frame(tkinterMainAssetRoot)
tkinterMainAsseFrame.pack(expand=True)
tkinterMainAssetRoot.title("Swim Help - Asset Management")
tkinterMainAssetRoot.geometry("800x600")  # Set a default size

windowSizeX = tkinterMainAssetRoot.winfo_width()
windowSizeY = tkinterMainAssetRoot.winfo_height()
windowSizeButtonX = windowSizeX / 10
windowSizeButtonY = windowSizeY / 10
# defaultWidgeToWidgettPadding = int(windowSizeY / 5)
# defaultLabelToWidgetPadding = int(windowSizeY / 10)
defaultWidgeToWidgettPadding = 20
defaultLabelToWidgetPadding = 1
defaultWidgetFont = ("Roboto", 16)

lifesavingSocietyLevels = {
    "Parent & Tot": ["Parent & Tot 1", "Parent & Tot 2", "Parent & Tot 3"],
    "Preschool": ["Preschool 1", "Preschool 2", "Preschool 3", "Preschool 4", "Preschool 5"],
    "Swimmer": ["Swimmer 1", "Swimmer 2", "Swimmer 3", "Swimmer 4", "Swimmer 5", "Swimmer 6"],
    "Swim Patrol": ["Rookie Patrol", "Ranger Patrol", "Star Patrol"],
    "Bronze Medals": ["Bronze Star", "Bronze Medallion", "Bronze Cross"]
}
lifesavingSocietyLevels = { # these level needed to be changed to the offical times for each level!!!
    "Parent & Tot": {
        "Parent & Tot 1": 30,
        "Parent & Tot 2": 30,
        "Parent & Tot 3": 30
    },
    "Preschool": {
        "Preschool 1": 35,
        "Preschool 2": 35,
        "Preschool 3": 35,
        "Preschool 4": 35,
        "Preschool 5": 35
    },
    "Swimmer": {
        "Swimmer 1": 45,
        "Swimmer 2": 45,
        "Swimmer 3": 45,
        "Swimmer 4": 45,
        "Swimmer 5": 45,
        "Swimmer 6": 45
    },
    "Swim Patrol": {
        "Rookie Patrol": 50,
        "Ranger Patrol": 50,
        "Star Patrol": 50
    },
    "Bronze Medals": {
        "Bronze Star": 60,
        "Bronze Medallion": 90,
        "Bronze Cross": 90
    }
}

lifesavingSocietyLevelTitle = "Lifesaving Society Swim Program Level"
defaultClass = {
    "ClassName": "",
    "startDate": "",
    "amountOfSets": "",
    "level": "",
}


class CreateNewClassWindow:
    def __init__(self, master, frame):
        self.master = master
        self.frame = frame
        self.master.title("Create A New Class")
        self.master.attributes('-fullscreen', True)
        self.placeholderWidgetList = []
        self.placeholderList = []
        self.jsonClass = jsonFileManagement("jsonClassData.json")

        for widget in self.frame.winfo_children():
            widget.destroy()

        self.master.focus_set()


        # Create a label for the window
        label = tk.Label(self.frame, text="Create A New Class", font=("Roboto", 24))
        label.pack(pady=defaultWidgeToWidgettPadding)
        self.classNameEntry = tk.Entry(self.frame, font=("Roboto", 16), fg='grey')
        # self.classNameEntry.pack(fill='x', padx=10)
        self.classNameEntry.pack(fill='x', padx=10, pady=defaultLabelToWidgetPadding)
        self.classNamePlaceholderText  = "Enter Class Name (for display only) "
        self.classNameEntry.insert(0, self.classNamePlaceholderText )
        # Bindings for placeholder text to clear and restore
        self.classNameEntry.bind("<FocusIn>", self._clear_placeholder)
        self.classNameEntry.bind("<FocusOut>", self._restore_placeholder)
        self.placeholderWidgetList.append(self.classNameEntry)
        self.placeholderList.append(self.classNamePlaceholderText)

        # Start date entry
        self.dateLabel = tk.Label(self.frame, text="Select Start Date:", font=("Roboto", 16))
        self.dateLabel.pack(pady=defaultWidgeToWidgettPadding)
        self.startDateEntry = DateEntry(self.frame, width=12, background='grey', foreground='lightgrey', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.startDateEntry.pack(pady=defaultLabelToWidgetPadding)

        # Amount of sets entry
        self.amountOfSetsLabel = tk.Label(self.frame, text="Amount Of Sets: ", font=("Roboto", 16))
        self.amountOfSetsLabel.pack(pady=defaultWidgeToWidgettPadding)
        self.amountOfSetsEntry = tk.Entry(self.frame, font=("Roboto", 16), fg='grey')
        self.amountOfSetsEntry.pack(pady=defaultLabelToWidgetPadding)
        self.amountOfSetsPlaceholderText  = "Amount Of Sets"
        self.amountOfSetsEntry.insert(0, self.amountOfSetsPlaceholderText )
        # Bindings for placeholder text to clear and restore
        self.amountOfSetsEntry.bind("<FocusIn>", self._clear_placeholder)
        self.amountOfSetsEntry.bind("<FocusOut>", self._restore_placeholder)
        # self.amountOfSetsEntry.bind("<KeyRelease>", self.check_if_number(self.amountOfSetsEntry)) # lambda e: 
        self.placeholderWidgetList.append(self.amountOfSetsEntry)
        self.placeholderList.append(self.amountOfSetsPlaceholderText)

        # Dropdown for selecting level
        self.selectedGroupLevel = tk.StringVar()
        levelOptions = list(lifesavingSocietyLevels.keys())
        self.levelGroupComboBox = ttk.Combobox(self.frame, textvariable=self.selectedGroupLevel, values=levelOptions, state="readonly")
        self.levelGroupComboBox.set(lifesavingSocietyLevelTitle)
        self.levelGroupComboBox.bind("<<ComboboxSelected>>", self.on_combobox_selected)
        self.levelGroupComboBox.pack(pady=defaultWidgeToWidgettPadding)

        # self.levelTimeLabel = tk.Label(self.frame, text="Select Level:", font=("Roboto", 16))
        # # Buttons for saving and exiting
        # self.saveAndExitButton = tk.Button(self.frame, text="Save And Exit Class Plan", font=("Roboto", 16, "bold"), command=self.save_class_and_exit)
        # self.saveAndExitButton.pack(side="left",pady=defaultWidgeToWidgettPadding)
        # self.saveButton = tk.Button(self.frame, text="Save Class Plan", font=("Roboto", 16, "bold"), command=self.save_class)
        # self.saveButton.pack(side="right",pady=defaultWidgeToWidgettPadding, padx=15)
        # Create a new frame to hold both buttons and error message
        self.buttonFrame = tk.Frame(self.frame)
        self.buttonFrame.pack(pady=defaultWidgeToWidgettPadding)

        # Add Save and Save+Exit buttons to this sub-frame
        self.saveAndExitButton = tk.Button(self.buttonFrame, text="Save Class And Exit", font=("Roboto", 16, "bold"), command=self.save_class_and_exit)
        self.saveAndExitButton.pack(side="left", padx=10)

        self.saveButton = tk.Button(self.buttonFrame, text="Save Class", font=("Roboto", 16, "bold"), command=self.save_class)
        self.saveButton.pack(side="right", padx=10)

        self.discardButton = tk.Button(self.buttonFrame, text="Discard Class", font=("Roboto", 16, "bold"), command=self.discard_class)
        self.discardButton.pack(side="right", padx=10)

        
        # Create a label for error messages
        self.errorLabel = None
        self.subLevelDropDown = None


    def discard_class(self):
        reset_to_main_menu()
        self.master.focus_set()

    def save_class_and_exit(self):
        if(self.save_class()):
            reset_to_main_menu(self.master)
            self.master.focus_set()

    def save_class(self):
        try:
            className = self.classNameEntry.get()
            startDate = self.startDateEntry.get()
            amountOfSets = self.amountOfSetsEntry.get()
            selectedLevel = self.selectedSubLevel.get()
        except AttributeError:
            self.display_error("Please fill in all fields")
            print("Please fill in all fields")
            return False
        saveData = {className, startDate, amountOfSets, selectedLevel}
        for data in saveData:
            if data.strip() == "" or data == self.classNamePlaceholderText or data == self.amountOfSetsPlaceholderText:
                self.display_error("Please fill in all fields")
                print("Please fill in all fields")
                return False
            
        # json things
        jsonExportData = {
            "ClassName": className,
            "startDate": startDate,
            "amountOfSets": amountOfSets,
            "selectedLevel": selectedLevel
        }
        
        # try:
        #     with open("jsonClassData.json", "r") as file:
        #         importedData = json.load(file)  # This will be a list
        # except (FileNotFoundError, json.JSONDecodeError):
        #     importedData = []

        # if isinstance(importedData, dict):
        #     importedData = [importedData]
        # importedData.append({
        #     "ClassName": className,
        #     "startDate": startDate,
        #     "amountOfSets": amountOfSets,
        #     "selectedLevel": selectedLevel
        # })

        # with open("jsonClassData.json", "w") as file:
        #     # file.write(json.dumps(importedData) + "\n")
        #     json.dump(importedData, file, indent=4)
        self.jsonClass.writeJson(jsonExportData)
        # print(printThis)
        print(f"Saved: {className}, {startDate}, {amountOfSets}, {selectedLevel}")
        return True

    def _clear_placeholder(self, event):
        widget = event.widget
        count = 0
        for placeholderWidget in self.placeholderWidgetList:
            if widget == placeholderWidget:
                # if self.placeholderWidgetList[count] == self.placeholderList[count]:
                if placeholderWidget.get() == self.placeholderList[count]:
                    placeholderWidget.delete(0, "end")
                    placeholderWidget.config(fg="black")
                    break
            count += 1
        # self.check_if_number(event)
        # if self.classNameEntry.get() == self.classNamePlaceholderText:
        #     self.classNameEntry.delete(0, "end")
        #     self.classNameEntry.config(fg="grey")

    def _restore_placeholder(self, event):
        widget = event.widget
        count = 0
        for placeholderWidget in self.placeholderWidgetList:
            if widget == placeholderWidget:
                if placeholderWidget.get().strip() == "":
                    placeholderWidget.insert(0, self.placeholderList[count])
                    placeholderWidget.config(fg="grey")
            count += 1

    def on_combobox_selected(self, event):
    #     for widget in self.frame.winfo_children():
    #         if isinstance(widget, ttk.Combobox) and widget != self.levelGroupComboBox:
    #             widget.destroy()
    #     for level in lifesavingSocietyLevels:
    #         if level in self.selectedGroupLevel.get():
    #             self.selectedSubLevel = tk.StringVar()
    #             self.selectedSubLevel.set(lifesavingSocietyLevelTitle)
    #             self.sublevelGroupComboBox = ttk.Combobox(self.frame, textvariable=self.selectedSubLevel, values=lifesavingSocietyLevels.get(level), state="readonly")
    #             break
    #     self.sublevelGroupComboBox.pack(after=self.levelGroupComboBox)
    #     self.levelTimeLabel = tk.Label(self.frame, text=lifesavingSocietyLevels[self.selectedGroupLevel][self.selectedSubLevel], font=("Roboto", 16))
    # Destroy old sublevel combobox if one exists
        for widget in self.frame.winfo_children():
            if isinstance(widget, ttk.Combobox) and widget != self.levelGroupComboBox:
                widget.destroy()
        
        selected_group = self.selectedGroupLevel.get()

        if selected_group in lifesavingSocietyLevels:
            # Get sublevels (keys of the nested dictionary)
            sublevels = list(lifesavingSocietyLevels[selected_group].keys())

            self.selectedSubLevel = tk.StringVar()
            self.selectedSubLevel.set("Select Specific Level")  # default prompt

            self.sublevelGroupComboBox = ttk.Combobox(
                self.frame,
                textvariable=self.selectedSubLevel,
                values=sublevels,
                state="readonly"
            )
            self.sublevelGroupComboBox.pack(after=self.levelGroupComboBox)

            # Optional: bind to sublevel selection to show time
            self.sublevelGroupComboBox.bind("<<ComboboxSelected>>", self.show_level_time)

        
    def display_error(self, message):
        if self.errorLabel:
            self.errorLabel.destroy()
        self.errorLabel = tk.Label(self.frame, text="Please Select All Options And/Or Change Your Answer", font=("Roboto", 16),fg="red", bg="white")
        self.errorLabel.pack(side="bottom",pady=defaultWidgeToWidgettPadding)
        self.master.after(3000, self.remove_error)

    def remove_error(self):
        if self.errorLabel:
            self.errorLabel.destroy()
            self.errorLabel = None

    # def clear_all_fields(self):
    #     self.classNameEntry.delete(0, "end")
    #     self.classNameEntry.insert(0, self.classNamePlaceholderText)
    #     self.classNameEntry.config(fg="grey")
    #     self.startDateEntry.set_date(date.today())
    #     self.amountOfSetsEntry.delete(0, "end")
    #     self.amountOfSetsEntry.insert(0, self.amountOfSetsPlaceholderText)
    #     self.amountOfSetsEntry.config(fg="grey")
    #     self.selectedGroupLevel.set(lifesavingSocietyLevelTitle)
    #     if hasattr(self, 'sublevelGroupComboBox'):
    #         self.sublevelGroupComboBox.destroy()
    def check_if_number(self, widget):
        num = widget.get()
        try:
            int(num)
        except ValueError:
            widget.delete(0, "end")

    def show_level_time(self, event):
        selectedGroup = self.selectedGroupLevel.get()
        selected_level = self.selectedSubLevel.get()

        if selectedGroup and selected_level:
            minutes = lifesavingSocietyLevels[selectedGroup].get(selected_level, "N/A")
            
            if hasattr(self, "levelTimeLabel") and self.levelTimeLabel:
                self.levelTimeLabel.destroy()
            
            self.levelTimeLabel = tk.Label(
                self.frame,
                text=f"Class Time: {minutes} minutes",
                font=("Roboto", 16)
            )
            self.levelTimeLabel.pack(after=self.sublevelGroupComboBox, pady=defaultWidgeToWidgettPadding)


class ViewOldClassWindow:
    def __init__(self, master, frame):
        self.master = master
        self.frame = frame
        self.master.title("View Old Class")
        self.master.attributes('-fullscreen', True)
        self.placeholderWidgetList = []
        self.placeholderList = []
        self.jsonClass = jsonFileManagement("jsonClassData.json")
        self.foundClasses = self.jsonClass.readJson()

        for widget in self.frame.winfo_children():
            widget.destroy()

        label = tk.Label(self.frame, text="View Old Class", font=("Roboto", 24))
        label.pack(pady=defaultWidgeToWidgettPadding)

        # Placeholder for old class data
        self.oldClassDataLabel = tk.Label(self.frame, text="Old Class Data Will Be Displayed Here", font=("Roboto", 16), fg='grey')
        self.oldClassDataLabel.pack(pady=defaultWidgeToWidgettPadding)

        # for classData in self.foundClasses:
        #     text_button = tk.Label(self.frame, text=classData, fg="blue", cursor="hand2", font=("Roboto", 16, "underline"))
        #     text_button.bind("<Double-Button-1>", lambda event, data=classData: self.on_click(data, event))
        #     text_button.pack(pady=defaultWidgeToWidgettPadding)

        gridFrame = tk.Frame(self.frame)
        gridFrame.pack(pady=10)
        tk.Label(gridFrame, text="Class Level", font=("Roboto", 14, "bold")).grid(row=0, column=0, padx=10, pady=5)
        tk.Label(gridFrame, text="Start Date", font=("Roboto", 14, "bold")).grid(row=0, column=1, padx=10, pady=5)
        # tk.Label(self.frame, text="Class Level", font=("Roboto", 14, "bold")).pack(pady=5)
        # tk.Label(self.frame, text="Start Date", font=("Roboto", 14, "bold")).pack(pady=5)

        # Add rows of class data
        for index, classData in enumerate(self.foundClasses):
            levelLabel = tk.Label(gridFrame, text=classData["selectedLevel"], font=("Roboto", 12, "underline"), cursor="hand2")
            levelLabel.grid(row=index+1, column=0, padx=10, pady=5)
            levelLabel.bind("<Double-Button-1>", lambda event, data=classData: self.on_click(data, event))
            tk.Label(gridFrame, text=classData["startDate"], font=("Roboto", 12)).grid(row=index+1, column=1, padx=10, pady=5)
    def on_click(self, classData, event):
        print("Clicked on class data: ", classData)
    # def clicked(row, col):
    #     print(f"Button at ({row}, {col}) clicked")

# Fullscreen
tkinterMainAssetRoot.attributes('-fullscreen', True)

def newClassButton_action():
    print("newClassButton pressed!")
    newPlan = CreateNewClassWindow(tkinterMainAssetRoot, tkinterMainAsseFrame)

def oldClassButton_action():
    print("oldPlanButton pressed!")
    # findJsonClasse = jsonFileManagement("jsonClassData.json")
    # foundClasses = findJsonClasse.readJson()
    # print(f"Found Classes: {foundClasses}")
    viewOldPlan = ViewOldClassWindow(tkinterMainAssetRoot, tkinterMainAsseFrame)

def exitButton_action():
    tkinterMainAssetRoot.destroy()
    print("exitButton pressed!")

def reset_to_main_menu():
    for widget in tkinterMainAsseFrame.winfo_children():
        widget.destroy()
    newClassButton = tk.Button(tkinterMainAsseFrame, text="Create A New Class", font=("Roboto", 16), command=newClassButton_action)
    oldClassButton = tk.Button(tkinterMainAsseFrame, text="View Old Class", font=("Roboto", 16), command=oldClassButton_action)
    exitButton = tk.Button(tkinterMainAsseFrame, text="Exit", font=("Roboto", 16, "bold"), command=exitButton_action)
    newClassButton.pack(pady=defaultWidgeToWidgettPadding)
    oldClassButton.pack(pady=defaultWidgeToWidgettPadding)
    exitButton.pack(pady=defaultWidgeToWidgettPadding)
    # tkinterMainAsseFrame.set_focus()
    # newPlanButton.pack(pady=defaultWidgeToWidgettPadding)
    # oldPlanButton.pack(pady=defaultWidgeToWidgettPadding)
    # exitButton.pack(pady=defaultWidgeToWidgettPadding)

def reset_json_file(jsonFilePath):
    if not jsonFilePath.endswith('.json') and jsonFilePath != "":
        raise ValueError("File path must end with .json")
    # for index, data in enumerate(jsonData):
    #     jsonExportData = [index] = data
    # jsonExportData = {
    #     "ClassName": "",
    #     "startDate": "",
    #     "amountOfSets": "",
    #     "selectedLevel": ""
    # }
    with open("jsonClassData.json", "w") as file:
        file.write(json.dumps(defaultClass) + "\n")


# reset_json_file()
tkinterMainAssetRoot.bind("<Escape>", lambda e: tkinterMainAssetRoot.destroy())
reset_to_main_menu()
# reset_json_file("jsonClassData.json")


# newPlanButton.pack(pady=defaultWidgeToWidgettPadding)
# oldPlanButton.pack(pady=defaultWidgeToWidgettPadding)
# exitButton.pack(pady=defaultWidgeToWidgettPadding)

tkinterMainAssetRoot.mainloop()
