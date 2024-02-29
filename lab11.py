def counter(nums, target): 
    hashmap = {}    
    for i, n in enumerate(nums): 
        if n in hashmap:
            return [hashmap[n], i]  
        hashmap[target - n] = i    
    return -1   
print(counter(nums = [2,7,11,15], target = 9)) 
