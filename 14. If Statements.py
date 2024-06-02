#if statements:
is_male = False

if is_male:
    print("You are a male")
else:
    print("you are not a male")

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
you are not a male

Process finished with exit code 0




#if statements with or operator:
is_male = False
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("you are neither a male nor tall")

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
You are a male or tall or both

Process finished with exit code 0




#if statements with and operator:
is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a male and tall both")
else:
    print("you are neither a male nor tall")

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
you are neither a male nor tall

Process finished with exit code 0




#if statements with elif and not() function:
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a male and tall both")

elif is_male and not(is_tall):
    print("you are a male but you are not tall")

elif not(is_male) and is_tall:
    print("you are not a male but you are tall")

else:
    print("you are neither a male nor tall")

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
you are a male but you are not tall

Process finished with exit code 0
