import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog, Text
from tkinter import messagebox
import os

HEIGHT = 700
WIDTH = 800
folders = []
root = tk.Tk()

v = tk.IntVar()
t = tk.IntVar()

if os.path.isfile('saved.txt'):
    with open('saved.txt', 'r') as f:
        tempFolders = f.read()
        tempFolders = tempFolders.split('%')
        for tempFolder in tempFolders:
            folderApps = tempFolder.split('$')
            if len(folderApps) > 1:
                if len(folderApps[1]) != 0:
                    tempApps = folderApps[1].split(',')
                    apps = [x for x in tempApps if x.strip()]
                else:
                    apps = []
                folder = {folderApps[0]: apps}
                folders.append(folder)

# Print the folders


def printApps():
    for widget in frame3.winfo_children():
        widget.destroy()

    value = 0
    if len(folders) != 0:
        folderName = list(folders[v.get()].keys())

        for app in folders[v.get()].get(folderName[0]):
            tk.Radiobutton(frame3, text=app, width=90, padx=40, bg="white",
                           variable=t, value=value, command=selectFolder).pack(anchor=tk.W)
            value = value + 1
    if value != 0:
        delApp_btn['state'] = tk.NORMAL

# Add Apps Method


def addApp():
    for widget in frame3.winfo_children():
        widget.destroy()

    folderName = list(folders[v.get()].keys())
    filename = filedialog.askopenfilename(
        initialdir="/", title=" Select An Application", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps = folders[v.get()].get(folderName[0])
    apps.append(filename)
    folders[v.get()].update({folderName[0]: apps})
    if len(folders[v.get()]) > 0:
        printApps()

# Removes Selected App


def delApp():
    folderNames = list(folders[v.get()].keys())
    apps = folders[v.get()].get(folderNames[0])
    msg = "Are you sure you want to delete " + apps[t.get()] + "?"
    answer = messagebox.askyesno("Confirmation", msg)
    if answer:
        apps.remove(apps[t.get()])
        folders[v.get()].update({folderNames[0]: apps})
        # printFolders()
        printApps()
        if len(apps) == 0:
            delApp_btn['state'] = tk.DISABLED
            runApps_btn['state'] = tk.DISABLED
    else:
        print(answer)
# select a folder


def selectFolder():
    newApp_btn['state'] = tk.NORMAL
    delFolder_btn['state'] = tk.NORMAL
    folderNames = list(folders[v.get()].keys())
    if len(folders[v.get()].get(folderNames[0])) != 0:
        runApps_btn['state'] = tk.NORMAL
    printApps()

# Print the folders


def printFolders():
    for widget in frame2.winfo_children():
        widget.destroy()

    value = 0
    for folder in folders:
        folder = list(folder.keys())
        tk.Radiobutton(frame2, text=folder[0], indicatoron=0, width=90, padx=40,
                       variable=v, value=value, command=selectFolder).pack(anchor=tk.W)
        value = value + 1


def addFolder(folderName):
    for widget in frame2.winfo_children():
        widget.destroy()

    d = {folderName: []}
    folders.append(d.copy())
    if len(folders) != 0:
        printFolders()
    newFolder_entry.delete(0, 'end')

# Removes Selected Folder


def delFolder():
    folderNames = list(folders[v.get()].keys())
    msg = "Are you sure you want to delete " + folderNames[0] + "?"
    answer = messagebox.askyesno("Confirmation", msg)
    if answer:
        folders.remove(folders[v.get()])
        printFolders()
        printApps()
        print(folders)
        if len(folders) == 0:
            delApp_btn['state'] = tk.DISABLED
            runApps_btn['state'] = tk.DISABLED
            newApp_btn['state'] = tk.DISABLED
    else:
        print(answer)


def runApps():
    folderName = list(folders[v.get()].keys())
    for app in folders[v.get()].get(folderName[0]):
        os.startfile(app)


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

bg_image = ImageTk.PhotoImage(Image.open('bg.jpg'))
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#ccc")
frame.place(relx=0.5, rely=0.1, relwidth=0.94, relheight=0.06, anchor="n")

newFolder_entry = tk.Entry(frame, font=50)
newFolder_entry.place(relx=0.03, rely=0.1, relwidth=0.3, relheight=0.8)
newFolder_entry.focus()
newFolder_btn = tk.Button(frame, text="Add New Folder",
                          command=lambda: addFolder(newFolder_entry.get()))
newFolder_btn.place(relx=0.33, rely=0.1, relheight=0.8)

newApp_btn = tk.Button(frame, text="Add New App",
                       state='disabled', command=addApp)
newApp_btn.place(relx=0.63, rely=0.1, relheight=0.8)

delApp_btn = tk.Button(frame, text="Remove App",
                       state='disabled', command=delApp)
delApp_btn.place(relx=0.77, rely=0.1, relheight=0.8)

frame2 = tk.Frame(root, bg="#ccc", bd=5)
frame2.place(relx=0.03, rely=0.19, relwidth=0.45, relheight=0.7)

folders_label = tk.Label(frame2, bg="#fff")
folders_label.place(relwidth=1, relheight=1)

frame3 = tk.Frame(root, bg="#ccc", bd=5)
frame3.place(relx=0.51, rely=0.19, relwidth=0.46, relheight=0.7)

apps_label = tk.Label(frame3, bg="#fff")
apps_label.place(relwidth=1, relheight=1)

frame4 = tk.Frame(root, bg="#ccc")
frame4.place(relx=0.5, rely=0.92, relwidth=0.94, relheight=0.05, anchor='n')

delFolder_btn = tk.Button(frame4, text="Remove Folder",
                          state='disabled', command=delFolder)
delFolder_btn.place(relx=0.015, rely=0.1, relheight=0.8, relwidth=0.45)

runApps_btn = tk.Button(frame4, text="Run Apps",
                        state='disabled', command=runApps)
runApps_btn.place(relx=0.53, rely=0.1, relheight=0.8, relwidth=0.45)
printFolders()
root.mainloop()

# Saving data to file
with open('saved.txt', 'w') as f:
    for folder in folders:
        folderName = list(folder.keys())
        f.write(folderName[0] + '$')
        for app in folder.get(folderName[0]):
            f.write(app + ',')
        f.write("%")
