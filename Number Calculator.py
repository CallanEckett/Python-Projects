import tkinter as tk
from tkinter import messagebox

class Application(tk.Tk):
    def __init__(self, master=None):
        tk.Tk.__init__(self, master)
        self.title("Number Calculator")

        self.create()
        self.numbers = []

    def create(self):
        self.nLabel = tk.Label(self, text="Add 5 Numbers to Calculate Sum & Average").grid(row=0, column=0)
        self.nEntry = tk.Entry(self, width=4)
        self.nButton = tk.Button(self, text="Add Number", command=self.calculator).grid(row=0, column=2)

        self.currentNumbers = tk.Label(self, text="Current Numbers: ")

        self.currentNumbers.grid(row=1, column=0, columnspan=3, sticky=tk.W)
        self.nEntry.grid(row=0, column=1, padx=2)

    def calculator(self):
        self.numbers.append(float(self.nEntry.get()))

        if len(self.numbers) <= 5:

            self.sum = 0
            self.average = 0

            for x in self.numbers:
                self.sum += float(x)
                self.average = (self.sum/5)

                self.currentNumbers.config(text="Current Numbers: " + str(self.numbers))
        else:
            self.message = tk.messagebox.showinfo("Calculation", ("Calculation: Sum of Numbers: {0:.2f}".format(self.sum)) +
                                                  ("\nCalculation: Average of Numbers: {0:.2f}".format(self.average)))
            self.destroy()

if __name__ == '__main__':
    App = Application()
    App.mainloop()