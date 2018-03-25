file_name = 'files/learn_python.txt'

with open(file_name) as file_object:
    print(file_object)
    contents = file_object.read()
    print(contents)

print('---------------------------')

with open(file_name) as file_object:
    for line in file_object:
        print(line)

print('---------------------------')

lines = []
with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)
