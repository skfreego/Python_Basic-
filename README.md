# Python_Basic_Introduction
HackerRank Challenge|
Domain:Python|
SubDomain:Introduction|
Skill:Python(Basic)|

#say_hello_world_with_python|
   Objective: This is a simple challenge to help you practice creating variables and printing to stdout.(stdout)Standard output is a stream to which a program writes
 its output data. The program requests data transfer with the write operation. Not all programs generate output.
   
#python_if_else|
	In this challenge, we test your knowledge of using if-else conditional statements to automate decision-making processes. An if-else statement has the 
following logical flow:
Sample Input:3
Sample Output:Weird
Explanation: n=3, n is odd and odd numbers are weird, so print Weird.

Sample Input1:24
Sample Output1:Not Weird
Explanation1: n=24, n>20 and n is even, so it is Not Weird.

#arithmetic_operators|

	#Python 2
	a = int(raw_input())
	b = int(raw_input())

	#Python 3
	a = int(input())
	b = int(input())
In the above statements, raw_input() and input() are the Python 2 and Python 3 methods to read lines from STDIN. The methods return a string by default. 
Since this problem uses numeric data, the input value must be converted to an integer. Convert a string to an integer using int().
Now, a bit about Arithmetic Operators
The three basic arithmetic operators are the following:
    Addition (+)
    Subtraction (-)
    Multiplication (*)
There are several division methods that will be discussed in the next challenge. Of the three operators shown, multiplication takes precedence 
over addition and subtraction. Addition and subtraction have equal precedence. 
For Example:
Given (3*2) + 3 = 6 + 3 = 9, the paranthesis are unnecessary due to precedence.Multiplication is performed before addition. This equation can be written more simply as
3 * 2 + 3.
To multiply 3 by 2 + 3, write 3 *(2 + 3) = 3 * 5 = 15.

  Sample Input:- 
  3
  2

  Sample Output:-
  5
  1
  6

  Explanation
  3 + 2 = 5
  3 - 2 = 1
  3 * 2 = 6



#python_division|
	In Python, there are two kinds of division: integer division and float division.
	Integer Division
	Integer division returns the floor of the division. That is, the values after the decimal point are discarded. 
	It is written as '//' in Python 3. So, 1//3 = 0, 2//3 = 0 and 3//3 = 1. Integer values are precisely stored, so they are safe to use in comparisons.
	In Python 2, the '//' operator is not included, so it must be imported from the __future__ module. 
	See the code below for how to use the '//' operator in Python 2. The '/' operator in Python 2 returns an integer result if both of the operands are integers.

	Python 2
	# Python 2 integer division using '//'
	from __future__ import division
	print 4//3  # prints 1
	or
	# Python 2 integer division using '/'
	print 4/3  # prints 1

	Python 3
	# Python 3 integer division
	print(4//3) # prints 1

	Float Division
	Float division returns a floating point approximation of the result of a division. For example,
	Only a certain number of values after the decimal can be stored, so it is not possible to store an exact binary representation of many floating point numbers. 
	This sometimes leads to problems when comparing numbers or when rounding.
	In Python 2, the only standard division operator is '/'. If both values are integers, the result is an integer. If either of the values is a float, 
	the return is a float. The __future__ module can be used so that '/' represents floating point division as it does in Python 3.

	Python 2
	from __future__ import division

	# floating point division using __future__ syntax
	print 4 / 3 # prints 1.33333333333

	or

	# floating point division using a float to force float result
	# no need to import from __future__
	print 4 / 3.0 # prints 1.33333333333
	Python 3
	print(4 / 3) # prints 1.33333333333

#loops|
Loops are control structures that iterate over a range to perform a certain task. They can work with any iterable type, such as lists and dictionaries.
 To control the loop in this problem, use the range function (see below for a description).
There are two kinds of loops in Python.

for loop:

for i in range(0, 5):
    print i

And a while loop:

i = 0
while i < 5:
    print i
    i += 1

When using a for loop, the next value from the iterator is automatically taken at the start of each loop.
When using a while loop, the iterator must be initialized prior to the loop, and the value updated within the loop.
The range() function
The range function is a built in function that returns a series of numbers. At a minimum, it needs one integer parameter. 

for example:- 
n = 3
the list of non-negative integers that are less than n = 3 is [0,1,2].Print the square of each number on a separate line.
0
1
4

#print_function|
In Python 2, the default print is a simple IO method that doesn't give many options to play around with.
The following two examples will summarize it.

Example 1:

var, var1, var2 = 1,2,3
print var
print var1, var2 

Prints two lines and, in the second line,and are separated by a single space.

Example 2:

for i in xrange(10):
    print i,

Prints each element separated by space on a single line. Removing the comma at the end will print each element on a new line.Let's import the advanced print_function from the __future__ module.

Its method signature is below:

print(*values, sep=' ', end='\n', file=sys.stdout)
print(value1, value2, value3, sep=' ', end='\n', file=sys.stdout)
Here, values is an array and *values means array is unpacked, you can add values separated by a comma too. The arguments sep, end, and file are optional, but they can prove helpful in formatting output without taking help from a string module.
The argument definitions are below:
sep defines the delimiter between the values.
end defines what to print after the values.
file defines the output stream.The Python 2 print_function is much faster than the default print.
