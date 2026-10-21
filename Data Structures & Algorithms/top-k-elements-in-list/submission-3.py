class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kMap = defaultdict(int)
        res = []
        output = []

        for i in nums:
            kMap[i] += 1
        
        for num, freq in kMap.items():
            res.append((-freq, num))
        
        heapq.heapify(res)

        for i in range (k):
            x = heapq.heappop(res)[1]
            output.append(x)
        
        return output

            