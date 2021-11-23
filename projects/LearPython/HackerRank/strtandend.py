
# Re.start() & Re.end()
# These expressions return the indices of the start and end of the substring matched by the group.
# >>> import re
# >>> m = re.search(r'\d+','1234')
# >>> m.end()
# 4
# >>> m.start()
# 0
# Task
# You are given a string .
# Your task is to find the indices of the start and end of string in .
# Input Format
# The first line contains the string .
# The second line contains the string .
# Constraints
# Output Format
# Print the tuple in this format: (start _index, end _index).
# If no match is found, print (-1, -1) .
# Sample Input
# aaadaa
# aa
# Sample Output
# (0, 1)
# (1, 2)
# (4, 5)
# start() & end()
# Code


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
S = input()
K = input()

pttn = re.compile(K)
result = pttn.search(S)
if not result:
    print((-1,-1))
while result:
    lst = [result.start(),result.end()-1]
    print(tuple(lst))
    result = pttn.search(S,result.start()+1)
