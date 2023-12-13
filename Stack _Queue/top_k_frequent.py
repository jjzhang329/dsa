# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# 347. Top K Frequent Elements https://leetcode.com/problems/top-k-frequent-elements/description/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        top = []
        for key, freq in count.items():
            heapq.heappush(top, (freq, key))
            if len(top) > k:
                heapq.heappop(top)

        res = []

        while len(res) < k:
            res.append(heapq.heappop(top)[1])
        return res