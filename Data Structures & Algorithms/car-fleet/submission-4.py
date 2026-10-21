class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleets = 0
        lead_time = 0 
        
        pairs = [(p,s) for p,s in zip(position, speed)]
        pairs.sort(reverse=True)


        for p,s in pairs: 
            time = (target - p) / s
            if time > lead_time:
                fleets += 1
                lead_time = time
        
        return fleets