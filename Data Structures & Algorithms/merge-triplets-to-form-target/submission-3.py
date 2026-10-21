class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = set()

        for i in range(len(triplets)):
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                continue
            for k in range(3):
                if triplets[i][k] == target[k]:
                    found.add(k)
        
        return len(found) == 3