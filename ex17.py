from sys import argv
script, from_file, to_file = argv

old_file = open(from_file, 'r')
data = old_file.read()
new_file = open(to_file, 'w')
new_file.write(data)

old_file.close()
new_file.close()
