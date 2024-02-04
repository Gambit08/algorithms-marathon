# https://leetcode.com/problems/longest-repeating-character-replacement/description/

# s = ABABCC, k = 2
# AAAA or BBBB, answer = 4


def longest_repeating(s: str, k: int):

    freq = {char: 0 for char in s}

    i = 0
    j = 0

    longest_seq = 0

    while j < len(s):
        
        freq[s[j]] = freq[s[j]] + 1

        # check if valid window
        if j-i+1 - max(freq.values()) > k:
            # replacements cannot be made so we shrink the window
            # in addition to that we also update the freq
            while i <= j:
                freq[s[i]] -= 1
                i += 1
        
        longest_seq = max(longest_seq, j-i+1)
        j += 1
    
    return longest_seq