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
        label.pack(pady=20)

        # Example input field
        self.lessonNameEntry = tk.Entry(self.frame, font=("Roboto", 16))
        self.lessonNameEntry.pack(pady=10)
        self.lessonNameEntry.insert(0, "Enter Lesson Name")  # Placeholder text

        # Bind events to simulate placeholder behavior
        self.lessonNameEntry.bind("<FocusIn>", self._clear_placeholder)
        self.lessonNameEntry.bind("<FocusOut>", self._restore_placeholder)

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



# Create main window
tkinterMainAssetRoot = tk.Tk()
tkinterMainAsseFrame = tk.Frame(tkinterMainAssetRoot)
tkinterMainAsseFrame.pack(expand=True)#, fill=tk.BOTH)
tkinterMainAssetRoot.title("Swim Help")

windowSizeX = tkinterMainAssetRoot.winfo_width()
windowSizeY = tkinterMainAssetRoot.winfo_height()
windowSizeButtonX = windowSizeX / 10
windowSizeButtonY = windowSizeY / 10
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
newPlanButton.pack(pady=20)
oldPlanButton.pack(pady=20)
exitButton.pack(pady=20)

# Start the app
tkinterMainAssetRoot.mainloop()