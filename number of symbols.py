filename = input('Please type a file name (For  example - name.txt) : ')

file = open(filename, 'r')
print('In this file ' + str(len(file.read())) + ' symbols.')

file.close()