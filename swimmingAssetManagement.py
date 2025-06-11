import tkinter as tk
from tkinter import ttk
import tkcalendar
from tkcalendar import DateEntry
import tkinter.font as tkFont
from datetime import date
import time

# Create main window
tkinterMainAssetRoot = tk.Tk()
tkinterMainAsseFrame = tk.Frame(tkinterMainAssetRoot)
tkinterMainAsseFrame.pack(expand=True)
tkinterMainAssetRoot.title("Swim Help")

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
    "Bronze": ["Bronze Star", "Bronze Medallion", "Bronze Cross"]
}
lifesavingSocietyLevelTitle = "Lifesaving Society Swim Program Level"

class CreateNewLessonPlanWindow:
    def __init__(self, master, frame):
        self.master = master
        self.frame = frame
        self.master.title("Create New Lesson Plan")
        self.master.attributes('-fullscreen', True)
        self.placeholderWidgetList = []
        self.placeholderList = []

        for widget in self.frame.winfo_children():
            widget.destroy()

        self.master.focus_set()

        label = tk.Label(self.frame, text="Create New Lesson Plan", font=("Roboto", 24))
        label.pack(pady=defaultWidgeToWidgettPadding)
        self.lessonNameEntry = tk.Entry(self.frame, font=("Roboto", 16), fg='grey')
        self.lessonNameEntry.pack(pady=defaultLabelToWidgetPadding)
        self.lessonNamePlaceholderText  = "Enter Lesson Name (for display only): "
        self.lessonNameEntry.insert(0, self.lessonNamePlaceholderText )
        # Bindings for placeholder text to clear and restore
        self.lessonNameEntry.bind("<FocusIn>", self._clear_placeholder)
        self.lessonNameEntry.bind("<FocusOut>", self._restore_placeholder)
        self.placeholderWidgetList.append(self.lessonNameEntry)
        self.placeholderList.append(self.lessonNamePlaceholderText)

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
        self.placeholderWidgetList.append(self.amountOfSetsEntry)
        self.placeholderList.append(self.amountOfSetsPlaceholderText)

        # Dropdown for selecting level
        self.selectedGroupLevel = tk.StringVar()
        levelOptions = list(lifesavingSocietyLevels.keys())
        self.levelGroupComboBox = ttk.Combobox(self.frame, textvariable=self.selectedGroupLevel, values=levelOptions, state="readonly")
        self.levelGroupComboBox.set(lifesavingSocietyLevelTitle)
        self.levelGroupComboBox.bind("<<ComboboxSelected>>", self.on_combobox_selected)
        self.levelGroupComboBox.pack(pady=defaultWidgeToWidgettPadding)


        self.saveAndExitButton = tk.Button(self.frame, text="Save And Exit Lesson Plan", font=("Roboto", 16, "bold"), command=self.save_and_exit_lesson_plan)
        self.saveAndExitButton.pack(side="left",pady=defaultWidgeToWidgettPadding)
        self.saveButton = tk.Button(self.frame, text="Save Lesson Plan", font=("Roboto", 16, "bold"), command=self.save_lesson_plan)
        self.saveButton.pack(side="right",pady=defaultWidgeToWidgettPadding, padx=15)

        self.errorLabel = None
        self.subLevelDropDown = None

    def save_lesson_plan(self):
        lessonName = self.lessonNameEntry.get()
        startDate = self.startDateEntry.get()
        amountOfSets = self.amountOfSetsEntry.get()
        selectedLevel = self.selectedSubLevel.get()

        if (lessonName.strip() == "" or lessonName == self.lessonNamePlaceholderText) or startDate.strip() == "" or amountOfSets.strip() == "" or selectedLevel == lifesavingSocietyLevelTitle:
            self.display_error("Lesson name is required")
            print("Please enter a valid lesson name")
            return
        print(f"Saved: {lessonName}, {startDate}, {amountOfSets}, {selectedLevel}")

    def save_and_exit_lesson_plan(self):
        self.save_lesson_plan()
        # lessonNameEntry = self.lessonNameEntry.get()
        # startDate = self.startDateEntry.get()
        # amountOfSets = self.amountOfSetsEntry.get()
        # print(f"Saved: {lessonNameEntry}, {startDate}, {amountOfSets}")
        # self.lessonNameEntry.delete(0, "end")
        # self.lessonNameEntry.insert(0, self.lessonNamePlaceholderText)
        # self.lessonNameEntry.config(fg="grey")
        # self.startDateEntry.set_date(date.today())
        # self.amountOfSetsEntry.delete(0, "end")
        # self.selectedGroupLevel.set('')
        reset_to_main_menu()
        self.master.focus_set()

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
        
        # if self.lessonNameEntry.get() == self.lessonNamePlaceholderText:
        #     self.lessonNameEntry.delete(0, "end")
        #     self.lessonNameEntry.config(fg="grey")

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
        for widget in self.frame.winfo_children():
            if isinstance(widget, ttk.Combobox) and widget != self.levelGroupComboBox:
                widget.destroy()
        for level in lifesavingSocietyLevels:
            if level in self.selectedGroupLevel.get():
                self.selectedSubLevel = tk.StringVar()
                self.selectedSubLevel.set(lifesavingSocietyLevelTitle)
                self.sublevelGroupComboBox = ttk.Combobox(self.frame, textvariable=self.selectedSubLevel, values=lifesavingSocietyLevels.get(level), state="readonly")
                break
        self.sublevelGroupComboBox.pack(after=self.levelGroupComboBox)

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

# Fullscreen
tkinterMainAssetRoot.attributes('-fullscreen', True)

def newPlanButton_action():
    print("newPlanButton pressed!")
    newPlan = CreateNewLessonPlanWindow(tkinterMainAssetRoot, tkinterMainAsseFrame)

def oldPlanButton_action():
    print("oldPlanButton pressed!")

def exitButton_action():
    tkinterMainAssetRoot.destroy()
    print("exitButton pressed!")

def reset_to_main_menu():
    for widget in tkinterMainAsseFrame.winfo_children():
        widget.destroy()
    newPlanButton = tk.Button(tkinterMainAsseFrame, text="Create New Lesson Plan", font=("Roboto", 16), command=newPlanButton_action)
    oldPlanButton = tk.Button(tkinterMainAsseFrame, text="View Old Lesson Plan", font=("Roboto", 16), command=oldPlanButton_action)
    exitButton = tk.Button(tkinterMainAsseFrame, text="Exit", font=("Roboto", 16, "bold"), command=exitButton_action)
    
    newPlanButton.pack(pady=defaultWidgeToWidgettPadding)
    oldPlanButton.pack(pady=defaultWidgeToWidgettPadding)
    exitButton.pack(pady=defaultWidgeToWidgettPadding)



tkinterMainAssetRoot.bind("<Escape>", lambda e: tkinterMainAssetRoot.destroy())

newPlanButton = tk.Button(tkinterMainAsseFrame, text="Create New Lesson Plan", font=("Roboto", 16), command=newPlanButton_action)
oldPlanButton = tk.Button(tkinterMainAsseFrame, text="View Old Lesson Plan", font=("Roboto", 16), command=oldPlanButton_action)
exitButton = tk.Button(tkinterMainAsseFrame, text="Exit", font=("Roboto", 16, "bold"), command=exitButton_action)

newPlanButton.pack(pady=defaultWidgeToWidgettPadding)
oldPlanButton.pack(pady=defaultWidgeToWidgettPadding)
exitButton.pack(pady=defaultWidgeToWidgettPadding)

tkinterMainAssetRoot.mainloop()
