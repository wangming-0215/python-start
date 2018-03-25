file_name = 'files/learn_python.txt'

with open(file_name) as file_object:
    contents = file_object.read().replace('python', 'javascript')
    print(contents)
