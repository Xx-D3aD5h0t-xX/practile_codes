l = [79,42,51,21,18,69]
# Var init
small_no = l[0] 
large_no = 0

for i in l:
    if i <= small_no:
        small_no = i
    if i >= large_no:
        large_no = i
print("The Smallest Number in the List is:", small_no)
print("The Largest Number in the List is:", large_no)




