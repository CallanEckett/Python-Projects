import tkinter as tk
from tkinter import messagebox

class Application(tk.Tk):
    def __init__(self, master=None):
        tk.Tk.__init__(self, master)
        self.title("Text Book Price Calculator")

        self.create()

    def create(self):
        self.tbLabel = tk.Label(self, text="Number of textbooks ordered:").grid(row=0, column=0, sticky=tk.E)
        self.pLabel = tk.Label(self, text="Price of single text book:").grid(row=1, column=0, sticky=tk.E)
        self.tbEntry = tk.Entry(self, width=5)
        self.pEntry = tk.Entry(self, width=5)
        self.button = tk.Button(self, text="Calculate Costs", command=self.calcCosts).grid(row=2, column =0, sticky=tk.E)

        self.tbEntry.grid(row=0, column=1)
        self.pEntry.grid(row=1, column=1)

    def calcCosts(self):
        try:
            self.cost = (float(self.tbEntry.get())*float(self.pEntry.get()))
            self.VAT = (float(self.cost)+(float(self.cost/10)*2))
            self.totalCost = (float(self.VAT)-float(self.VAT/10))

            self.output = tk.messagebox.showinfo("Cost Calculated", "Number of textbooks ordered: " + self.tbEntry.get() +
                                                 ("\nPrice of single textbook: {0:.2f}".format(float(self.pEntry.get())) +
                                                  ("\nPrice of textbooks, ex VAT: {0:.2f}".format(float(self.cost))) +
                                                  ("\nPrice of textbooks, inc VAT: {0:.2f}".format(float(self.VAT))) +
                                                  ("\nPrice of textbooks, inc %10 discount: {0:.2f}".format(float(self.totalCost)))))
        except:
            self.error = tk.messagebox.showerror("Error", "Please Enter the Correct Information")

if __name__ == '__main__':
    App = Application()
    App.mainloop()