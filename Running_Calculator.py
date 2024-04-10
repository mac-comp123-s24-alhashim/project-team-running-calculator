from Input_Conversions import *
from Lap_Splits_Output import *
import tkinter as tk


class First_Window_GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.userMinPace = tk.StringVar()
        self.userSecPace = tk.StringVar()
        self.userDistance = tk.StringVar


    def createWidgets(self):
        self.root.title('Running Calculator')

        welcome = tk.Label(master=self.root, text="Tyler and Noah's Running Calculator",
                           font='Arial 20 bold', bd=10, relief='groove')
        welcome.grid(row=0, columnspan=12)

        instruction_1 = tk.Label(master=self.root, text="Fill in 2 of the below cells",
                                 font='Arial 10', bd=5, relief='groove')
        instruction_1.grid(row=1, column=4, columnspan=4)

        time = tk.Label(master=self.root, text="Time:",
                              font='Arial 15', bd=5, relief='groove')
        time.grid(row=2, column=0, columnspan=4, pady=10)

        distance = tk.Label(master=self.root, text="Distance:",
                              font='Arial 15', bd=5, relief='groove')
        distance.grid(row=3, column=0, columnspan=4, pady=10)

        pace = tk.Label(master=self.root, text="Pace:",
                                  font='Arial 15', bd=5, relief='groove')
        pace.grid(row=4, column=0, columnspan=4, pady=10)

        distance_input = tk.Entry(textvariable=self.userDistance, font='Arial 16', bd=1,
                               exportselection=0, width=25, justify='center')
        distance_input.grid(row=3, column=4)








    def goProgram(self):
        self.root.mainloop()






if __name__ == '__main__':
    s = First_Window_GUI()
    s.createWidgets()
    s.goProgram()
    print('back to main')
