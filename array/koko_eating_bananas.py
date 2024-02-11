# https://leetcode.com/problems/koko-eating-bananas/description/

# Approach - binary search
# Time complexity = O(nlogm) where n is the number piles and m is the higest no of bananas among the piles.

import math

def get_min_rate(piles, h):

    def check_rate(rate):
        """
        Find the total time to finish the pile with the give rate
        """
        total_time = 0

        for pile in piles:

            if total_time > h:
                break
            # add the time to completely finish the pile
            total_time += math.ceil(pile/rate)

        if total_time <= h:
            return True
        else:
            return False
    
    l = 1
    # largest number of bananas in the pile
    r = max(piles)

    min_rate = r

    while l <= r:

        mid = (l+r)//2

        if check_rate(mid):
            min_rate = min(min_rate, mid)
            r = mid - 1
        else:
            l = mid + 1

    return min_rate