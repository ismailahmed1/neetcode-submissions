class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqList = [ [] for i in range (len(nums)+ 1)]

        freqMap = defaultdict(int)

        for i in nums:
            freqMap[i] += 1

        for n, freq in freqMap.items():
            freqList[freq].append(n)
        

        res = []
        for i in range (len(freqList) - 1, -1, -1):
            for j in freqList[i]:
                res.append(j)
                k -= 1
                if k == 0:
                    return res
                else:
                    continue
        
        return []
