# https://leetcode.com/problems/container-with-most-water/description/

# Approach 1
# Brute force but TLE

def max_water(height):

    max_area = 0

    for i in range(len(height)):

        for j in range(i+1, len(height)):

            area = abs(j - i) * min(height[i], height[j])

            max_area = max(max_area, area)

    return max_area

# Approach 2
# Two pointers

def max_water(height):
    
    max_area = 0
    i = 0
    j = len(height) - 1

    while i < j:

        if height[i] <= height[j]:
            area = height[i] * abs(j-i)
            i += 1
        
        else:
            area = height[j] * abs(j-i)
            j -= 1
        
        max_area = max(area, max_area)

    return max_area