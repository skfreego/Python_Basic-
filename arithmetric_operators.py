"""
Task:- The provided code stub reads two integers from STDIN,a and b. Add code to print three lines where:
    1.The first line contains the sum of the two numbers.
    2.The second line contains the difference of the two numbers (first - second).
    3.The third line contains the product of the two numbers.

Input Format:-The first line contains the first integer, a.The second line contains the second integer, b.
Output Format:-  Print the three lines as explained above.
"""

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())

a = 3
b = 2
print('{0} \n{1} \n{2}'.format((a + b), (a - b), (a * b)))
