nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):
    hashmap = {} 
    for index, number in enumerate(nums):
        complement = target - number
        if complement in hashmap:
            return [hashmap[complement], index]  
        hashmap[number] = index
    return "Not valid" 

print(two_sum(nums, target))
