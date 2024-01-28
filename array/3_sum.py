# https://leetcode.com/problems/3sum/editorial/

# Constraints
# find ALL triplets such that their sum is equal to 0
# i != j , i != k and j != k
# Soln must not contain duplicate triplets.

# Approach
# We can tackle this by following the two_sum problem approach, specifically two_sum_ii problem since it involves sorting.
# Sorting the array beforehand is important to deal with the requirement of not having duplicate triplets.
# For each element in the array.
# If we have seen that element before we can continue in order to avoid duplicate triplets.
# If the current element is greater than zero that we can return since we cannot expect its compliment ahead as the array is sorted in ascending order.
# Otherwise, we run the two_sum_ii on rest of the elements with the target being the compliment of current number.

def three_sum(nums:list):
    
        
    # sort the nums array
    nums.sort()

    # define function to be reused.
    def two_sum_ii(i, l, r, target):
        # note that we cannot use the same element twice.
        while l < r:

            if nums[l] + nums[r] == target:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                # avoid duplicates
                # consider a edge case [-2,0,0,2,2]
                # i = 0, l = 1, r = 4
                # on the next iteration it's going to consider  0 and 2 nums pair again at pos 2 and pos 3 if below snippet was not put.
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif nums[l] + nums[r] < target:
                l = l+1
            else:
                r = r-1

        return res
    

    res = []
    size = len(nums)

    for i in range(size):

        if nums[i] > 0:
            break
        
        # consider a edge case
        # note first is for the scenario where every number is same
        # [2,2,2,2,2], in such case we need to consider the num one time.
        if i != 0 and nums[i] == nums[i-1]:
            continue

        two_sum_ii(i, i+1, size-1, -nums[i])


    return res

        


