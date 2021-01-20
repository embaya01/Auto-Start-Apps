import tkinter as tk
from tkinter import filedialog, Text
import os

# Windows
root = tk.Tk()
root.title("Auto Start Apps")
apps = []

# Load saved file

if os.path.isfile('saved.txt'):
    with open('saved.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def printFiles():
    for app in apps:
        label = tk.Label(frame, text=app, bg="blue", fg="white",)
        label.pack()


# Add Apps Method


def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(
        initialdir="/", title=" Select An Application", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    if len(apps) != 0:
        printFiles()


def runApps():
    for app in apps:
        os.startfile(app)


# Main Container
canvas = tk.Canvas(root, height=700, width=700, bg="#eee")
canvas.pack()

# container
frame = tk.Frame(root, bg="white", borderwidth=2, relief='sunken')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.05)

# add app button
addApp = tk.Button(root, text="Add App", padx=10,
                   pady=5, fg="white", bg="green", command=addApp)
addApp.pack()
runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg="white", bg="green", command=runApps)
runApps.pack()

printFiles()
# Run
root.mainloop()

# Saving data to file
with open('saved.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
