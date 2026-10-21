class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_fleet = []
        target_stack = []
        fleet_count = 0

        for i in range (len(position)):
            sorted_fleet.append((position[i], speed[i]))
        
        sorted_fleet.sort(key=lambda tup: tup[0], reverse=True)

        #sorted_fleet = [[7,1], [4,2], [1,2], [0,1]], target = 10

        for i in sorted_fleet:
            if target_stack and ((target - i[0]) / i[1]) <= ((target - target_stack[-1][0]) / target_stack[-1][1]):
                continue
            else:
                fleet_count += 1
                target_stack.append(i)
        
        return len(target_stack)


        


        

