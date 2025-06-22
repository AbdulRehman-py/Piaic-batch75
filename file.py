from os import read


with open('file.txt', 'w') as file:
    file.write('just a simple message doing some practice to learn python\n' \
    'this is a second line\n' \
    'this is a third line\n')



with open('file.txt', 'r') as file:
    content = file.readlines()
    fileline = content[1]
    print(fileline)


