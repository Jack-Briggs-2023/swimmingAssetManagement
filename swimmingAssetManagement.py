# from tkinter import  *
# tkinterMainAsset = Tk()
# '''
# widgets are added here
# '''
# tkinterMainAsset.mainloop()

# label = Label(tkinterMainAsset, text='Swim Help!')
# label.pack()
# tkinterMainAsset.mainloop()
import tkinter as tk
import tkcalendar
from tkcalendar import DateEntry
import tkinter.font as tkFont


# Create main window
tkinterMainAssetRoot = tk.Tk()
tkinterMainAsseFrame = tk.Frame(tkinterMainAssetRoot)
tkinterMainAsseFrame.pack(expand=True)#, fill=tk.BOTH)
tkinterMainAssetRoot.title("Swim Help")

windowSizeX = tkinterMainAssetRoot.winfo_width()
windowSizeY = tkinterMainAssetRoot.winfo_height()
windowSizeButtonX = windowSizeX / 10
windowSizeButtonY = windowSizeY / 10
defaultWidgetPadding = 20


# Lifesaving Society swim program levels in order
lifesavingSocietyLevels = {
    "Parent & Tot": [
        "Parent & Tot 1",  # For 4–12 months
        "Parent & Tot 2",  # For 12–24 months
        "Parent & Tot 3"   # For 24–36 months
    ],
    "Preschool": [
        "Preschool 1", "Preschool 2", "Preschool 3",
        "Preschool 4", "Preschool 5"
    ],
    "Swimmer": [
        "Swimmer 1", "Swimmer 2", "Swimmer 3",
        "Swimmer 4", "Swimmer 5", "Swimmer 6"
    ],
    "Swim Patrol": [
        "Rookie Patrol",
        "Ranger Patrol",
        "Star Patrol"
    ],
    "Bronze": [
        "Bronze Star",
        "Bronze Medallion",
        "Bronze Cross"
    ]
}
lifesavingSocietyLevelTitle = "Lifesaving Society Swim Program Level (Parent and Tot 1 -3, Preschool 1-5, Swimmer 1-6, Patrol, and Bronzes):"



class CreateNewLessonPlanWindow:
    def __init__(self, master, frame):
        self.master = master
        self.frame = frame
        self.master.title("Create New Lesson Plan")
        self.master.attributes('-fullscreen', True)

        for widget in self.frame.winfo_children():
            widget.destroy()

        # Add widgets for creating a new lesson plan here
        label = tk.Label(self.frame, text="Create New Lesson Plan", font=("Roboto", 24))
        label.pack(pady=defaultWidgetPadding)

        # Example input field
        self.lessonNameEntryButton = tk.Entry(self.frame, font=("Roboto", 16))
        self.lessonNameEntryButton.pack(pady=10)
        self.lessonNameEntryButton.insert(0, "Enter Lesson Name (for display only): ")  # Placeholder text

        # Bind events to simulate placeholder behavior
        self.lessonNameEntryButton.bind("<FocusIn>", self._clear_placeholder)
        self.lessonNameEntryButton.bind("<FocusOut>", self._restore_placeholder)

        # Example date entry using tkcalendar
        self.dateLabel = tk.Label(self.frame, text="Select Start Date:", font=("Roboto", 16))
        self.dateLabel.pack(pady=defaultWidgetPadding)
        self.dateEntryButton = DateEntry(self.frame, width=12, background='grey', foreground='lightgrey', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.dateEntryButton.pack(pady=defaultWidgetPadding)

        # Example entry for amount of sets
        amountOfSetsButton = tk.Entry(self.frame, text="Enter Amount of Sets:", font=("Roboto", 16))
        amountOfSetsButton.pack(pady=defaultWidgetPadding)

        self.levelLavel = tk.Label(self.frame, text=lifesavingSocietyLevelTitle, font=("Roboto", 16))
        self.levelLavel.pack(pady=defaultWidgetPadding)
        self.selectLevel = tk.StringVar()
        levelDropDown = tk.Combobox(self.frame, textvariable=self.selectLevel, values=lifesavingSocietyLevels, state="readonly")
        levelDropDown.pack(pady=defaultWidgetPadding)  # Set default text

        # Example button to save the lesson plan
        self.saveButton = tk.Button(self.frame, text="Save Lesson Plan", font=("Roboto", 16, "bold"), command=self.save_lesson_plan)
        self.saveButton.pack(pady=defaultWidgetPadding)



    def save_lesson_plan(self):
        lessonNameEntry = self.lessonNameEntryButton.get()
        startDate = self.dateEntryButton.get()
        amountOfSets = self.amountOfSetsButton.get()
        # print(f"Lesson Plan Saved: {lessonNameEntry} on {startDate}")
        # Here you would typically save the lesson plan to a file or database

        # Clear the entry fields after saving
        self.lessonNameEntry.delete(0, "end")
        self.lessonNameEntry.insert(0, "Enter Lesson Name")
        self.dateEntry.set_date('')

    def _clear_placeholder(self, event):
        if self.lessonNameEntry.get() == "Enter Lesson Name":
            self.lessonNameEntry.delete(0, "end")
            self.lessonNameEntry.config(fg="black")

    def _restore_placeholder(self, event):
        if self.lessonNameEntry.get() == "":
            self.lessonNameEntry.insert(0, "Enter Lesson Name")
            self.lessonNameEntry.config(fg="grey")

# class CreateNewLessonPlan:
#     def __init__(self, master):

# Make the window full screen
tkinterMainAssetRoot.attributes('-fullscreen', True)

def newPlanButton_action():
    print("newPlanButton pressed!")
    newPlan = CreateNewLessonPlanWindow(tkinterMainAssetRoot, tkinterMainAsseFrame)

def oldPlanButton_action():
    print("oldPlanButton pressed!")

def exitButton_action():
    tkinterMainAssetRoot.destroy() # command=tkinterMainAssetRoot.quit
    print("exitButton pressed!")

# buttonTotaList = []
# Optional: Press Esc to exit full screen
# def exit_fullscreen(event):
#     tkinterMainAssetRoot.attributes('-fullscreen', False)

# ends the program when Esc is pressed
tkinterMainAssetRoot.bind("<Escape>", lambda e: tkinterMainAssetRoot.destroy())

# Create buttons
newPlanButton = tk.Button(tkinterMainAsseFrame, text="Create New Lesson Plan", font=("Roboto", 16), command=newPlanButton_action)
# buttonTotaList.append(newPlanButton)
# newPlanButton.pack(x=(windowSizeX / 2) - (newPlanButton.winfo_width() / 2), y=(windowSizeY / 2) - (newPlanButton.winfo_height() / 2))
oldPlanButton = tk.Button(tkinterMainAsseFrame, text="View Old Lesson Plan", font=("Roboto", 16), command=oldPlanButton_action)
# buttonTotaList.append(oldPlanButton)
exitButton = tk.Button(tkinterMainAsseFrame, text="Exit", font=("Roboto", 16, "bold"), command=exitButton_action)
# buttonTotaList.append(exitButton)

# Arrange buttons vertically in the center
newPlanButton.pack(pady=defaultWidgetPadding)
oldPlanButton.pack(pady=defaultWidgetPadding)
exitButton.pack(pady=defaultWidgetPadding)

# Start the app
tkinterMainAssetRoot.mainloop()