Hello, first year computer science students! Today, we will be discussing conditional statements in computer programming. Simply put, a conditional statement is like a fork in the road. 


Imagine you are driving down a road and you come to a fork. You have to make a decision about which path to take. Similarly, in computer programming, a conditional statement allows the program to make a decision about what to do based on certain conditions or criteria. 


Just like how you might decide to take the left path if you want to go to the beach and the right path if you want to go to the mountains, a program can make different decisions based on different conditions. For example, if a user enters the correct password, the program will allow them to access their account. But if they enter the wrong password, the program will deny them access.


Conditional statements are useful because they allow programs to be more flexible and responsive to different situations. They also help to prevent errors and ensure that the program is functioning as intended. 


So, just like how you make decisions based on different factors in your life, programs can make decisions based on different conditions with the help of conditional statements.


Introduction to Conditional Statements
======================================


Welcome to our lesson on Conditional Statements! As computer scientists, we often need to make decisions based on certain conditions. Conditional statements help us do just that. 


A conditional statement is a programming statement that performs different actions based on whether a certain condition is true or false. 


Syntax
------


The basic syntax of a conditional statement in Python is as follows:


`python
if condition:
 # do something
else:
 # do something else`


The `if` statement is followed by a condition that is either true or false. If the condition is true, the code block inside the `if` statement is executed. If the condition is false, the code block inside the `else` statement is executed. 


Example
-------


Let's look at an example to make this clearer. 


Suppose we want to write a program that tells us whether a number is positive or negative. We can use a conditional statement to do this. 


```python


Take input from user
====================


num = int(input("Enter a number: "))


Check if number is positive or negative
=======================================


if num > 0:
 print("The number is positive.")
else:
 print("The number is negative.")
```


In this code, we first take input from the user using the `input()` function. We convert the input to an integer using the `int()` function and store it in the variable `num`. 


Next, we use a conditional statement to check if the number is positive or negative. If the number is greater than 0, we print "The number is positive." If the number is less than or equal to 0, we print "The number is negative."


Conclusion
----------


That's it for our lesson on Conditional Statements! They are an important part of programming and can help us make decisions based on certain conditions. Remember to always test your code with different inputs to make sure it works correctly.


Conditional Statements
======================


Conditional statements are an essential part of programming. They allow us to make decisions based on certain conditions. In simple terms, we can think of them as "if-then" statements. If a certain condition is met, then we do something, otherwise, we do something else.


Example Use Cases
-----------------


Let's take a look at some example use cases to understand how conditional statements can be used in programming.


### 1. Grade Calculator


Suppose we want to create a program that calculates the letter grade for a student based on their numerical grade. We can use conditional statements to achieve this.


For example, if the numerical grade is greater than or equal to 90, then the letter grade is an "A". If the numerical grade is between 80 and 89, then the letter grade is a "B", and so on.


### 2. Authentication


Another use case for conditional statements is in authentication. Suppose we have a login system where users need to enter a username and password to access their account. We can use conditional statements to check if the username and password entered by the user are correct.


If the username and password are correct, then we allow the user to access their account. If the username or password is incorrect, then we display an error message and ask the user to try again.


### 3. Game Logic


Conditional statements can also be used in game development. For example, suppose we are creating a game where the player needs to collect coins to score points. We can use conditional statements to check if the player has collected enough coins to move to the next level.


If the player has collected enough coins, then we move them to the next level. If not, then we display a message asking the player to collect more coins before moving to the next level.


Conclusion
----------


Conditional statements are an essential part of programming, and they allow us to make decisions based on certain conditions. We can use them in various use cases, such as grade calculation, authentication, and game development. By understanding how to use conditional statements, we can create more complex and useful programs.


1. Which of the following is a valid conditional statement in programming?
a) if (x = 5)
b) if x == 5:
c) if (x equals 5)
d) if x = 5
2. What is the purpose of a conditional statement in programming?
a) To execute a block of code repeatedly
b) To terminate a program
c) To execute a block of code only if a certain condition is met
d) To print output on the screen
3. What is the syntax for an if statement in programming?
a) if (condition) { code }
b) if condition: code
c) if [condition] then { code }
d) if {condition} code
4. What is the difference between the "if" and "else" statements in programming?
a) "If" is used to execute a block of code only if a certain condition is met, while "else" is used to execute a block of code if the condition is not met
b) "If" and "else" are used interchangeably in programming
c) "If" is used to terminate a program, while "else" is used to execute a block of code repeatedly
d) There is no difference between "if" and "else" statements in programming
5. Which of the following is an example of a nested if statement in programming?
a) if (x > 5) { if (y > 10) { code } }
b) if (x > 5) { code } else { code }
c) if (x > 5 || y < 10) { code }
d) if (x == 5) { code }


