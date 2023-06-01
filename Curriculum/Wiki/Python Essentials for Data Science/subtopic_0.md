Welcome to Python Basics
========================


Dear first-year computer science students, today I will be introducing you to the wonderful world of Python programming. Python is a versatile and powerful programming language that is widely used in various fields such as data science, web development, and software engineering. We will be discussing some fundamental concepts that will help you get started with Python programming, including Syntax, Variables, Data Types, and Control Flow. To make it more relatable and engaging, I will be using a metaphor for each concept, so let's dive in!


Syntax - The Grammar of Python
------------------------------


Imagine you are learning a new language, say French. In order to communicate effectively, you need to follow certain rules and structures, like sentence formation, verb conjugation, and punctuation. Similarly, in Python or any programming language, there are specific rules and structures that dictate how we write code. These rules are called "syntax." By following these rules, we create a clear and concise code that both the computer and other programmers can understand.


Variables - The Labels of the Programming World
-----------------------------------------------


Let's say you have a box containing different items, and you want to keep track of them. You might label the box as "Stationery" if it contains pens, pencils, and erasers. In programming, we also need a way to store and organize information. We achieve this by using "variables." Variables are like labels that allow us to store, modify, and retrieve data in our code. This data can be numbers, text, or even more complex types of information.


Data Types - The Categories of Information
------------------------------------------


Continuing with our box analogy, imagine that you have several boxes containing different types of items: one for stationery, one for electronics, and one for clothes. Just like categorizing the items in our boxes, we need a way to classify the data in our code. This is where "data types" come into play. In Python, there are several built-in data types, such as:


* Integers (whole numbers)
* Floats (decimal numbers)
* Strings (text)
* Booleans (True or False)
* Lists (ordered collection of items)
* Tuples (ordered, immutable collection of items)
* Dictionaries (unordered collection of key-value pairs)


Understanding data types is crucial because it allows us to perform specific operations and manipulations according to the type of data we are working with.


Control Flow - The Decision-Making Process
------------------------------------------


Finally, let's discuss "control flow." In our daily lives, we often make decisions based on certain conditions. For example, if it's raining, we'll take an umbrella; otherwise, we won't. Similarly, in programming, we need a way to make decisions and control the flow of our code. This is achieved through the use of control flow statements such as:


* If, elif, and else statements (conditional branching)
* For loops (iterating over a sequence)
* While loops (iterating based on a condition)


Control flow allows us to create dynamic and flexible code that can react and adapt to different situations and inputs.




---


And that's a brief overview of Python basics. By understanding the syntax, variables, data types, and control flow, you are now well-equipped to start your journey into the world of Python programming. Happy coding!


Python Basics
=============


Welcome to your first year of computer science! Today, we'll be exploring some of the fundamental concepts in Python, a versatile and widely-used programming language. Specifically, we will cover Syntax, Variables, Data Types, and Control Flow. Let's dive right in!


Syntax
------


Python is designed to be easy to read and write, with a clear and concise syntax. The basic structure of a Python program consists of statements, which are executed sequentially. Indentation is used to denote blocks of code, such as the body of a function or a loop. Comments can be added using the '#' symbol.


```python


This is a single-line comment in Python
=======================================


"""
This is a multi-line comment
in Python, it's actually a string literal
but it's commonly used for comments as well
"""
```


Variables
---------


In Python, variables are used to store data. They are assigned a value using the '=' operator. Variables in Python are dynamically typed, meaning you don't need to explicitly state their type before assigning a value.


`python
x = 5 # Assign the value 5 to the variable x`


Data Types
----------


Python has a variety of built-in data types for representing different kinds of data. Some common data types are:


1. **int**: Integer numbers (e.g., 42, -3).
2. **float**: Floating-point numbers (e.g., 3.14, -0.5).
3. **str**: Strings, which are sequences of characters (e.g., "hello", "world").
4. **bool**: Boolean values, either `True` or `False`.
5. **list**: Ordered, mutable sequences of elements (e.g., [1, 2, 3]).
6. **tuple**: Ordered, immutable sequences of elements (e.g., (1, 2, 3)).
7. **dict**: Key-value mappings (e.g., {"key": "value"}).


`python
integer_value = 42
float_value = 3.14
string_value = "hello"
boolean_value = True
list_value = [1, 2, 3]
tuple_value = (1, 2, 3)
dictionary_value = {"key": "value"}`


Control Flow
------------


Control flow statements allow you to change the order in which your code is executed. Some common control flow statements are:


1. **if, elif, else**: Conditional statements used to perform different actions based on whether a condition is true or false.
2. **for**: Used to iterate over a sequence (e.g., list, tuple, string).
3. **while**: Repeats a block of code as long as a condition is true.
4. **break**: Exits the nearest enclosing loop.
5. **continue**: Skips the rest of the current iteration and continues with the next iteration of the loop.


### Example


```python


Here's a concrete example demonstrating the concepts we've covered.
===================================================================


Defining a function to check if a number is even
================================================


def is\_even(number):
 if number % 2 == 0:
 return True
 else:
 return False


Defining a list of integers
===========================


numbers = [1, 2, 3, 4, 5]


Iterating over the list and printing even numbers
=================================================


for num in numbers:
 if is\_even(num):
 print(f"{num} is even.")
 else:
 continue # Skip to the next iteration if the number is not even


```


That's a brief overview of Python basics! As you progress through your computer science journey, you'll become more familiar with these concepts and learn about many more advanced topics. Happy coding!


Python Basics
=============


Welcome, first year computer science students! Today, we will be discussing Python basics, which include Syntax, Variables, Data Types, and Control Flow. Python is a versatile and powerful programming language, making it a great choice for beginners and experts alike. To make this knowledge relatable and easier to understand, we'll go through three example use cases.


Syntax
------


Python syntax refers to the set of rules that dictate how we should write Python code. Proper syntax is crucial because it ensures that the code is readable and can be correctly interpreted by the Python interpreter.


### Example 1: Hello, World!


Let's begin with a classic example - printing "Hello, World!" to the console. In Python, we can achieve this using the `print()` function.


`python
print("Hello, World!")`


Here, we've written a single line of code that calls the `print()` function with a string argument `"Hello, World!"`. The function then prints the given text to the console.


Variables
---------


Variables are used to store and manipulate data in a program. They are given unique names (identifiers) and can be assigned values using the assignment operator `=`.


### Example 2: Simple Arithmetic


Let's say we want to perform some basic arithmetic operations, like adding two numbers together. We can use variables to store these numbers and their sum.


```python


Declare variables
=================


num1 = 5
num2 = 3


Perform arithmetic operation
============================


sum = num1 + num2


Print the result
================


print("The sum of", num1, "and", num2, "is", sum)
```


In this example, we've declared three variables: `num1`, `num2`, and `sum`. We've assigned the values 5 and 3 to `num1` and `num2` respectively, and then calculated their sum. Finally, we've printed the result to the console.


Data Types
----------


Python has several built-in data types, such as integers, floats, strings, and lists. These data types help us store and manipulate different kinds of data in our programs.


### Example 3: Shopping List


Imagine we want to create a program to manage a shopping list. We can use a list data type to store the items on the list and perform various operations, like adding and removing items.


```python


Declare a shopping list
=======================


shopping\_list = ["milk", "eggs", "bread"]


Add an item to the list
=======================


shopping\_list.append("butter")


Remove an item from the list
============================


shopping\_list.remove("eggs")


Print the updated shopping list
===============================


print("Updated shopping list:", shopping\_list)
```


In this example, we've created a shopping list using a Python list data type. We've added an item to the list using the `append()` method and removed an item using the `remove()` method. Finally, we've printed the updated shopping list to the console.


Control Flow
------------


Control flow refers to the order in which a program's statements are executed. It allows us to create more complex programs by using constructs like loops and conditional statements.


### Example 4: FizzBuzz


As a final example, let's implement the classic FizzBuzz problem. We want to print the numbers from 1 to 20, but for multiples of 3, we'll print "Fizz" instead of the number, and for multiples of 5, we'll print "Buzz". For numbers which are multiples of both 3 and 5, we'll print "FizzBuzz".


```python


Iterate over numbers from 1 to 20
=================================


for i in range(1, 21):
 # Check for multiples of 3 and 5
 if i % 3 == 0 and i % 5 == 0:
 print("FizzBuzz")
 # Check for multiples of 3
 elif i % 3 == 0:
 print("Fizz")
 # Check for multiples of 5
 elif i % 5 == 0:
 print("Buzz")
 # Print the number if it's not a multiple of 3 or 5
 else:
 print(i)
```


In this example, we've used a `for` loop to iterate over the numbers from 1 to 20. We've used `if`, `elif`, and `else` conditional statements to determine whether a number is a multiple of 3, 5, or both, and printed the appropriate output.


These examples should provide you with a good foundation for understanding Python basics. As you continue your studies, you'll learn more about Python's features and how to use them to create even more advanced programs. Good luck, and happy coding!


Question 1: In Python, what is the correct way to define a variable?


a) var my*variable = 10
b) int my*variable = 10
c) my*variable: int = 10
d) my*variable = 10


Question 2: Which of the following is NOT a basic data type in Python?


a) int
b) float
c) char
d) str


Question 3: What is the output of the following code snippet?


`python
x = 5
if x > 3:
 print("A")
elif x < 7:
 print("B")
else:
 print("C")`


a) A
b) B
c) A B
d) C


Question 4: What is the correct way to start a for loop in Python?


a) for i = 0; i < 5; i++:
b) for i in range(5):
c) for(i = 0; i < 5; i++):
d) for i from 0 to 5:


Question 5: Which of the following Python code snippets correctly defines a function that takes two numbers as input and returns their sum?


a)
`python
def add_numbers(a, b):
 return a + b`


b)
`python
function add_numbers(a, b):
 return a + b`


c)
`python
def add_numbers(a, b):
print(a + b)`


d)
`python
add_numbers(a, b) = a + b`


