from Input_Conversions import *
from Lap_Splits_Output import *

import tkinter as tk


class First_Window_GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.userMinPace = tk.StringVar()
        self.userSecPace = tk.StringVar()
        self.userDistance = tk.StringVar()
    



    def createWidgets(self):
        self.root.title('Running Calculator')

        welcome = tk.Label(master=self.root, text="Tyler and Noah's Running Calculator",
                           font='Arial 20 bold', bd=10, relief='groove')
        welcome.grid(row=0, columnspan=12)

        instruction_1 = tk.Label(master=self.root, text="Fill in 2 of the below cells",
                                 font='Arial 10', bd=5, relief='groove')
        instruction_1.grid(row=1, column=2, columnspan=4)

        time_frame = tk.Frame(self.root, bg="black", bd=1,
                              relief='groove', padx=0, pady=0)
        time_frame.grid(row=2, column=4)
        time_label = tk.Label(master=self.root, text="Time:",
                        font='Arial 15', bd=5, relief='groove')
        time_label.grid(row=2, column=0, columnspan=4, pady=10)
        time_hour_entry = tk.Entry(time_frame, width=6, justify='center')
        time_hour_entry.grid(row=2, column= 5, padx=5, pady=1)
        time_min_entry = tk.Entry(time_frame, width=6, justify='center')
        time_min_entry.grid(row=2, column=6, padx=5, pady=1)
        time_sec_entry = tk.Entry(time_frame, width=6, justify='center')
        time_sec_entry.grid(row=2, column=7, padx=5, pady=1)

        distance_frame = tk.Frame(self.root, bg = "black", bd=1,
                                  relief='groove', padx=0, pady=0)
        distance_frame.grid(row=3, column=4)
        distance_label = tk.Label(master=self.root, text="Distance:",
                            font='Arial 15', bd=5, relief='groove')
        distance_label.grid(row=3, column=0, columnspan=4, pady=10)
        distance_entry = tk.Entry(distance_frame, width=20, justify='center')
        distance_entry.grid(row=3, column=1, padx=5, pady=1)
        distance_mi_button = tk.Checkbutton(distance_frame, text="mi", onvalue='yes', offvalue='no', font='Arial 14')
        distance_mi_button.grid(row=2, column = 5)
        distance_km_button = tk.Checkbutton(distance_frame, text="km", onvalue='yes', offvalue='no', font='Arial 14')
        distance_km_button.grid(row=3, column = 5)
        distance_m_button = tk.Checkbutton(distance_frame, text="m", onvalue='yes', offvalue='no', font='Arial 14')
        distance_m_button.grid(row=4, column = 5)

        pace_frame = tk.Frame(self.root, bg="black", bd=1,
                              relief='groove', padx=0, pady=0)
        pace_frame.grid(row=4, column=4)
        pace = tk.Label(master=self.root, text="Pace:",
                        font='Arial 15', bd=5, relief='groove')
        pace.grid(row=4, column=0, columnspan=4, pady=10)
        pace_min_entry = tk.Entry(pace_frame, width=10, justify='center')
        pace_min_entry.grid(row=4, column=3, padx=5, pady=1)
        pace_sec_entry = tk.Entry(pace_frame, width=10, justify='center')
        pace_sec_entry.grid(row=4, column=4, padx=5, pady=1)
        pace_per_mi_button = tk.Checkbutton(pace_frame, text="per mi", onvalue='yes', offvalue='no', font='Arial 14')
        pace_per_mi_button.grid(row = 3, column = 5)
        pace_per_km_button = tk.Checkbutton(pace_frame, text="per km", onvalue='yes', offvalue='no', font='Arial 14')
        pace_per_km_button.grid(row=4, column=5)





    def goProgram(self):
        self.root.mainloop()


"""
Amin said to try using the Frame widget. It puts a grid that we can manipulate within the tkinter grid.
Could help us center stuff.
Also said we could download Bootstrap to make it look nicer. Says the commands are all the same, but 
I don't think we need that.
"""



if __name__ == '__main__':
    s = First_Window_GUI()
    s.createWidgets()
    s.goProgram()
    print('back to main')
