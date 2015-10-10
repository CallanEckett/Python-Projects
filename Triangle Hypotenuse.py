import tkinter as tk
from tkinter import messagebox
import math

class Application(tk.Tk):
    def __init__(self, master=None):
        tk.Tk.__init__(self, master)
        self.title("Triangle Hypotenuse Calculator")
        self.create()

    def create(self):
        self.aLabel = tk.Label(self, text="A Value:").grid(row=0, column=0)
        self.bLabel = tk.Label(self, text="B Value:").grid(row=1, column=0)
        self.aEntry = tk.Entry(self, width=3)
        self.bEntry = tk.Entry(self, width=3)

        self.calcButton = tk.Button(self, text="Calculate Hypotenuse", command=self.calculator).grid(row=2, column=0, columnspan=3)

        self.aEntry.grid(row=0, column=1, padx=2)
        self.bEntry.grid(row=1, column=1, padx=2)

    def calculator(self):
        try:
            self.aValue = float(self.aEntry.get())
            self.bValue = float(self.bEntry.get())

            self.hValue = math.sqrt((self.aValue**2)+(self.bValue**2))
            self.message = tk.messagebox.showinfo("Calculation", "Triange Hypotenuse: {0:.2f}".format(self.hValue))
        except:
            self.error = tk.messagebox.showerror("Error", "Please enter valid information")


if __name__ == '__main__':
    App = Application()
    App.mainloop()