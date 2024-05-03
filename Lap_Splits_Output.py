"""
@author: Tyler Edwards (tedward1@macalester.edu)
@author: Noah Koch (nkoch1@macalester.edu)

These functions calculate the lap splits and are called in our main file. (Running_Calculator.py)
"""


from Input_Conversions import *


def num_laps(distance_meters, track_type):
    if track_type == "Outdoor":
        lap_num = distance_meters / 400
    elif track_type == "Indoor":
        lap_num = distance_meters / 200
    if lap_num > 25:
        return False
    return lap_num


def even_lap_splits(lap_num, total_time):
    splits = total_time / lap_num
    return splits


if __name__ == "__main__":
    distance = distance_convert(1609, "m")
    lap_num = num_laps(distance, "Indoor")
    print(even_lap_splits(lap_num, 300))

