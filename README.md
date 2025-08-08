# Python Basic Tasks

This repository contains two beginner-level Python scripts:

- **Task 1**: Perform Basic Mathematical Operations
- **Task 2**: Create a Personalized Greeting
- **Task 3**: Check if a Number is Even or Odd
- **Task 4**: Sum of Integers from 1 to 50 Using a Loop
- **Task 5**: Calculate Factorial Using a Function
- **Task 6**: Using the Math Module for Calculations
- **Task 7**: Read a File and Handle Errors
- **Task 8**: Write and Append Data to a File
- **Task 9**: Create a Dictionary of Student Marks
- **Task 10**: Demonstrate List Slicing 

---

## Task 1: Basic Mathematical Operations

### File: `task1.py`

### Functionality:
This script:
1. Prompts the user to enter two numbers.
2. Performs and displays:
   - Addition
   - Subtraction
   - Multiplication
   - Division
3. Handles invalid numeric input and division by zero.

### Sample Output:
```
Enter the first number:50
Enter the second number:20
Addition:  70
Subtraction:  30
Multiplication:  1000
Division:  2.5
```
---

## Task 2: Personalized Greeting

### File: `task2.py`

### Functionality:
This script:
1. Prompts the user for their first and last name.
2. Combines them into a full name.
3. Prints a personalized greeting using the full name.

### Sample Output:
```
Enter your first name:John
Enter your second name:Doe
Hello, John Doe! Welcome to the Python program.
```
---

## Task 3: Check if a Number is Even or Odd

### File: `task3.py`

### Functionality:
This script:
1. Takes an integer input from the user.
2. Checks whether the number is even or odd using an if-else statement.
3. Displays the result accordingly.

### Sample Output:
```
Enter a number:5
5 is an odd number.
```
---

## Task 4: Sum of Integers from 1 to 50 Using a Loop

### File: `task4.py`

### Functionality:
This script:
1. Uses a for loop to iterate over numbers from 1 to 50.
2. Calculates the sum of all integers in this range.
3. Displays the final sum.

### Sample Output:
```
The sum of numbers from 1 to 50 is: 1275
```
---

## Task 5: Calculate Factorial Using a Function

## File: `task5.py`

### Functionality:
This script:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.

### Sample Output:
```
Enter a number:6
Factorial of 6 is: 720
```
---

## Task 6: Using the Math Module for Calculations

## File: `task6.py`

### Functionality:
This script:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.

### Sample Output:
```
Enter a number:49
Square root: 7.0
Logarithm: 3.8918202981106265
Sine: -0.9537526527594719
```
---

## Task 7: Read a File and Handle Errors 

## File: `task7.py`

### Functionality:
This script:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.

### Sample Output:
```
Line1: Hi, I'm Shyam.
Line2: Come let's have some coffee.
```
---

## Task 8: Write and Append Data to a File

## File: `task8.py`

### Functionality:
This script:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

### Sample Output:
```
Enter text to write a file:Hello all,
Data successfully written to output.txt
Enter additional text to append:How are you?
Data successfully appended
Final content of output.txt:
Hello all,
How are you?
```
---

## Task 9: Create a Dictionary of Student Marks

## File: `task9.py`

### Functionality:
This script:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.

### Sample Output:
```
Enter the student's name:John
John marks: 88
```
---

## Task 10: Demonstrate List Slicing 

## File: `task10.py`

### Functionality:
This script:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list

### Sample Output:
```
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed extracted elements: [5, 4, 3, 2, 1]
```
