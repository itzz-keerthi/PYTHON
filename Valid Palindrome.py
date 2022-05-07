'''TASK
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: 
A man, a plan, a canal: Panama

Output: 
1
Example 2:

Input: 
race a car

Output: 
0
 Constraints:

s consists only of printable ASCII characters. '''

str=input()
str1=str.lower()
str2=""
for i in str1:
    if(i.isalpha()==True):
        str2=str2+i
str3=str2[::-1]
if(str2==str3):
    print("1")
else:
    print("0")
