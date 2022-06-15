from datetime import datetime as dt
# 15 6 
x = '2022-06-09'

def datecalc(lent, curmon, curdate):
    dadd = 0
    lent_month = int(lent[5:7])
    lent_day = int(lent[8:])
    for i in range(lent_month, curmon):
        

        if i == 2:
            dadd += 28
        elif i == 8:
            dadd += 31
        elif i == 9:
            dadd += 30
        elif i == 10:
            dadd += 31
        elif i == 11:
            dadd += 30
        elif i == 12:
            dadd += 31
        elif i % 2 == 0:
            dadd += 30
        else:
            dadd += 31
    
        curdate = curdate + dadd
        return( curdate - lent_day)
    
monthnow = dt.now().month
print(monthnow)
daynow = dt.now().day

print(datecalc(x, monthnow, daynow ))
