# https://leetcode.com/problems/longest-consecutive-sequence/description/

# Approach 1 
# Sorting

def longest_consecutive_sequence(nums):
    
    if len(nums) == 0:
        return 0

    nums.sort()

    longest_seq = 1
    current_streak = 1 

    for i in range(1, len(nums)):

        if nums[i] == nums[i-1]+1:
            current_streak += 1
            longest_seq = max(current_streak, longest_seq)
        elif nums[i] == nums[i-1]:
            pass
        else:
            current_streak = 1

    return longest_seq

# Approach 2
# Hashset

def _longest_consecutive_sequence(nums):

    # we can safely convert list to a set since we need to count repeating numbers only once.
    _nums = set(nums)
    longest_seq = 0

    for num in nums:

        # this shows that num-1 is part of a longer sequence already.
        if num-1 not in _nums:

            current_seq = 1
            current_num = num

            while current_num+1 in _nums:
                current_seq += 1
                current_num += 1

            longest_seq = max(current_seq, longest_seq)
    
    return longest_seq