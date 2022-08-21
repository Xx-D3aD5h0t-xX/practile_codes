#num = int(input("Enter any number: "))
num = 2**135
old_num = num
count = 0

big_loop = True
while big_loop:
    num = old_num
    loop = True
    max = 0

    while loop:
        if num != 1:
            if num % 2 == 0:
                num = num/2
                count += 1
            else:
                num = (3*num) + 1
                count += 1
            if num > max:
                max = num
        else:
            loop = False
    if max > 1000000000:
        big_loop = False
    else:
        old_num += 1
        print(f'failed num: {old_num}')

print('-'*40)
print(f'The Number Was: {old_num}')
print(f'The Max Number reached: {max}')
print(F'The Number Of Iterations: {count}')
print(num)
print('-'*40)
