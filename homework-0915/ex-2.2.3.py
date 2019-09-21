start_time_secs = 24720
ez_pace = 495
tempo_pace = 432
ez_miles = 2
tempo_miles = 3
ez_time = ez_pace * ez_miles
tempo_time = tempo_pace * tempo_miles
total_time = ez_time + tempo_time
finish_time = start_time_secs + total_time
finish_time_hours = finish_time // 3600
finish_time_mins = finish_time % 3600 // 60
finish_time_secs = finish_time % 3600 % 60
print("I got home for breakfast at " + str(finish_time_hours) + ":" + str(finish_time_mins) + ":" + str(finish_time_secs) + " AM")