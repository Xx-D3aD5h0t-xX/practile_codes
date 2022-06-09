# Second Code

vowelCount = 0
consoCount = 0
upperCount = 0
lowerCount = 0


file = open(r'./proj.txt', 'r')
x = file.read()
for i in range(0, len(x)):

    if x[i] in 'aeiou':
        vowelCount += 1

    if x[i] not in 'aeiou1234567890, ./"()[]}{':
        consoCount += 1

    if x[i].isupper():
        upperCount += 1

    if x[i].islower():
        lowerCount += 1


print('Vowels:', vowelCount)
print('Consonant:', consoCount)
print('Upper:', upperCount)
print('Lower:', lowerCount)
