class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1 
        
        heap = []
        for i in count.keys():
            heapq.heappush(heap, (count[i], i))
            if len(heap) > k:
                heapq.heappop(heap)
        
        arr = []
        for i in range (k):
            arr.append(heapq.heappop(heap)[1])
        
        return arr