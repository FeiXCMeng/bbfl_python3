from sys import argv

script, filename = argv
print("we will rewrite the {}." .format(filename))
print("first, opening the file.")
target = open(filename, 'w')

print("then turncate the file.")
target.truncate()

print("now, you can write three words.")
line1 = input("line1 is:")
line2 = input("line2 is:")
line3 = input("line3 is:")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
# target.write(line2 + "\n")
# target.write(line3 + "\n")

print("at last, we must close the file")
target.close()
