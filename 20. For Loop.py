#for loop:
#example 1:
for letter in "Garima Nagdeve":
    print(letter)

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
G
a
r
i
m
a
 
N
a
g
d
e
v
e

Process finished with exit code 0




#example 2:
friends = ['garima', 'doll']
for friend in friends:
    print(friend)

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
garima
doll

Process finished with exit code 0




#other uses with range:
friends = ['garima', 'doll']
for index in range(10):
    print(index)

#this will print everything from 1 to 10 not including 10

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
0
1
2
3
4
5
6
7
8
9

Process finished with exit code 0




#other uses of range:
friends = ['garima', 'doll']
for index in range(3,10):
    print(index)

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
3
4
5
6
7
8
9

Process finished with exit code 0




#other uses:
friends = ['garima' , 'doll' , 'kevin']
for name in range(len(friends)):
    print(friends[name])

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
garima
doll
kevin

Process finished with exit code 0
