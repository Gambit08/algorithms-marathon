# https://leetcode.com/problems/top-k-frequent-elements/description/
# Approach 1
# Create a hashmap of each num and its corresponding frequency
# Sort the hashmap based on it's values(frequency) in descending order and gets it first 'k' key-value pairs.
# Cast the map keys to list and return.
# Time Complexity -> O(nlogn)

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

    sorted_num_freqs = {k: v for k, v in sorted(num_freq.items(),
                        key=lambda d: d[1], reverse=True)[0:k]}
    return list(sorted_num_freqs.keys())

# Approach 2
# Bucket sort

def _topKFrequent(self, nums: List[int], k: int) -> List[int]:

    bucket = [[] for i in range(len(nums)+1)]

    num_freq = {}
    
    for num in nums:
        if num in num_freq:
            num_freq[num] += 1
        else:
            num_freq[num] = 1

    for num, freq in num_freq.items():
        bucket[freq].append(num)

    res = []
    for i in range(len(bucket),0,-1):

        item = bucket[i]

        for num in item:
            if k > 0:
                res.append(num)
                k -= 1
            else:
                break
    
    return res


