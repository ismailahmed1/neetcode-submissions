class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqCount = defaultdict(int)

        for n in nums:
            freqCount[n] += 1
            if freqCount[n] > (len(nums) / 2):
                return n 