#2D-Lists:

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][0])

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
1

Process finished with exit code 0





#now, we can use the nested for loop in order to print out all the elements inside of this 2D list:

for row in number_grid:
    for col in row:
        print(col)

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
1
2
3
4
5
6
7
8
9
0

Process finished with exit code 0
