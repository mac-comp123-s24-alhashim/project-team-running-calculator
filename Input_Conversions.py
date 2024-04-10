def time_convert(hour_input, minute_input, seconds_input):
    hours = int(hour_input)
    minutes = int(minute_input)
    seconds = int(seconds_input)
    hours_in_seconds = hours * 3600
    minutes_in_seconds = minutes * 60
    total_inputted_time_in_seconds = hours_in_seconds + minutes_in_seconds + seconds
    return total_inputted_time_in_seconds


def distance_convert(distance_input, units_input_distance):
    distance_final_meters = distance_input
    if units_input_distance == "mi":
        distance_final_meters = distance_input * 1609.344
    elif units_input_distance == "km":
        distance_final_meters = distance_input * 1000
    elif units_input_distance == "m":
        distance_final_meters = distance_input
    return distance_final_meters


def pace_convert(pace_input_minutes, pace_input_seconds, units_input_pace):
    pace_in_seconds_per_km = time_convert(0, pace_input_minutes, pace_input_seconds)
    if units_input_pace == "per mi":
        pace_in_seconds_per_km = pace_in_seconds_per_km * 0.62137119223733
    if units_input_pace == "per km":
        pace_in_seconds_per_km = pace_in_seconds_per_km
    return pace_in_seconds_per_km



if __name__ == "__main__":
    print(pace_convert(4,30, "per mi"))


