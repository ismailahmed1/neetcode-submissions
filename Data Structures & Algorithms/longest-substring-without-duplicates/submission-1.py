class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = deque()
        seen = set()
        max_length = 0

        for ch in s:
            if ch not in seen:
                seen.add(ch)
                curr.append(ch)
            else: 
                while ch in curr: 
                    x = curr.popleft()
                    seen.remove(x)
                curr.append(ch)
                seen.add(ch)
            max_length = max(max_length, len(curr))
            
        return max_length
