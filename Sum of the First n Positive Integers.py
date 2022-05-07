'''TASK
Write a program that reads a positive integer, n, from the user and then displays the sum of all of the integers from 1 to n. The sum of the first n positive integers can be computed using the formula:

sum = ( n ) (n + 1) / 2

Sample Input

10

Sample Output

The sum of the first 10 positive integers is 55.0 '''

n=int(input())
sum=0
for i in range(1,n+1):
    sum+=i
print("The sum of the first",n,"positive integers is",float(sum))
