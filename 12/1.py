file = open(r'.\proj1.txt', 'r')
fileObj = file.read()
x = fileObj.replace(' ', '#')
print(x)
