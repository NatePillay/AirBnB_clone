Write a README.md:
description of the project
description of the command interpreter:
how to start it
how to use it
examples



The project was developed using Python


All Unit test files were created in the test folder to test each executable piece of code as there were many classes created in order to create this project.

The class attributes and methods are all labelled with a short description in the executable .py files

BaseModel:
the beginning point
assign a UUID, update and create time, important for any user entering the app
we then had to convert that data as recieved into a format that would be easy to store/

ISOFORMAT on Datetime

Part i had a hard time with and still working through:
Now we can recreate a BaseModel from another one by using a dictionary representation:

<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
It’s great but it’s still not persistent: every time you launch the program, you don’t restore all objects created before… The first way you will see here is to save these objects to a file.

Writing the dictionary representation to a file won’t be relevant:

Python doesn’t know how to convert a string to a dictionary (easily)
It’s not human readable
Using this file with another program in Python or other language will be hard.
So, you will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.

Now the flow of serialization-deserialization will be:

<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
Magic right?

Terms:

simple Python data structure: Dictionaries, arrays, number and string. ex: { '12': { 'numbers': [1, 2, 3], 'name': "John" } }
JSON string representation: String representing a simple data structure in JSON format. ex: '{ "12": { "numbers": [1, 2, 3], "name": "John" } }'


The console was also challenging but good lessons to be learning. I had a problem when executing my console as it could not work with the serialization

Creating classes for user was good

AUTHOR NATHAN PILLAY
