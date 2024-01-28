# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# Constraints
# Array is sorted and soln must only use constant extra space.

# Approach
# Two pointers apprach seems to be suitable for this problem specially when we are only allowed to use constant extra space and the array is sorted.
# We can have two pointers at the start and the end of the array respectively.
# We sum these two elements and compare with out target.
# If the sum is greater than the target, we move our right pointer to the left.
# Conversely, if the sum is lesser than the targer, we move our left pointer to the right.
# We continue until the left index is lesser than the right index.
# Space complexity O(1) - additional space is only used to store two indices.
# Time complexity O(n) - array is only traversed once.

def two_sum_ii(numbers, target):
    
    l = 0
    r = len(numbers)-1

    # note that we cannot use the same element twice.
    while l < r:

        if numbers[l] + numbers[r] == target:
            return [l+1,r+1]
        elif numbers[l] + numbers[r] < target:
            l = l+1
        else:
            r = r-1

    return [-1.-1]