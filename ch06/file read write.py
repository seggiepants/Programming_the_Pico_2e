f = open('test.txt', 'w')
f.write(str(1))
f.close()

f = open('test.txt', 'r')
print(f.read())
f.close()