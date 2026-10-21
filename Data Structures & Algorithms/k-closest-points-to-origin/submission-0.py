class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        output = []
        k_points = []

        for point in points:
            x, y = point[0], point[1]
            distance = math.sqrt((x)**2 + (y)**2)
            k_points.append((distance, x, y))
        
        heapq.heapify(k_points)

        for i in range(k):
            vals = heapq.heappop(k_points)
            x, y = vals[1], vals[2]
            output.append([vals[1], vals[2]])
        
        return output