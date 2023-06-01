Operators and Expressions: The Building Blocks of Programming
=============================================================


Welcome to your first year of Computer Science! Today, we are going to talk about two very important building blocks of programming: Operators and Expressions.


You can think of Operators as the tools that we use to manipulate data in a program. Just like a carpenter uses a hammer to drive nails into wood, a programmer uses operators to perform actions on data. 


Expressions, on the other hand, are combinations of values, variables, and operators that evaluate to a single value. It's like a recipe that combines different ingredients to make a delicious dish. 


For example, imagine you are baking a cake. You have all the necessary ingredients - flour, sugar, eggs, and butter. These ingredients are like the values and variables in a program. 


Now, you need to mix them together and add some operators - like a whisk, a spatula, or a mixer - to create a batter. This batter is like an expression. It's a combination of ingredients - values and variables - and operators that evaluate to a single value - in this case, a cake batter.


In programming, we use operators to perform various actions on data. For example, we can use the '+' operator to add two numbers together, or the '\*' operator to multiply them. We can also use operators to compare values, like the '==' operator to check if two values are equal.


Expressions are used to create more complex operations by combining values, variables, and operators. For example, we can create an expression that adds two numbers together and then multiplies them by a third number. 


In conclusion, operators and expressions are the building blocks of programming. They allow us to manipulate data and create more complex operations. So, just like a carpenter needs to know how to use different tools to build a house, a programmer needs to understand operators and expressions to build great software.


Operators and Expressions
=========================


Introduction
------------


In programming, an **operator** is a symbol that represents a specific action on one or more operands. An **operand** is a value or a variable that is operated on by an operator. Together, an operator and operands form an **expression**. 


Expressions are the building blocks of programs. They are used to perform arithmetic, logical, and comparison operations. In this lesson, we will explore some common operators and expressions in Python.


Arithmetic Operators
--------------------


Arithmetic operators are used to perform mathematical operations on operands. The following table lists some common arithmetic operators:


| Operator | Description | Example |
|----------|-----------------|---------|
| + | Addition | 2 + 3 |
| - | Subtraction | 5 - 2 |
| \* | Multiplication | 3 \* 4 |
| / | Division | 7 / 2 |
| % | Modulus | 7 % 2 |
| *\* | Exponentiation | 2 \** 3 |


Let's take a look at some examples of arithmetic expressions:


```python


Addition
========


x = 2
y = 3
z = x + y
print(z) # Output: 5


Subtraction
===========


a = 5
b = 2
c = a - b
print(c) # Output: 3


Multiplication
==============


p = 3
q = 4
r = p \* q
print(r) # Output: 12


Division
========


m = 7
n = 2
o = m / n
print(o) # Output: 3.5


Modulus
=======


e = 7
f = 2
g = e % f
print(g) # Output: 1


Exponentiation
==============


h = 2
i = 3
j = h \*\* i
print(j) # Output: 8
```


Comparison Operators
--------------------


Comparison operators are used to compare two values and return a Boolean value (True or False). The following table lists some common comparison operators:


| Operator | Description | Example |
|----------|--------------------|---------|
| == | Equal to | 2 == 3 |
| != | Not equal to | 5 != 2 |
| > | Greater than | 7 > 2 |
| < | Less than | 3 < 4 |
| >= | Greater than or equal to | 5 >= 5 |
| <= | Less than or equal to | 2 <= 3 |


Let's take a look at some examples of comparison expressions:


```python


Equal to
========


x = 2
y = 3
z = x == y
print(z) # Output: False


Not equal to
============


a = 5
b = 2
c = a != b
print(c) # Output: True


Greater than
============


p = 7
q = 2
r = p > q
print(r) # Output: True


Less than
=========


m = 3
n = 4
o = m < n
print(o) # Output: True


Greater than or equal to
========================


e = 5
f = 5
g = e >= f
print(g) # Output: True


Less than or equal to
=====================


h = 2
i = 3
j = h <= i
print(j) # Output: True
```


Logical Operators
-----------------


Logical operators are used to combine two or more Boolean expressions and return a Boolean value. The following table lists some common logical operators:


| Operator | Description | Example |
|----------|-------------------------------|-----------|
| and | True if both operands are True | x > 0 and x < 10 |
| or | True if either operand is True | x < 0 or x > 10 |
| not | True if operand is False | not(x > 0 and x < 10) |


Let's take a look at some examples of logical expressions:


```python


and
===


x = 5
y = 7
z = (x > 0) and (y < 10)
print(z) # Output: True


or
==


a = 5
b = 11
c = (a < 0) or (b > 10)
print(c) # Output: True


not
===


p = 5
q = (p > 0) and (p < 10)
r = not q
print(r) # Output: False
```


Conclusion
----------


In summary, operators and expressions are essential concepts in programming. They are used to perform various


Introduction
------------


Welcome to our lesson on Operators and Expressions! In programming, operators are symbols that represent an action or a process that is carried out on one or more data values. Expressions, on the other hand, are combinations of variables, values and operators that produce a result.


Example 1: Arithmetic Operators
-------------------------------


Let's start with arithmetic operators, which are used to perform mathematical operations on numerical values. Some examples of arithmetic operators include:


* Addition (+)
* Subtraction (-)
* Multiplication (\*)
* Division (/)
* Modulus (%)


Let's say we want to write a program that calculates the area of a rectangle. We can use the multiplication operator (\*) to multiply the length and width of the rectangle:


`length = 5
width = 3
area = length * width
print(area)`


The output of this program would be: `15`


Example 2: Comparison Operators
-------------------------------


Comparison operators are used to compare two values and return a Boolean value (True or False). Some examples of comparison operators include:


* Equal to (==)
* Not equal to (!=)
* Greater than (>)
* Less than (<)
* Greater than or equal to (>=)
* Less than or equal to (<=)


Let's say we want to write a program that compares the age of two people. We can use the greater than operator (>) to compare the ages:


`age1 = 20
age2 = 25
is_older = age2 > age1
print(is_older)`


The output of this program would be: `True`


Example 3: Logical Operators
----------------------------


Logical operators are used to combine multiple conditions and return a Boolean value. Some examples of logical operators include:


* And (and)
* Or (or)
* Not (not)


Let's say we want to write a program that determines if a person is eligible to vote. We can use the logical and operator (and) to combine two conditions: the person must be 18 years or older, and must be a citizen:


`age = 20
is_citizen = True
is_eligible_to_vote = age >= 18 and is_citizen
print(is_eligible_to_vote)`


The output of this program would be: `True`


Conclusion
----------


In conclusion, operators and expressions are essential components of programming. They allow us to perform operations on values, compare values, and combine conditions. By understanding how to use operators and expressions, we can write more sophisticated and powerful programs.


1. Which of the following is NOT a valid operator in Python?
a) +
b) %
c) &
d) $
2. What is the result of the following expression: 10 \* 5 + 3?
a) 35
b) 53
c) 53.0
d) None of the above
3. Which of the following is true for the following expression: 5 > 3 and 4 < 6?
a) True
b) False
c) Error
d) None of the above
4. Which of the following operators has the highest precedence in Python?
a) \*\*
b) \*
c) +
d) %
5. What is the result of the following expression: 7 // 3 + 4 \*\* 2?
a) 16
b) 17
c) 18
d) None of the above


