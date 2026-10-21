class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreq = defaultdict(int)
        heap = []

        time = 0 

        for task in tasks:
            taskFreq[task] += 1

        for freq in taskFreq.values():
            heap.append(-freq)
        
        heapq.heapify(heap)
        q = deque()

        while heap or q:
            time += 1
            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt:
                    q.append((cnt, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        
        return time




