# Python - Advanced DS, Loops Assignment

## Part - B (Q6-Q10)

Question 6: Create the following tuple:

marks = (78, 85, 90, 67, 88)

Write a Python program to:
1. Display the first and last values.
2. Display values from index 1 to 3.
3. Find the highest and lowest marks.
4. Convert the tuple into a list.
5. Add 95 to the list.
6. Convert the updated list back into a tuple

Answer:

Marks = (78, 85, 90, 67, 88)
# 1. Display the first and last values
print(“first value:”, marks[0])
print(“last value:”, marks[-1])

Output:
First value: 78
Last value: 88

# 2. Display values from index 1 to 3
print(“values from index 1 to 3:”, marks[1:4])

Output: values from index 1 to 3 : (85, 90, 67)

# 3. Find the highest and lowest marks

print(“Highest marks:”, max(marks))
print(“Lowest marks:”, min(marks))

Output: Highest marks: 90
Lowest marks: 67

# 4. Convert the tuple into a list
Marks_list = list(marks)
print(“List:”, marks_list)

Output: List : [78, 85, 90, 67, 88]

# 5. Add 95 to the list
marls_list.append(95)
print(“Update list :”, marks_list)

Output : updated list : [78, 85, 90, 67, 88, 95]

# 6. Convert the updated list back into a tuple
Marks = tuple(marks_list)
print(“Updated tuple :”, marks

Output : updated tuple : (78, 85, 90, 67, 88, 95)

Question 7: Create a dictionary to store:

● Student name
● Roll number
● Course
● Marks

Write a Python program to:
1. Display all student details.
2. Add the student's city.
3. Update the marks.
4. Display all keys and values.
5. Iterate through the dictionary and print each key with its value.

# Creating a dictionary
student = {
"name": "Rahul",
"roll_number": 101,
"course": "BCA",
"marks": 85
}

# 1. Display all student details
print(“Student details:”)
print(student)

Output: {'name': 'Rahul', 'roll_number': 101, 'course': 'BCA', 'marks': 85}

# 2. Add the student’s city
student[“city”] = “Delhi”

# 3. Update the marks
Student[“marks”] = 90

# 4. Display all keys and values
print(“\n keys :”, student.keys())
print(“\n values :”, student.values())

Output: Keys: dict_keys(['name', 'roll_number', 'course', 'marks', 'city'])
Values: dict_values(['Rahul', 101, 'BCA', 90, 'Delhi'])

# 5. Iterate through the dictionary and print each key with its value
print(“\n key-value pairs:”)
For key, value in student.item():
print(Key, “:”, value)

Output:

Key-Value Pairs:
name : Rahul
roll_number : 101
course : BCA
marks : 90
city : Delhi

Question 8: Two classes have registered for different activities.

sports = {"Rahul", "Anil", "Priya", "Kiran"}
music = {"Priya", "Kiran", "Meena", "Arun"}

Write a Python program to find:
1. Students who joined either activity.
2. Students who joined both activities.
3. Students who joined only sports.
4. Students who joined only music.

Answer:

sports = {"Rahul", "Anil", "Priya", "Kiran"}
music = {"Priya", "Kiran", "Meena", "Arun"}

# 1. Students who joined either activity
either _activity = sports | music
print(“Students who joined either activity:”, either_activity)

Output:
Students who joined either activity: {'Rahul', 'Anil', 'Priya', 'Kiran', 'Meena', 'Arun'}

# 2. Students who joined both activities

Both_activites = sports & music
print(“Students who joined both activities:”, both_activities)

Output:
Students who joined both activities: {'Priya', 'Kiran'}

# 3. Students who joined only sports
Only_sports = sports - music
print(“Students who joined only sports:”, only_sports)

Output:
Students who joined only sports: {'Rahul', 'Anil'}

# 4. Students who joined only music

Only_music = music - sports
print(“Students who joined only music:”, only_music)

Output:
          
Students who joined only music: {'Meena', 'Arun'}
          
Question 9: Consider the following string:
          
"Python Java C C++ Python Java Python"
          
Write a Python program to:
1. Convert the string into a list of programming languages.
2. Display the list.
3. Count how many times "Python" appears.
4. Remove duplicate language names.
5. Join the unique language names using " | ".
          
Answer:
          
Languages = "Python Java C C++ Python Java Python"
# 1. Convert the string into a list
Language_list = language.split()
Output:
List: ['Python', 'Java', 'C', 'C++', 'Python', 'Java', 'Python']
          
# 2. Display the list
print(“Listr:”, language_list)
Output:
['Python', 'Java', 'C', 'C++', 'Python', 'Java', 'Python']
          
# 3. Count how many times “Python” appears
Print(“Python appears:”, language_list.count(“Pyhton”), “times”)
          
Output:
Python appears: 3 times
  
# 4. Remove duplicate language names
Unique_languages = list(dict.fromkeys(language_list))
Output:
['Python', 'Java', 'C', 'C++']
  
# 5. Join the unique language names using “ | “
Result = “ | “ . join(unique_languages)
print(“Unique language:”, result)
Output:
Python | Java | C | C++
  
# 10. Question 10: Write a Python program to print multiplication tables from 1 to 5.
Use nested loops to display each table from 1 × 1 up to 5 × 10.
Also modify the program so that:
● The number 5 is skipped using continue.
● The inner loop stops when the multiplier reaches 8 using break
  
Answer:
# Multiplication tables from 1 to 5
for i in range(1, 6):
# Skip the table of 5
if i == 5:
continue
print("\nTable of", i)
# Print table up to multiplier 10
for j in range(1, 11):
# Stop the inner loop when multiplier reaches 8
if j == 8:
break
print(i, "x", j, "=", i * j)
          
Output:
Table of 1
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
Table of 2
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
Table of 3
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
Table of 4
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
