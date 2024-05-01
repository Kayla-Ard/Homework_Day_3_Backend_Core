# Python Lists Transformation - Task 1: Given the list of grades
# Sort the grades in descending order and display the sorted list

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(grades)



# Python Lists Transformation - Task 2: Calculate the average grade and display it

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades_sum = sum(grades)
average_grade = grades_sum / len(grades)
print(f"The average grade is {average_grade}.")



# Advanced List Methods and Identity Operators - Task 1: Given the two lists
# Find out which students both submitted their assignments and attended the class

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
good_students = [name for name in submitted if name in attended]
print(good_students)



# Advanced Slicing Techniques - Task 1: Given the list of temperatures
# Extract the temperatures for the second week (7 days) of the month (index 7 to index 14)
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
print(temperatures[7:14])



# Advanced Slicing Techniques - Task 2: Extract all the temperatures above 100. **hint** add the temperatures over 100 to a new list
# Extract all the temperatures above 100

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
hot_temps = []
for temp in temperatures:
    if temp >= 100:
        hot_temps.append(temp)
print(hot_temps)