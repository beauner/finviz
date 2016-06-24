#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

class MainWindow:
    def __init__(self, master):

        mainLabel = ttk.Label(master, text="Risk Management Assistant", justify = CENTER, font = 18).pack()

        self.executeButton = ttk.Button(master, text="Execute", command = self.execute)
        self.executeButton.pack()

        self.frame = ttk.Frame(master).pack()

        self.pricePoint = StringVar()
        ttk.Entry(master, width=30, textvariable=self.pricePoint).pack()

        self.totalCapital = StringVar()
        ttk.Entry(master, width=30, textvariable=self.totalCapital).pack()


        self.targetPercent = StringVar()
        Spinbox(master, from_ = 5, to = 25, textvariable=self.targetPercent).pack()



    def execute(self):

        print(self.pricePoint.get())
        print(self.targetPercent.get())
        pass

def main():

    root = Tk()
    app = MainWindow(root)
    root.mainloop()

    print(frame.targetPercent)



if __name__ == "__main__": main()
