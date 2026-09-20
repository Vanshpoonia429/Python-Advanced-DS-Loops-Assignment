# Python - Advanced DS, Type Conversion & Loops Assignment

## Part A - Theory (Q1-Q5)

Question 1: What is a tuple in Python? Explain how tuples are created, accessed, and sliced. Why are
tuples called immutable? Give one real-world situation where a tuple can be useful.

Answer:

A tuple in python is an ordered collection of elements that can store multiple values of different data
types. Tuple are written using parentheses().

- Creating a tuple

A tuple can be created by placing elements inside parentheses, separated by commas.
Example:- my_tuple = (10, 20, 30, 40)
A tuple can also contain different data types:
Student = (“Rahul”, 20, 30, 40)

- Accessing Elements

Tuple elements are accessed using their index. Indexing starts from 0.
Example:- my_tuple = (10, 20, 30, 40)

print( my_tuple[0] ) # 10
print(myt_tuple [2] ) # 30
Negative index can also be used:
print( my_tuple [-1] ) # 40

- Slicing a Tuple

Slicing is used to get a portion of a tuple
Example:- my_tuple = (10, 20, 30, 40, 50)
print( my_tuple [1:4 ) # (20, 30, 40)
This syntax is:- tuple [start:stop]

- Why are tuple immutable?

Tuple are called immutable because their elements cannot be changed, added, or removed
after the tuple is created.
For example:-

my_tuple = (10, 20, 30)
My_tuple [0] = 40 # Error
This produces a TypeError because the tuple cannot be modified.

- Real-World Use

A tuple is useful for storing fixed information, such as the cordinates of a location:
Location = (20.61, 77.23)
Here, the latitude and longitude can be stored together as a tuple because they represented a
fixed pair of values.

Question 2: What is a dictionary? Explain how key-value pairs work in Python. Describe how to add,
modify, delete, and access dictionary elements.

Answer:

Dictionary in Python

A dictionary in python is a collection of data stored in key-value pairs. Each key is required and is used
to identify and access its corresponding value.
Dictionaries are written using curly brackets {}.
Example:-

Student = {“Name”: “Rahul”, “Age”: 20, “Marks”: 85 }
Here “name”, “Age”, “Marks” are keys, while “Rahul”, 20, and 85 are their values.

- Creating a Dictionary

A dictionary can be created as follows:
student = {
"name": "Rahul",
"age": 20,
"marks": 85
}
Here :
- “Name”, “age”, and “marks” are keys.
- “Rahul”, 20, and 85 are their values.
- Adding Elements

A new key-value pair can be added by assigning a value to a new key.
student [“city”] = “Delhi”
Now the dictionary contains the “City” key with the value “Delhi”.

- Modifying Elements

An existing value can be changed by assigning a new value to its key.
student[“marks”] = 90
The value or “marks” is now 90.

- Deleting Elements

An element can be deleted using the del statement:
del student[“age”]
The pop() method can also be used:
student.pop(“city”)
Both methods remove the specified key-value pair.

- Accessing Dictionary Elements

Dictionary values can be accessed using their keys.

print(student[“name”]) # Rahul
print(stydent[“marks”]) # 90
The get() method can also be used:
print(student.get(“Age”)) # 20

Question 3: What is a set in Python? Explain why duplicate values are not stored in a set. Describe
union, intersection, and difference with suitable examples.

Answer:

- What is a set in Python

A set in python is an unordered collection of unique elements. It is used to store multiple values,
but it does not allow duplicate values.
Example:
Numbers = {1, 2, 3, 4}

- Why are duplicate values not stored in a set?

A set stores only unique values. If the same value is added more than once, Python
automatically removes the duplicates and keeps only one occurrence.
Example:
Numbers = {1, 2, 3, 3, 4, 4, 5}
print(numbers)
Output:- {1, 2, 3, 4, 5}
Thus, duplicate values are not stored because a set is designed to contain only unique
elements.

- Union

Union combines the elements of two sets. Duplicate elements are included only once.
Example:
A = {1, 2, 3}
B = {3, 4, 5}
print( A.union(B) )
Output:- {1, 2, 3, 4, 5}

- Intersection

Intersection gives the elements that are common to both sets
Example:.
print( A.intersection(B) )
Output:- {3}

- Difference

Difference gives the elements that are present in the first set but not in the second set.
Example:
print( A.difference(B) )
Output:- {1, 2}

Question 4: What are conditional statements in Python? Explain if, if-else, if-elif-else, and nested if

statements with suitable examples.

Answer:

What are conditional statements in python?
Conditional statements in python are used to make decisions in a program.
They executed a particular block of code when a specified condition is true.

- If statement

The if statement executed a block of code only when the given condition is true.
Age = 20
If age >= 18:
print(“Eligible to vote”)

- If-else statement

The if-else statement executed one block of code if the condition is true and another block if the
condition is false.
Age = 16
If age >= 18:
print(“Eligible to vote”)
else:
print(“Not eligible to vote”)

- If-elif-else Statement

The if-elif-else statement is used when there are multiple conditions, Python checks the
conditions one by one and executed the block of the first true condition.
marks = 75
if marks >= 90:
print(“Grade A”)
Elif marks >= 60:
print(“Grade B”)
Else:
print(“Grade C”)

- Nested if Statement

A nested if statement is an if statement placed inside another if statement.
If is used when one condition needs to be checked inside another condition.
Age = 20
If age >= 18:
If citizen:
print(“Eligible to vote”)

Question 5: Explain the difference between for and while loops. Also explain the purpose of break,

continue, pass, and the else clause with loops.

Answer:

- Difference Between for and while Loop

Loops in Python are used to repeat a block of code multiple times.
Difference Between for and while Loops

for Loop while Loop
Used when the number of iterations or
items to be processed is known.

Used when the number of
iterations depends on a
condition.

It is commonly used to iterate over
sequences such as lists, strings, and
ranges.

It continues running as long as
the given condition is true.

Example:- for i in range(5): Example:- while i < 5:

Example of for loop:
For i in range(5):
print(i)
Example of while loop:
i = 0
while i < 5:
print(i)
I += 1

- Break Statement

The break statement is used to immediately stop a loop.
for i in range (5) :
if i == 3:
break
print(i)

- Condition Statement

The continue statement skips the current iteration and moves to the next iteration of the loop.
for i in range(5):
if i == 2:
Continue
print(i)

- Pass Statement

The pass statement does nothing. It is used as a placeholder when a statement is required
syntactically but no action needs to be performed.
for i in range(3):
Pass

- Else Clause with Loops

The else clause with a loop executes when the loop finishes normally, without being terminated
by a break statement.
for i in range(3):
print(i)
else:
print(:Loop completed”)
