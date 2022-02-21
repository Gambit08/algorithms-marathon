# left -> index of the last number picked from the left side of the array, nums.
# i -> index of the last multiplier picked from the multiplier array.
# (i - left) -> number of elements picked from the right side of array.
# right -> index of the last number picked from the right side of the array, nums. n - (i-left) -1


def maximumScore(nums: List[int], multipliers: List[int]) -> int:
    
    n = len(nums)
    m = len(multipliers)
    memo = [[0] * (m + 1) for _ in range(m + 1)]
    def dp(i, left):
        # Base case
        if i == m:
            return 0
        
        right = n - (i-left) - 1

        if not memo[i][left]:
            memo[i][left] = max(nums[left]*multipliers[i] + dp(i+1, left+1), nums[right]*multipliers[i] + dp(i+1, left))

        return memo[i][left]
        
    return dp(0, 0)


print(maximumScore([1,2,3], [3,2,1]))