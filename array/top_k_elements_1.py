# Leetcode #347
# Time Complexity - > O(nlogn)

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    """
    Gets the frequency for each number in the list, sorts them in descending order
    & returns the first k elements int he computed list.
    """
    num_freq = {}
    for num in nums:
        if num in num_freq:
            num_freq[num] += 1
        else:
            num_freq[num] = 1
            
    sorted_num_freqs = {k:v for k,v in sorted(num_freq.items(), key = lambda d: d[1], reverse=True)} 
    sorted_freqs = sorted_num_freqs.keys()
    return list(sorted_freqs)[0:k]