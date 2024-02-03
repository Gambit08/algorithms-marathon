# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Find the length of longest substring without repeating characters
# abcabcbb, the answer would be 3 since 'abc' is longest substring with non repeating characters.

# Approach 1
# Brute force 

def longest_sequence(s):
    
    longest_sub = 0

    if len(s) <= 1:
        return len(s)

    for i in range(len(s)):

        seen = set()

        for j in range(i, len(s)):

            if s[j] not in seen:
                seen.add(s[j])
                longest_sub = max(longest_sub, j-i+1)
            else:
                break

    return longest_sub

# Approach 2
# Sliding window

def _longest_sequence(s):

    if len(s) <= 1:
        return len(s)
    
    longest_sub = 0
    seen = set()
    j = 0
    i = 0

    while j < len(s):

        while s[j] in seen:
            seen.remove(s[i])
            i += 1
        
        seen.add(s[j])
        longest_sub = max(longest_sub, j-i+1)
        j += 1

    return longest_sub

    