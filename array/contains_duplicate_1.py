# Leetcode #217 
# Time complexity -> O(N) where N is the size of input list.

def containsDuplicate(self, nums: List[int]) -> bool:
    """
    Checks to see if the list contains a duplicate.
    """
    hashset = set()
    for num in nums:
        # Time complexity -> O(1)
        # https://wiki.python.org/moin/TimeComplexity
        if num in hashset:
            return True
        else:
            hashset.add(num)
    return False