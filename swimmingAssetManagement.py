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
import tkinter.font as tkFont

# Create main window
tkinterMainAssetRoot = tk.Tk()
tkinterMainAssetRoot.title("Swim Help")

windowSizeX = tkinterMainAssetRoot.winfo_width()
windowSizeY = tkinterMainAssetRoot.winfo_height()
windowSizeButtonX = windowSizeX / 10
windowSizeButtonY = windowSizeY / 10
# Make the window full screen
tkinterMainAssetRoot.attributes('-fullscreen', True)

def newPlanButton_action():
    print("newPlanButton pressed!")
    CreateNewLessonPlan(tkinterMainAssetRoot)

def oldPlanButton_action():
    print("oldPlanButton pressed!")

def exitButton_action():
    tkinterMainAssetRoot.destroy() # command=tkinterMainAssetRoot.quit
    print("exitButton pressed!")

# Optional: Press Esc to exit full screen
# def exit_fullscreen(event):
#     tkinterMainAssetRoot.attributes('-fullscreen', False)

# ends the program when Esc is pressed
tkinterMainAssetRoot.bind("<Escape>", lambda e: tkinterMainAssetRoot.destroy())

# Create buttons
newPlanButton = tk.Button(tkinterMainAssetRoot, text="Create New Lesson Plan", font=("Roboto", 16), command=newPlanButton_action)
# newPlanButton.pack(x=(windowSizeX / 2) - (newPlanButton.winfo_width() / 2), y=(windowSizeY / 2) - (newPlanButton.winfo_height() / 2))
oldPlanButton = tk.Button(tkinterMainAssetRoot, text="View Old Lesson Plan", font=("Roboto", 16), command=oldPlanButton_action)
exitButton = tk.Button(tkinterMainAssetRoot, text="Exit", font=("Roboto", 16, "bold"), command=exitButton_action)

# Arrange buttons vertically in the center
newPlanButton.pack(pady=20)
oldPlanButton.pack(pady=20)
exitButton.pack(pady=20)

# Start the app
tkinterMainAssetRoot.mainloop()

class CreateNewLessonPlan:
    def __init__(self, master):
        self.master = master
        self.master.title("Create New Lesson Plan")
        self.master.attributes('-fullscreen', True)

        # Add widgets for creating a new lesson plan here
        label = tk.Label(self.master, text="Create New Lesson Plan", font=("Arial", 24))
        label.pack(pady=20)

        # Example input field
        self.lessonNameEntry = tk.Entry(self.master, font=("Arial", 16))
        self.lessonNameEntry.pack(pady=10)
        self.lessonNameEntry.insert(0, "Enter Lesson Name")  # Placeholder text