'''TASK
Create a program that reads the length and width of a farmer’s field from the user in feet. Display the area of the field in acres.

Hint: There are 43,560 square feet in an acre.

Sample Input

1000

1000

Sample Output

22.95684113865932 acres  '''

length=int(input())
width=int(input())
print((length*width)/43560,"acres")
