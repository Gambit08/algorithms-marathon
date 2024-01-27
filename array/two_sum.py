# https://leetcode.com/problems/two-sum/description/

# Approach 1
# two pass
# In the first pass, create a hashmap of each element and its corresponding index in the array
# In the second pass, iterate over each element in the array.
# For each element find its compliment by subtracting it from the target value.
# Check if that compliment exists in the hashmap and it's index is not the current index in the iteration (ensure we do not choose the same element twice.)
# If true, we return the array with two values being the current and it's compliment's index. (only one result exists)

def two_sum_1(nums, target):
    
    index = {}
    for i, num in enumerate(nums):
        index[num] = i
    
    for i, num in enumerate(nums):
        compliment = target - num
        if compliment in index and index[compliment] != i:
            return [i, index[compliment]]