# The Range Riddle - Task 1: Your Mood Today
# Write a program that prints off different moods for each day of the week. 
# Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". 
# Using the range() function, loop through the days of the week and for each day, randomly select a mood from the list and print it.
# Ensure that your program includes the use of the random module to select the mood.

import random
moods = ["Happy", "Sad", "Mad", "Energetic", "Calm", "Lonely", "Hyper"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for i in range(7):
        print(f"On {days_of_week[i]} I was feeling {random.choice(moods)}.")



# Double Scoop with Nested Loops - Task 1: Your Mood Tracker
# Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week.
# Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day.
# For each time, randomly select a mood from a predefined list and print it.

import random
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times_of_day = ["Morning", "Afternoon", "Evening"]
moods = ["Happy", "Sad", "Mad", "Energetic", "Calm", "Lonely", "Hyper"]
for day in days_of_week:
    for time in times_of_day:
        print(f" On {day} {time} I was {random.choice(moods)}.")