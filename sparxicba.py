# Run update.py instead of this script
from tkinter import *
from tkinter import ttk

import threading


def addtolist(code, string):
    with open("sparxanswers.txt", "a") as listfile:
        listfile.write(code + '@@' + string + '\n')


def readlist(code):
    with open("sparxanswers.txt", "r") as listfile:
        for line in listfile:
            parts = line.strip().split("@@")
            if code == parts[0]:
                return parts[1]
    return None

def tkinterthread():
    root = Tk()

    curr = StringVar(root, '1A')
    ans = StringVar(root, '')

    def advanceL():
        splcode = [*(curr.get())]
        if splcode[1] == 'Z':
            pass
        else:
            cai = ord(splcode[1])
            cai += 1
            nextcode = splcode[0] + chr(cai).upper()
            curr.set(nextcode)
    
    def advanceN():
        splcode = [*(curr.get())]
        nextcode = str(int(splcode[0])+1) + "A"
        curr.set(nextcode)
    

    def read():
        ans.set(readlist(curr.get()))
    
    def save():
        addtolist(curr.get(), ans.get())
        advanceL()
        ans.set("")

    root.title("Sparx I CBA by Deac")
    root.focus()
    root.geometry("250x140")
    root.attributes('-topmost', True)

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    ttk.Entry(mainframe, textvariable=curr).grid(column=2, row=1, sticky=(W, E))
    ttk.Label(mainframe, text='Code:').grid(column=1, row=1, sticky=W)

    ttk.Entry(mainframe, textvariable=ans).grid(column=2, row=2, sticky=(W, E))
    ttk.Label(mainframe, text='Answer:').grid(column=1, row=2, sticky=W)

    ttk.Button(mainframe, text="Advance L", command=advanceL).grid(column=1, row=3, sticky=(W, E))
    ttk.Button(mainframe, text="Advance #", command=advanceN).grid(column=1, row=4, sticky=(W, E))
    ttk.Button(mainframe, text="Read", command=read).grid(column=2, row=3, sticky=(W, E))
    ttk.Button(mainframe, text="Save", command=save).grid(column=2, row=4, sticky=(W, E))

    root.mainloop()


thread = threading.Thread(target=tkinterthread)
thread.start()