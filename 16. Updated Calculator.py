#Building a better calculator:

num1 = float(input("enter first number: "))
op = input("enter operator: ")
num2 = float(input("enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("invalid operator")

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
enter first number: 2
enter operator: +
enter second number: 5
7.0

Process finished with exit code 0
