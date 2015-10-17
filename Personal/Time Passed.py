import tkinter as tk
from tkinter import messagebox

class Application(tk.Tk):
    def __init__(self, master=None):
        tk.Tk.__init__(self, master)
        self.title("Seconds Passed Calculator")

        self.create()

    def create(self):
        self.tLabel = tk.Label(self, text="Input Time in Form hh:mm:ss").grid(row=0, column=0)
        self.tEntry = tk.Entry(self, width=7)
        self.tButton = tk.Button(self, text="Calculate", command=self.secCalc).grid(row=0, column=2)

        self.tEntry.grid(row=0, column=1)

    def secCalc(self):
        self.hours = ((int(self.tEntry.get()[:2]))*3600)
        self.minute = ((int(self.tEntry.get()[3:5]))*60)
        self.second = int(self.tEntry.get()[6:])

        self.timePassed = (self.hours + self.minute + self.second)
        self.message = tk.messagebox.showinfo("Calculated", "Time Passed Since Midnight: {0} Seconds".format(self.timePassed))

if __name__ == '__main__':
    App = Application()
    App.mainloop()