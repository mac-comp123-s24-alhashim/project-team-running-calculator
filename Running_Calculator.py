from Input_Conversions import *
from Lap_Splits_Output import *

import tkinter as tk


class First_Window_GUI:
    def __init__(self):
        self.root = tk.Tk()

        self.userHourTime = tk.StringVar()
        self.userMinTime = tk.StringVar()
        self.userSecTime = tk.StringVar()

        self.userDistance = tk.StringVar()
        self.distanceUnitsMi = tk.StringVar()
        self.distanceUnitsKm = tk.StringVar()
        self.distanceUnitsM = tk.StringVar()

        self.userMinPace = tk.StringVar()
        self.userSecPace = tk.StringVar()
        self.paceUnitsMi = tk.StringVar()
        self.paceUnitsKm = tk.StringVar()



    def createWidgets(self):
        self.root.title('Running Calculator')

        self.welcome = tk.Label(master=self.root, text="Tyler and Noah's Running Calculator",
                           font='Arial 20 bold', bd=10, relief='groove')
        self.welcome.grid(row=0, columnspan=12)

        self.instruction_1 = tk.Label(master=self.root, text="Fill in 2 of the below cells",
                                 font='Arial 10', bd=5, relief='groove')
        self.instruction_1.grid(row=1, column=2, columnspan=4)

        self.time_frame = tk.Frame(self.root, bg="black", bd=1,
                              relief='groove', padx=0, pady=0)
        self.time_frame.grid(row=2, column=4)
        self.time_label = tk.Label(master=self.root, text="Time:",
                        font='Arial 15', bd=5, relief='groove')
        self.time_label.grid(row=2, column=0, columnspan=4, pady=10)
        self.time_hour_entry = tk.Entry(self.time_frame, textvariable=self.userHourTime, width=6, justify='center')
        self.time_hour_entry.grid(row=2, column= 5, padx=5, pady=1)
        self.time_min_entry = tk.Entry(self.time_frame, textvariable= self.userMinTime, width=6, justify='center')
        self.time_min_entry.grid(row=2, column=6, padx=5, pady=1)
        self.time_sec_entry = tk.Entry(self.time_frame,textvariable= self.userSecTime, width=6, justify='center')
        self.time_sec_entry.grid(row=2, column=7, padx=5, pady=1)

        self.distance_frame = tk.Frame(self.root, bg = "black", bd=1,
                                  relief='groove', padx=0, pady=0)
        self.distance_frame.grid(row=3, column=4)
        self.distance_label = tk.Label(master=self.root, text="Distance:",
                            font='Arial 15', bd=5, relief='groove')
        self.distance_label.grid(row=3, column=0, columnspan=4, pady=10)
        self.distance_entry = tk.Entry(self.distance_frame, textvariable= self.userDistance, width=20, justify='center')
        self.distance_entry.grid(row=3, column=1, padx=5, pady=1)
        self.distance_mi_button = tk.Checkbutton(self.distance_frame, text="mi", variable=self.distanceUnitsMi, onvalue='yes', offvalue='no', font='Arial 14')
        self.distance_mi_button.grid(row=2, column=5)
        self.distance_km_button = tk.Checkbutton(self.distance_frame, text="km", variable=self.distanceUnitsKm, onvalue='yes', offvalue='no', font='Arial 14')
        self.distance_km_button.grid(row=3, column=5)
        self.distance_m_button = tk.Checkbutton(self.distance_frame, text="m", variable=self.distanceUnitsM, onvalue='yes', offvalue='no', font='Arial 14')
        self.distance_m_button.grid(row=4, column=5)
        self.distance_mi_button.select()
        self.distance_km_button.deselect()
        self.distance_m_button.deselect()

        self.pace_frame = tk.Frame(self.root, bg="black", bd=1,
                              relief='groove', padx=0, pady=0)
        self.pace_frame.grid(row=4, column=4)
        self.pace = tk.Label(master=self.root, text="Pace:",
                        font='Arial 15', bd=5, relief='groove')
        self.pace.grid(row=4, column=0, columnspan=4, pady=10)
        self.pace_min_entry = tk.Entry(self.pace_frame, textvariable= self.userMinPace, width=10, justify='center')
        self.pace_min_entry.grid(row=4, column=3, padx=5, pady=1)
        self.pace_sec_entry = tk.Entry(self.pace_frame,textvariable=self.userSecPace, width=10, justify='center')
        self.pace_sec_entry.grid(row=4, column=4, padx=5, pady=1)
        self.pace_per_mi_button = tk.Checkbutton(self.pace_frame, text="per mi", variable=self.paceUnitsMi, onvalue='yes', offvalue='no', font='Arial 14')
        self.pace_per_mi_button.grid(row=3, column=5)
        self.pace_per_km_button = tk.Checkbutton(self.pace_frame, text="per km",variable=self.paceUnitsKm, onvalue='yes', offvalue='no', font='Arial 14')
        self.pace_per_km_button.grid(row=4, column=5)
        self.pace_per_mi_button.select()
        self.pace_per_km_button.deselect()

        def calculations(self):
            hourTime = self.userHourTime.get()
            minTime = self.userMinTime.get()
            secTime = self.userSecTime.get()

            distance = self.userDistance.get()
            distanceUnitsMi = self.distanceUnitsMi.get()
            distanceUnitsKm = self.distanceUnitsKm.get()
            distanceUnitsM = self.distanceUnitsM.get()

            minPace = self.userMinPace.get()
            secPace = self.userSecPace.get()
            paceUnitsMi = self.paceUnitsMi.get()
            paceUnitsKm = self.paceUnitsKm.get()

            if hourTime and minTime and secTime == "":







    def goProgram(self):
        self.root.mainloop()


"""
Amin said to try using the Frame widget. It puts a grid that we can manipulate within the tkinter grid.


4/16:
i added tk.stringvar to all of the entry and button widgets so we can start doing calculations  


"""



if __name__ == '__main__':
    s = First_Window_GUI()
    s.createWidgets()
    s.goProgram()
    print('back to main')
