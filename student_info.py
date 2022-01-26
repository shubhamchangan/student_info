# WAP to accept student name, marks from user and create a dict.
# Also display the student name and marks
import sys
n = int(input('Enter the number of students: '))
d = {}
for i in range(n):
    name = input('Enter the student name:')
    marks = int(input('Enter the marks obtained:'))
    #print('Hello', name, 'you got a', marks, 'marks')
    d[name] = marks
print(d)
while True:
    nm = input('Enter the student name to search:')
    if nm in d:
        print('Hello', nm, 'you got a', d[nm], 'marks')
    else:
        print('Candidate not found')
        break
