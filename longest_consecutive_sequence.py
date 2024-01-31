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