from Input_Conversions import *
from Lap_Splits_Output import *

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class First_Window_GUI:
    def __init__(self):
        self.root = ttk.Window(themename="flatly")

        self.userHourTime = ttk.StringVar()
        self.userMinTime = ttk.StringVar()
        self.userSecTime = ttk.StringVar()

        self.userDistance = ttk.StringVar()
        self.distanceUnits = ttk.StringVar()

        self.userMinPace = ttk.StringVar()
        self.userSecPace = ttk.StringVar()
        self.paceUnits = ttk.StringVar()

        self.displaylaps = ttk.StringVar()
        self.tracktype = ttk.StringVar()

    def createWidgets(self):
        self.root.title('Running Calculator')

        self.welcome = ttk.Label(master=self.root, text="Tyler and Noah's Running Calculator", font='Arial 20 bold')
        self.welcome.grid(row=0, column = 0, columnspan=12)

        self.instruction_1 = ttk.Label(master=self.root, text="Fill in 2 of the below cells", font='Arial 10')
        self.instruction_1.grid(row=1, column=0, columnspan=4)

        self.time_frame = ttk.Frame(self.root)
        self.time_frame.grid(row=2, column=0)
        self.time_label = ttk.Label(master=self.time_frame, text="Time:", font='Arial 15')
        self.time_label.grid(row=0, column=0, columnspan=4, padx=5)
        self.time_hour_entry = ttk.Entry(self.time_frame, textvariable=self.userHourTime, width=6, justify='center')
        self.time_hour_entry.grid(row=0, column= 6, padx=5)
        self.time_min_entry = ttk.Entry(self.time_frame, textvariable=self.userMinTime, width=6, justify='center')
        self.time_min_entry.grid(row=0, column=7, padx=5)
        self.time_sec_entry = ttk.Entry(self.time_frame,textvariable=self.userSecTime, width=6, justify='center')
        self.time_sec_entry.grid(row=0, column=8, padx=5)

        self.distance_frame = ttk.Frame(self.root)
        self.distance_frame.grid(row=3, column=0)
        self.distance_label = ttk.Label(master=self.distance_frame, text="Distance:", font='Arial 15')
        self.distance_label.grid(row=2, column=0, columnspan=4, padx=5)
        self.distance_entry = ttk.Entry(self.distance_frame, textvariable=self.userDistance, width=20, justify='center')
        self.distance_entry.grid(row=2, column=6, padx=5)
        self.distance_mi_button = ttk.Checkbutton(self.distance_frame, text="mi", variable=self.distanceUnits, onvalue='mi')
        self.distance_mi_button.grid(row=1, column=7)
        self.distance_km_button = ttk.Checkbutton(self.distance_frame, text="km", variable=self.distanceUnits, onvalue='km')
        self.distance_km_button.grid(row=2, column=7)
        self.distance_m_button = ttk.Checkbutton(self.distance_frame, text="m", variable=self.distanceUnits, onvalue='m')
        self.distance_m_button.grid(row=3, column=7)

        self.pace_frame = ttk.Frame(self.root)
        self.pace_frame.grid(row=4, column=0)
        self.pace = ttk.Label(master=self.pace_frame, text="Pace:", font='Arial 15')
        self.pace.grid(row=1, column=0, columnspan=4, padx=5)
        self.pace_min_entry = ttk.Entry(self.pace_frame, textvariable= self.userMinPace, width=10, justify='center')
        self.pace_min_entry.grid(row=1, column=6, padx=5)
        self.pace_sec_entry = ttk.Entry(self.pace_frame,textvariable=self.userSecPace, width=10, justify='center')
        self.pace_sec_entry.grid(row=1, column=7, padx=5)
        self.pace_per_mi_button = ttk.Checkbutton(self.pace_frame, text="per mi", variable=self.paceUnits, onvalue='per mi', offvalue='per km')
        self.pace_per_mi_button.grid(row=0, column=8)
        self.pace_per_km_button = ttk.Checkbutton(self.pace_frame, text="per km",variable=self.paceUnits, onvalue='per km', offvalue='per mi')
        self.pace_per_km_button.grid(row=1, column=8)


        self.display_laps_frame = ttk.Frame(self.root)
        self.display_seperator = ttk.Separator(master=self.display_laps_frame, orient = 'horizontal')
        self.display_seperator.grid(row=3, column = 0, columnspan=5, sticky = EW)
        self.display_laps_frame.grid(row=5, column=0)
        self.display_lap_splits = ttk.Label(master= self.display_laps_frame, text="Display lap splits?", font='Arial 15')
        self.display_lap_splits.grid(row=4, column=1, padx=5, pady=1)
        self.display_yes = ttk.Checkbutton(self.display_laps_frame, text="Yes",variable=self.displaylaps, onvalue='Yes', offvalue='No')
        self.display_yes.grid(row = 4, column = 2)
        self.display_no = ttk.Checkbutton(self.display_laps_frame, text="No",variable=self.displaylaps, onvalue='No', offvalue='Yes')
        self.display_no.grid(row= 4, column = 3)
        self.if_select_indoor_label = ttk.Label(master= self.display_laps_frame, text="If select indoor: Max distance = 5000m", font='Arial 7')
        self.if_select_indoor_label.grid(row = 5, column =2)
        self.if_select_outdoor_label = ttk.Label(master= self.display_laps_frame, text="If select outdoor: Max distance = 10000m", font='Arial 7')
        self.if_select_outdoor_label.grid(row=5, column =3)
        self.indoor_button = ttk.Checkbutton(self.display_laps_frame, text= "Indoor", variable =self.tracktype, onvalue='Indoor', offvalue='Outdoor')
        self.indoor_button.grid(row=6, column = 3)
        self.outdoor_button = ttk.Checkbutton(self.display_laps_frame, text= "Outdoor", variable =self.tracktype, onvalue='Outdoor', offvalue='Indoor')
        self.outdoor_button.grid(row=6, column = 4)



        self.submitButton = ttk.Button(self.root, text="Submit", command=self.calculations)
        self.submitButton.grid(row=20, column=5)

    def calculations(self):
        hourTime = self.userHourTime.get()
        minTime = self.userMinTime.get()
        secTime = self.userSecTime.get()

        distance = self.userDistance.get()
        distanceUnits = self.distanceUnits.get()

        minPace = self.userMinPace.get()
        secPace = self.userSecPace.get()
        paceUnits = self.paceUnits.get()

        displaylaps = self.displaylaps.get()
        tracktype = self.tracktype.get()

        if hourTime + minTime + secTime == '':
            distance = float(distance)
            distance_in_meters = distance_convert(distance, distanceUnits)
            pace_in_sec_per_km = pace_convert(minPace, secPace, paceUnits)
            final_time_sec = (pace_in_sec_per_km * (distance_in_meters / 1000))
            return final_time_sec

        if distance == '':
            pace_in_sec_per_km = pace_convert(minPace, secPace, paceUnits)
            time_in_sec = time_convert(hourTime, minTime, secTime)
            final_distance = ''
            if distanceUnits == "mi":
                final_distance = (time_in_sec / (pace_in_sec_per_km * 1.609344))
            elif distanceUnits == "km":
                final_distance = time_in_sec / pace_in_sec_per_km
            elif distanceUnits == "m":
                final_distance = (time_in_sec / (pace_in_sec_per_km / 1000))
            return final_distance

        if minPace + secPace == '':
            distance = float(distance)
            distance_in_meters = distance_convert(distance, distanceUnits)
            time_in_sec = time_convert(hourTime, minTime, secTime)
            final_pace_sec = ''
            if paceUnits == "per mi":
                final_pace_sec = time_in_sec / (distance_in_meters / 1609.344)
            elif paceUnits == "per km":
                final_pace_sec = time_in_sec / (distance_in_meters / 1000)
            return final_pace_sec

        if displaylaps == 'Yes':
            numberlaps = num_laps(final_distance, tracktype)
            splits = even_lap_splits(numberlaps, final_time_sec)
            return splits











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
