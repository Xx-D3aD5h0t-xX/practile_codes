f = open(r'./study/result.txt', 'r+').readlines()
for i in range(0, len(f)):
    print(f'{i}) {f[i]}')
print(f'Total lines: {len(f)-1}')
