class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccMap = defaultdict(int)
        output = []

        for i in range(len(s)):
            lastOccMap[s[i]] = i 
        
        window_size = 0 
        max_reach = 0
        for i in range(len(s)):
            window_size += 1
            max_reach = max(lastOccMap[s[i]], max_reach)

            if max_reach == i:
                output.append(window_size)
                window_size = 0

        return output
            

                    
