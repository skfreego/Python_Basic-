"""
Task:- The provided code stub reads two integers, a and b, from STDIN.
    Add logic to print two lines. The first line should contain the result of integer division,
    a//b . The second line should contain the result of float division, a/b.
    No rounding or formatting is necessary.
For example:- a = 3, b = 5 , the result of the integer division is 0 and the result of the float division is 0.6
Input Format:- The first line contains the first integer,a.The second line contains the second integer, b.
Output Format:- Print the two lines as described above
"""

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())

a = 4
b = 3

print("{0}\n{1}".format(a//b, a/b))
# print(a//b)    # integer division
# print(a/b)     # float division

