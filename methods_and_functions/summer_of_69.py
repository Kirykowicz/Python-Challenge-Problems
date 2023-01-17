def summer_69(lst):
    total = 0
    add = True
    for num in lst:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False 
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total 

    
print(summer_69([1,2,6,8,9,10]))