#Building a guessing game:
#user can keep guessing the secret word util they get it right:

secret_word = "giraffe"
guess = ""

while guess != secret_word:
    guess = input("Enter guess: ")

print("You Got It!")

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
Enter guess: hello
Enter guess: hi
Enter guess: giraffe
You Got It!

Process finished with exit code 0




#building a better version of it:

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOOSE!")
else:
    print("You Got It, YOU WIN!")

"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
Enter guess: hello
Enter guess: hi
Enter guess: bye
Out of Guesses, YOU LOOSE!

Process finished with exit code 0



"C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\.venv\Scripts\python.exe" "C:\Users\Garima Nagdeve\PycharmProjects\pythonProject\app.py" 
Enter guess: hello
Enter guess: fnifo
Enter guess: giraffe
You Got It, YOU WIN!

Process finished with exit code 0
