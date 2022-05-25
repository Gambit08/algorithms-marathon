# Leetcode #242
# Check if a string is a valid anagram of another.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

def isAnagram(self, s: str, t: str) -> bool:
    alphabet_array = [0] * 26
    
    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        alphabet_array[ord(s[i]) - ord('a')] += 1
        alphabet_array[ord(t[i]) - ord('a')] -= 1
        
    for count in alphabet_array:
        if count is not 0:
            return False
    
    return True

# Time Complexity of the Soln is O(N) where N is the length of the input strings (s/t)