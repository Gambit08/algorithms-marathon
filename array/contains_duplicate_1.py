# Leetcode#217 Contains Duplicate
def containsDuplicate(self, nums: List[int]) -> bool:
    hashset = set()
    for num in nums:
        # Time complexity is O(1)
        # https://wiki.python.org/moin/TimeComplexity
        if num in hashset:
            return True
        else:
            hashset.add(num)
    return False