# >>> used in the book will indicate that the following text shown is being used in a terminal / python interpretter
print("Hello Python world!")

#chapter describes installing python and vscode

#python is the command to start the interpretter in a shell. it could also be python3 or py, whatever else you alias
#use >>> python src/chapter_1/hello_world.py to run this program
#or use >>> python3 src/chapter_1/hello_world.py

#install the python extension in vscode to get syntax highlighting and intellisense

#more resources for the book is available at ehmatthes.github.io/pcc_3e

message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

# following produces error because the variable reference is not spelled correctly: name not defined
message = "Hello Python Crash Course reader!"
# print(mesage)

#following is not required for program to close - just discussed in the chapter so I thought I'd put it here as a reminder
#this is one method of exitting from the interactive python interpretter
exit()