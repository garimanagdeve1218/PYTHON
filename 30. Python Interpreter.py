'''Interpreted Languages: Perl, BASIC, Python, JavaScript, Ruby, PHP.
Compiled Languages: C, C++, C#, COBOL and CLEO.'''



'''What are Interpreters?
Interpreters are the computer program that will convert the source code or an high level language into intermediate code (machine level language). It is also called translator in programming terminology. Interpreters executes each line of statements slowly. This process is called Interpretation. 
For example Python is an interpreted language, PHP, Ruby, and JavaScript.'''



'''Advantages of using Interpreter
It is flexible and error localization is easier.
It is smaller in size.
It executes line by line execution.



Disadvantages of using Interpreters
It takes lot of time to translate.
It is slower.
It uses lot of storage.'''



'''How interpreters function in Python?
Python interpreter is written in C programming language as we all know that C is considered as mother of all programming languages, Python interpreter called “CPython”.

Initially in source code analysis, Python get source and check for some Indentation rule and check for errors. if there are any errors Python stops its execution and make to modify to prevent errors. This process is called Lexical analysis in python which states that dividing the source code into list of individual tokens.

In Byte code generation, once the python interpreter receives the tokens, it generates AST (Abstract Structure tree) which coverts to byte code and then byte code can be saved in (.py) extension.

At last, by using Python Virtual Machine, interpreter loads the machine language and PVM converts in into 0s and 1 s which prints the results.'''
