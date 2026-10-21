class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for i in nums:
            count[i] += 1
        
        max_heap = []
        for num, freq in count.items():
            max_heap.append((-freq, num))
        
        heapq.heapify(max_heap)

        output = []
        for i in range(k):
            x = heapq.heappop(max_heap)[1]
            output.append(x)
        
        return output