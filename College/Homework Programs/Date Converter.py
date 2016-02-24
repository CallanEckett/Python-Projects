import tkinter as tk
from tkinter import messagebox

class Application(tk.Tk):
    def __init__(self, master=None):
        tk.Tk.__init__(self, master)
        self.title("Date Converter")

        self.create()

    def create(self):
        self.dLabel = tk.Label(self, text="Input Date in Format dd/mm/yyyy").grid(row=0, column=0)
        self.dEntry = tk.Entry(self, width=10)
        self.dButton = tk.Button(self, text="Convert Date", command=self.convert).grid(row=0, column=2)

        self.dEntry.grid(row=0, column=1)

    def convert(self):
        if len(self.dEntry.get()) < 10 or len(self.dEntry.get()) > 10:
            self.error = tk.messagebox.showerror("Error", "Please enter the date correctly")
        else:
            self.days = self.dEntry.get()[:2]
            self.months = self.dEntry.get()[3:5]
            self.years = self.dEntry.get()[6:]

            self.message = tk.messagebox.showinfo("Converted", str(self.months) + "/" + str(self.days) + "/" + str(self.years))

if __name__ == '__main__':
    App = Application()
    App.mainloop()