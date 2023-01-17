def has_33(array):
    for i in range(1, len(array) - 1):
        if array[i] != 3:
            continue
        else:
            if array[i - 1] == 3 or array[i + 1] == 3:
                return True 
    return False 



# alternate less complicated solution

def has_33_alternate(array):
    for i in range(0, len(array) -1):
        if array[i] == 3 and array[i + 1] == 3:
            return True 
        
    return False 

print(has_33_alternate([1,2,3,3]))