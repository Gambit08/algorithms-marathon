# https://leetcode.com/problems/permutation-in-string/

# Approach 1 
# Brute Force

def check_string_permutation_1(s1, s2):

    _s1 = ''.join(sorted(s1))

    for i in range(len(s2)):

        j = i + len(s1) 

        # check if a valid permutation
        sub = s2[i:j]
        if _s1 == ''.join(sorted(sub)):
            # valid permutation
            return True
    
    return False


# Approach 2
# HashMap

def check_string_permutation_2(s1, s2):

    def matches(freq1, freq2):
        for i in range(26):

            if freq1.get(chr(i+ord('a')), 0) - freq2.get(chr(i+ord('a')), 0) != 0:
                return False
        
        return True

    freq1 = {}

    for char in s1:
        freq1[char] = freq1.get(char, 0) + 1

    for i in range(len(s2)-len(s1)+1):

        freq2 = {}

        for j in range(len(s1)):

            freq2[s2[i+j]] = freq2.get(s2[i+j], 0) + 1

        if matches(freq1, freq2):
            return True

    return False        

# Approach 3
# HashMap

def check_string_permutation_3(s1, s2):

    freq1 = [0]*26
    freq2 = [0]*26

    if len(s1) > len(s2):
        return False
        
    def matches(freq1, freq2):

        for i in range(26):

            if freq1[i] - freq2[i] != 0:
                return False
        
        return True

    for i in range(len(s1)):
        freq1[ord(s1[i]) - ord('a')] += 1
        freq2[ord(s2[i]) - ord('a')] += 1

    for i in range(len(s2)- len(s1)):

        if matches(freq1, freq2):
            return True
        
        freq2[ord(s2[i+len(s1)]) - ord('a')] += 1
        freq2[ord(s2[i]) - ord('a')] -= 1
    
    return matches(freq1, freq2)
