from Input_Conversions import *
from Lap_Splits_Output import *

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from datetime import timedelta
from PIL import Image, ImageTk
from tkinter import messagebox

"""
Things we MUST do:

fix look of first GUI
Add track image/type of track selected in 2nd GUI -> added image (still need to add text inside oval)


Things we WANT to add:
indor mile specification (add extra time of 8m to first lap)
Try to make it look nicer/more readable (started to do this slightly)



"""


class first_Window_GUI:
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

        self.displayLaps = ttk.StringVar()
        self.trackType = ttk.StringVar()






    def createWidgets(self):
        self.root.title('Running Calculator')

        self.welcome = ttk.Label(master=self.root,
                                 text="Tyler and Noah's Running Calculator", font='Arial 20 bold')
        self.welcome.grid(row=0, column = 0, columnspan=12)

        self.instruction_1 = ttk.Label(master=self.root,
                                       text="Fill in 2 of the below cells", font='Arial 10')
        self.instruction_1.grid(row=1, column=0, columnspan=4)

        self.time_frame = ttk.Frame(self.root)
        self.time_frame.grid(row=2, column=0)
        self.time_label = ttk.Label(master=self.time_frame,
                                    text="Time:", font='Arial 15')
        self.time_label.grid(row=0, column=0, columnspan=4, padx=5)
        self.time_hour_entry = ttk.Entry(self.time_frame,
                                         textvariable=self.userHourTime, width=6, justify='center')
        self.time_hour_entry.grid(row=0, column= 6, padx=5)
        self.time_min_entry = ttk.Entry(self.time_frame,
                                        textvariable=self.userMinTime, width=6, justify='center')
        self.time_min_entry.grid(row=0, column=7, padx=5)
        self.time_sec_entry = ttk.Entry(self.time_frame,
                                        textvariable=self.userSecTime, width=6, justify='center')
        self.time_sec_entry.grid(row=0, column=8, padx=5)

        self.distance_frame = ttk.Frame(self.root)
        self.distance_frame.grid(row=3, column=0)
        self.distance_label = ttk.Label(master=self.distance_frame,
                                        text="Distance:", font='Arial 15')
        self.distance_label.grid(row=2, column=0, columnspan=4, padx=5)
        self.distance_entry = ttk.Entry(self.distance_frame,
                                        textvariable=self.userDistance, width=20, justify='center')
        self.distance_entry.grid(row=2, column=6, padx=5)
        self.distance_mi_button = ttk.Checkbutton(self.distance_frame,
                                                  text="mi", variable=self.distanceUnits, onvalue='mi')
        self.distance_mi_button.grid(row=1, column=7)
        self.distance_km_button = ttk.Checkbutton(self.distance_frame,
                                                  text="km", variable=self.distanceUnits, onvalue='km')
        self.distance_km_button.grid(row=2, column=7)
        self.distance_m_button = ttk.Checkbutton(self.distance_frame,
                                                 text="m", variable=self.distanceUnits, onvalue='m')
        self.distance_m_button.grid(row=3, column=7)
        self.distance_mi_button.state(['selected'])

        self.pace_frame = ttk.Frame(self.root)
        self.pace_frame.grid(row=4, column=0)
        self.pace = ttk.Label(master=self.pace_frame,
                              text="Pace:", font='Arial 15')
        self.pace.grid(row=1, column=0, columnspan=4, padx=5)
        self.pace_min_entry = ttk.Entry(self.pace_frame,
                                        textvariable= self.userMinPace, width=10, justify='center')
        self.pace_min_entry.grid(row=1, column=6, padx=5)
        self.pace_sec_entry = ttk.Entry(self.pace_frame,
                                        textvariable=self.userSecPace, width=10, justify='center')
        self.pace_sec_entry.grid(row=1, column=7, padx=5)
        self.pace_per_mi_button = ttk.Checkbutton(self.pace_frame,
                                                  text="per mi", variable=self.paceUnits,
                                                  onvalue='per mi', offvalue='per km')
        self.pace_per_mi_button.grid(row=0, column=8)
        self.pace_per_km_button = ttk.Checkbutton(self.pace_frame,
                                                  text="per km",variable=self.paceUnits,
                                                  onvalue='per km', offvalue='per mi')
        self.pace_per_km_button.grid(row=1, column=8)
        self.pace_per_mi_button.state(['selected'])

        self.display_laps_frame = ttk.Frame(self.root)
        self.display_seperator = ttk.Separator(master=self.display_laps_frame,
                                               orient = 'horizontal')
        self.display_seperator.grid(row=3, column = 0, columnspan=5, sticky = EW)
        self.display_laps_frame.grid(row=5, column=0)
        self.display_lap_splits = ttk.Label(master= self.display_laps_frame,
                                            text="Display lap splits?", font='Arial 15')
        self.display_lap_splits.grid(row=4, column=1, padx=5, pady=1)
        self.display_yes = ttk.Checkbutton(self.display_laps_frame,
                                           text="Yes",variable=self.displayLaps,
                                           onvalue='Yes', offvalue='No')
        self.display_yes.grid(row = 4, column = 2)
        self.display_no = ttk.Checkbutton(self.display_laps_frame,
                                          text="No",variable=self.displayLaps,
                                          onvalue='No', offvalue='Yes')
        self.display_no.grid(row= 4, column = 3)
        self.if_select_indoor_label = ttk.Label(master= self.display_laps_frame,
                                                text="If select indoor: Max distance = 5000m",
                                                font='Arial 7')
        self.if_select_indoor_label.grid(row = 5, column =2)
        self.if_select_outdoor_label = ttk.Label(master= self.display_laps_frame,
                                                 text="If select outdoor: Max distance = 10000m",
                                                 font='Arial 7')
        self.if_select_outdoor_label.grid(row=5, column =3)
        self.indoor_button = ttk.Checkbutton(self.display_laps_frame,
                                             text= "Indoor", variable =self.trackType,
                                             onvalue='Indoor', offvalue='Outdoor')
        self.indoor_button.grid(row=6, column = 2)
        self.outdoor_button = ttk.Checkbutton(self.display_laps_frame,
                                              text= "Outdoor", variable =self.trackType,
                                              onvalue='Outdoor', offvalue='Indoor')
        self.outdoor_button.grid(row=6, column = 3)

        self.submitButton = ttk.Button(self.root,
                                       text="Submit", command=self.calculations)
        self.submitButton.grid(row=20, column=5)

    def calculations(self):
        hourTime = self.userHourTime.get()
        if hourTime == '':
            hourTime = 0
        else:
            hourTime = int(hourTime)

        minTime = self.userMinTime.get()
        if minTime == '':
            minTime = 0
        else:
            minTime = int(minTime)

        secTime = self.userSecTime.get()
        if secTime == '':
            secTime = 0
        else:
            secTime = int(secTime)

        distance = self.userDistance.get()
        if distance == '':
            distance = 0
        else:
            distance = int(distance)

        distanceUnits = self.distanceUnits.get()

        minPace = self.userMinPace.get()
        if minPace == '':
            minPace = 0
        else:
            minPace = int(minPace)

        secPace = self.userSecPace.get()
        if secPace == '':
            secPace = 0
        else:
            secPace = int(secPace)

        paceUnits = self.paceUnits.get()

        displaylaps = self.displayLaps.get()
        tracktype = self.trackType.get()
        final_time_sec = 0
        final_distance = 0
        final_pace_sec = 0
        final_distance_meters = 0
        pace_in_sec_per_km = 0

        if hourTime + minTime + secTime == 0:
            distance = float(distance)
            distance_in_meters = distance_convert(distance, distanceUnits)
            pace_in_sec_per_km = pace_convert(minPace, secPace, paceUnits)
            final_time_sec = (pace_in_sec_per_km * (distance_in_meters / 1000))
            final_distance = distance
            final_pace_sec = pace_in_sec_per_km

        if distance == 0:
            pace_in_sec_per_km = pace_convert(minPace, secPace, paceUnits)
            time_in_sec = time_convert(hourTime, minTime, secTime)
            final_distance = ''
            if distanceUnits == "mi":
                final_distance = (time_in_sec / (pace_in_sec_per_km * 1.609344))
            elif distanceUnits == "km":
                final_distance = time_in_sec / pace_in_sec_per_km
            elif distanceUnits == "m":
                final_distance = (time_in_sec / (pace_in_sec_per_km / 1000))
            final_pace_sec = pace_in_sec_per_km
            final_time_sec = time_in_sec
            distance_in_meters = final_distance


        if minPace + secPace == 0:
            distance = float(distance)
            distance_in_meters = distance_convert(distance, distanceUnits)
            time_in_sec = time_convert(hourTime, minTime, secTime)
            if paceUnits == "per mi":
                final_pace_sec = time_in_sec / (distance_in_meters / 1609.344)
                pace_in_sec_per_km = time_in_sec / (distance_in_meters / 1000)
            elif paceUnits == "per km":
                final_pace_sec = time_in_sec / (distance_in_meters / 1000)
                pace_in_sec_per_km = final_pace_sec
            final_distance_meters = distance_in_meters
            final_distance = distance
            final_time_sec = time_in_sec

        if final_distance_meters > 10000 and tracktype == "Outdoor" and displaylaps == "Yes":
            messagebox.showwarning("showerror", "Distance must be less than 10,000m")#won't run if miles is selected first time

        if final_distance_meters > 5000 and tracktype == "Indoor" and displaylaps == "Yes":
            messagebox.showwarning("showerror", "Distance must be less than 5,000m")#won't run if miles is selected first time

        final_time = timedelta(seconds=final_time_sec)
        final_time = str(final_time - timedelta(microseconds=final_time.microseconds))
        final_pace = timedelta(seconds=final_pace_sec)
        final_pace = str(final_pace - timedelta(microseconds=final_pace.microseconds))

        if displaylaps == 'Yes':
            numberlaps = num_laps(distance_in_meters, tracktype)
            splits = int(even_lap_splits(numberlaps, final_time_sec))
            laps = int(numberlaps)


        self.root.withdraw()

        self.main = ttk.Toplevel()
        self.main.title('Running Calculator')
        self.welcome = ttk.Label(master=self.main,
                                 text="Tyler and Noah's Running Calculator", font='Arial 20 bold')
        self.welcome.grid(row=0, column=0, columnspan=12)

        self.time_frame = ttk.Frame(self.main)
        self.time_frame.grid(row=2, column=0)
        self.time_label = ttk.Label(master=self.time_frame,
                                    text="Time:", font='Arial 15')
        self.time_label.grid(row=0, column=0, columnspan=4, padx=5)
        self.time_label2 = ttk.Label(master = self.time_frame,
                                     text= final_time, font='Arial 15')
        self.time_label2.grid(row=0, column=6, padx=5)

        self.distance_frame = ttk.Frame(self.main)
        self.distance_frame.grid(row=3, column=0)
        self.distance_label = ttk.Label(master=self.distance_frame,
                                        text="Distance:", font='Arial 15')
        self.distance_label.grid(row=2, column=0, columnspan=4, padx=5)
        self.distance_2 = ttk.Label(master = self.distance_frame,
                                    text= final_distance, font='Arial 15')
        self.distance_2.grid(row=2, column=6, padx=5)
        self.distance_3 = ttk.Label(self.distance_frame,
                                    text=distanceUnits, font='Arial 15')
        self.distance_3.grid(row=2, column=7)

        self.pace_frame = ttk.Frame(self.main)
        self.pace_frame.grid(row=4, column=0)
        self.pace = ttk.Label(master=self.pace_frame,
                              text="Pace:", font='Arial 15')
        self.pace.grid(row=1, column=0, columnspan=4, padx=5)
        self.pace2 = ttk.Label(master=self.pace_frame,
                               text= final_pace, font='Arial 15')
        self.pace2.grid(row=1, column=6, padx=5)
        self.pace3 = ttk.Label(master=self.pace_frame,
                               text= paceUnits, font='Arial 15')
        self.pace3.grid(row=1, column=7, padx=5)

        self.splits_frame = ttk.Labelframe(self.main)
        self.splits_frame.grid(row=6, column=0)

        lapsCol = 1
        lapsRow = 1
        total = timedelta(seconds =0)
        non_whole_distance = 0

        if displaylaps == "Yes":
            non_whole_split = round(pace_in_sec_per_km * (non_whole_distance / 1000), 2)
            non_whole_laps = round(numberlaps - laps, 2)
            if tracktype == "Outdoor":
                non_whole_distance = final_distance_meters - (400 * laps)
            if tracktype == "Indoor":
                non_whole_distance = final_distance_meters - (200 * laps)


        self.splitsDisplay = []

        if displaylaps == "Yes":
            for i in range(1, laps + 1):
                if i != 0 and i % 5 == 0:
                    splits_label = ttk.Label(self.splits_frame,
                                            text = "Lap" +  ":" +" " + str(i)+
                                                " " + "+" + str(splits) + " " + "sec")
                    splits_label.grid(row = lapsRow, column = lapsCol, padx=10, pady=10)
                    self.splitsDisplay.append(splits_label)
                    total = total + timedelta(seconds=splits)
                    total_label = ttk.Label(self.splits_frame, text= str(total))
                    total_label.grid(row=lapsRow+1, column=lapsCol, padx=10, pady=10)
                    lapsCol = lapsCol + 2
                    lapsRow = 1
                else:
                    splits_label = ttk.Label(self.splits_frame, text= "Lap" + ":" + " " + str(i) + " " +
                                                                  "+" + str(splits) + " " + "sec")
                    splits_label.grid(row=lapsRow, column=lapsCol, padx=10, pady=10)
                    self.splitsDisplay.append(splits_label)
                    total = total + timedelta(seconds=splits)
                    total_label = ttk.Label(self.splits_frame, text=str(total))
                    total_label.grid(row=lapsRow+1, column=lapsCol, padx=10, pady=10)
                    lapsRow = lapsRow + 2

            if non_whole_laps != 0:
                non_whole_label= ttk.Label(self.splits_frame, text= "Lap" + ":" + " " +
                                                                str(laps+non_whole_laps)+ " " +
                                                                "+" + str(non_whole_split) + " " + "sec")
                non_whole_label.grid(row=lapsRow, column=lapsCol, padx=10, pady=10)
                total = total + timedelta(seconds=non_whole_split)
                total_label1 = ttk.Label(self.splits_frame, text=str(total))
                total_label1.grid(row=lapsRow + 1, column=lapsCol, padx=10, pady=10)

            trackImage = ImageTk.PhotoImage(file="Track.jpeg")
            imageLabel = ttk.Label(self.main, image=trackImage)
            imageLabel.grid(row=5, column = 0, padx=0, pady = 0)

        #trackImage = ImageTk.PhotoImage(file="Indoor_track.jpg")
        #imageLabel = ttk.Label(self.main, image=trackImage)
        #imageLabel.grid(row=5, column=0, padx=0, pady=0)



        self.main.mainloop()


    def goProgram(self):
        self.root.mainloop()




if __name__ == '__main__':
    s = first_Window_GUI()
    s.createWidgets()
    s.goProgram()

    print('back to main')
