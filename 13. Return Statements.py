#when we don't write return keyword:
def cube(num):
    num*num*num

cube(4)
print(cube(4))

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
None

Process finished with exit code 0




#return keyword will return the information to us back from the function:
def cube(num):
    return num*num*num

cube(4)
print(cube(4))

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
64

Process finished with exit code 0




#the return keyword breaks the function to an end:
def cube(num):
    return num*num*num
    print("hello")

print(cube(4))

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
64

Process finished with exit code 0
