filename = 'learning_python.txt'
"""Reading entire contents of file"""
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)


file_name = 'learning_python.txt'
"""Looping over file_object"""
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())


my_file = 'learning_python.txt'

"""Storing lines in a list, outside of the with block"""
with open(my_file) as file_object:
    lines = file_object.readlines()

file_string = ''
for line in lines:
    file_string += line.rstrip()

print(file_string)
print(len(file_string))

my_new_file = 'learning_python.txt'

with open(my_new_file) as file_object:
    lines = file_object.readlines()

file_str = ''
for line in lines:
    file_str += line.replace('Python', 'Javascript')


print(file_str)