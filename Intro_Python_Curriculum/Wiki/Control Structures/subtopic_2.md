As a computer science student, you might have come across situations where you have to perform the same task multiple times. For example, imagine you are asked to count the number of birds you see in your backyard. You might start by counting each bird as you see it, one by one. This is like a loop, where you repeat the same process until you have counted all the birds.


Now, imagine you see a bird that you have already counted. You don't want to count it again, so you skip it and continue counting the other birds. This is like a loop control statement, where you can skip or repeat certain parts of the loop based on a condition.


Similarly, let's say you are counting the number of cars that pass by your house. But you only want to count the red ones. In this case, you can use a loop control statement to skip all the cars that are not red and only count the ones that meet your condition.


Loop control statements are like traffic signals that guide the flow of traffic in a loop. They help you navigate through a loop and make the most out of it, just like traffic signals help you navigate through a busy road.


Loop Control Statements
=======================


Loop control statements are used to control the execution of loops (i.e., `for` and `while` loops). They allow us to modify the behavior of a loop in various ways, such as changing the loop counter, skipping iterations, or breaking out of the loop entirely.


The `while` loop
----------------


Let's start with the `while` loop. This loop repeatedly executes a block of code as long as a certain condition is true. Here's an example:


```python


This program prints the numbers 1 through 10 using a while loop
===============================================================


count = 1
while count <= 10:
 print(count)
 count += 1
```


In this example, we first initialize the counter variable `count` to 1. We then use a while loop to repeatedly print the value of `count` and increment it by 1 until it reaches 10. The condition `count <= 10` is checked before each iteration of the loop, and the loop exits as soon as this condition is no longer true.


The `for` loop
--------------


The `for` loop is used to iterate over a sequence (e.g., a list or a string) and execute a block of code once for each element in the sequence. Here's an example:


```python


This program prints the elements of a list using a for loop
===========================================================


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
 print(fruit)
```


In this example, we define a list of fruits and use a for loop to iterate over each element in the list and print it. The loop variable `fruit` takes on each value in the list in turn, and the loop exits when there are no more elements left to iterate over.


Loop control statements
-----------------------


Now that we know how to use loops, let's take a look at some loop control statements that can modify their behavior.


### The `break` statement


The `break` statement is used to immediately exit a loop, regardless of whether the loop condition has been met. Here's an example:


```python


This program searches a list for a target value using a for loop and a break statement
======================================================================================


numbers = [1, 3, 5, 7, 9]
target = 5
found = False


for number in numbers:
 if number == target:
 found = True
 break


if found:
 print("Target found!")
else:
 print("Target not found.")
```


In this example, we define a list of numbers and a target value to search for. We then use a for loop to iterate over each element in the list and check whether it is equal to the target value. When we find the target value, we set the flag variable `found` to `True` and immediately exit the loop using the `break` statement.


### The `continue` statement


The `continue` statement is used to skip the current iteration of a loop and move on to the next one. Here's an example:


```python


This program prints the odd numbers between 1 and 10 using a for loop and a continue statement
==============================================================================================


for i in range(1, 11):
 if i % 2 == 0:
 continue
 print(i)
```


In this example, we use the `range` function to generate the numbers 1 through 10 and iterate over them using a for loop. We use the modulus operator `%` to check whether each number is odd or even. When we encounter an even number, we skip the current iteration of the loop using the `continue` statement and move on to the next number.


### The `else` clause


The `else` clause can be used to specify a block of code that should be executed after a loop has finished iterating over its sequence. Here's an example:


```python


This program prints the elements of a list and a message indicating that the loop has finished using a for loop and an else clause
==================================================================================================================================


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
 print(fruit)
else:
 print("No more fruits.")
```


In this example, we define a list of fruits and use a for loop to iterate over each element in the list and print it. After the loop has finished iterating over the list, we print a message indicating that there are no more fruits left to print.


Conclusion
----------


Loop control statements allow us to modify the behavior of loops in various ways, such as exiting the loop early, skipping iterations, or executing code after the loop has finished. By using these statements in combination with `for` and `while` loops, we can write more complex and powerful programs that can handle a wide variety of tasks.


Loop Control Statements
-----------------------


Loop control statements are used in computer programming to control the execution of loops. There are three main loop control statements that we will be discussing today: `break`, `continue`, and `pass`. 


### Break


The `break` statement is used to terminate a loop prematurely. This is useful when we know that we want to exit a loop before it has completed all iterations. For example, let's say we are searching through a list of numbers for a specific value. Once we find the value, there is no need to continue searching through the rest of the list. We can use the `break` statement to exit the loop as soon as we find the value we are looking for.


```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for number in numbers:
 if number == 5:
 print("Found the number!")
 break
```


### Continue


The `continue` statement is used to skip over an iteration of a loop. This is useful when we want to skip over certain values or conditions in a loop. For example, let's say we are looping through a list of numbers and we want to print out only the even numbers. We can use the `continue` statement to skip over the odd numbers.


```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for number in numbers:
 if number % 2 != 0:
 continue
 print(number)
```


### Pass


The `pass` statement is used as a placeholder when we don't want to do anything in a loop. It is essentially a no-op statement, meaning it does nothing. This is useful when we are writing code and want to leave a section empty for future implementation. For example, let's say we are writing a function to calculate the average of a list of numbers, but we haven't yet implemented the code to calculate the average. We can use the `pass` statement as a placeholder until we write the actual code.


`python
def calculate_average(numbers):
 # TODO: Implement code to calculate average
 pass`


In summary, loop control statements are used to control the execution of loops in computer programming. The `break` statement is used to terminate a loop prematurely, the `continue` statement is used to skip over an iteration of a loop, and the `pass` statement is used as a placeholder when we don't want to do anything in a loop.


1. Which of the following loop control statements is used to skip the current iteration of a loop?
a. break
b. continue
c. return
d. exit
2. Which of the following loop control statements is used to terminate a loop immediately?
a. break
b. continue
c. return
d. exit
3. Which of the following loop control statements is used to execute a block of code repeatedly until a condition is met?
a. switch
b. if-else
c. while
d. for
4. Which of the following loop control statements is used to execute a block of code at least once, even if the condition is false?
a. do-while
b. for
c. while
d. if-else
5. Which of the following loop control statements is used to execute a block of code based on a specific range or number of iterations?
a. for
b. while
c. do-while
d. switch


