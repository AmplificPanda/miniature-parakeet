**Python Questions and Answers**
- What is the difference between a module and a package in python.?
Each pythion program is a module that imports other modules like objects and attributes,
thus a module is a way to structure a program. The folder of a python program is called a package of modules.

- Built in types avl in Python?
  There are mutable and immutable built in types in python... the mutable(changable) ones include
  lists, sets, dictionaries...immutable types include strings, tuples and numbers.  

- Difference between list and tuple?
  The list is mutable and the tuple is immutable. 
  Tuples can be hashed, as in the case of making keys for dictionaries.

- What is the difference between pickling and unpickling?
  In python, the pickle module accepts any python object, transforms it into a string representation and dumps it
  into a file using the dump function. This is known as pickling, done by pickle.dump(). Unpickle to reverse this is
  pickle.load() 

- A python decorator is a specific change made in the Python syntax for the easy alteration of functions.

- What is the difference between generators and iterators?
  Iterators are used to iterate over a group of elements (such as in a list). The way of implementing these iterators are known as generators, it yields an expression in the function but behaves like a normal function. 

- How to convert a number into a string?
  We can use the built in str() function for an octal or hexadecimal function. We can also use oct() or hex()

- What is the use of the // operator in Python?
  Using the // operator such as 14//2 = 7 ...gives the quotient when the numerator is divided by the denominator. 
  It is called the floor division operator. 

- Does Python have a switch or case statement like in C?
  No it does not, however we can make our switch function.

- What is the range() function? 
 The range function is used to generate a list of numbers, only integers are allowed. Parameters can be both
 negative and positive. Range(<start>, stop, <step>)

- What is the == in Python?
 It is an operator to check or compare the values of two objects. 

- Does Python have a main() function?
 Yes it executes whenever we run the python script.

- What is GIL?
  GLI is a Global Interpreter Lock which is a mutex(mutal exclusion), that is used to limit access to Python objects. 
  It synchronises threads and prevents them running at the same time.

- Before the 'in' operator, which method was used to check the presence of a key in a dictionary?
 has_key() method.

 - How do you change the data type of a list?'
 To change the list into a tuple? use the tuple() function. Similarily we can use set(), and dict() functions.
 .join() function for to change to string.

 - What are the key features of Python?
  Interpreted, dynamically typed, object orientated and english-like syntax.

- Is Python case sensitive? Yes

- Is python an OOP language? Yes, we can create classes and objects.

- Name some commonly used built in modules in Python?
  OS, sys, math, random, data time, JSON, print, 
 
- Explain self in Python?
 In Python self is a keyword used to define an instance or object of a class. Helps to distinguish the methods and attributes of a class from its local variables. 

- Indentation? Neccessary for Python and helps to specify a block of code.

- Explain the difference between Python arrays and lists?
 In python, both arrays and lists are used to store data. Arrays contains elemens of the same data types, whereas lists can consist of many different data types.

- What is __init__?
  A method or constructor which is auto called to allocate memory when a new obj or instance of a class is created. All classes have this method. 

- How to write comments?
  '#' character, but also using >>># 

- How can you capitalise the first letter of a string?
  Can utilize the capitalize() method to capitalize the first letter of a string. Will return original string if already capital.

- Explain the functions of is, not and in operators?
  in: checks if some element is present in some sequence. 
  is: returns true when when two operands are true
  not: returns the inverse of the boolean value

- What is a statement in python?
 It is an instruction that python can interpret and execute, type statement in command line, python executes and displays result.

- How do you do data abstraction in Python?
  Abstraction is hiding away information or showing information that is only necessary, 
  e.g. through private/public declarations...

- What are functions?
  Functions are a set of codes used when we want to run the same method for more than 1 time. It reduces length of program.
  Defined in two categories: Definition and function calling. 