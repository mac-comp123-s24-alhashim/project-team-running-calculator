from Input_Conversions import *


def time_output(pace_input_minutes, pace_input_seconds, units_input_pace, distance_input, units_input_distance):
    distance = distance_convert(distance_input, units_input_distance)
    pace = pace_convert(pace_input_minutes, pace_input_seconds, units_input_pace)
    final_time_seconds = distance / pace
    return final_time_seconds


if __name__ == "__main__":
    print(time_output(1, 1, "per mi", 1, "mi"))
