class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        output = []
        point_arr = []
        for point in points:
            dist = math.sqrt((point[0])**2 + ((point[1])**2))
            point_arr.append((dist, point[0], point[1]))
        
        heapq.heapify(point_arr)

        while k > 0:
            point = heapq.heappop(point_arr)
            xy_pair = [point[1], point[2]]
            output.append(xy_pair)
            k -= 1
        
        return output
