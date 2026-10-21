class Solution:
    def validPalindrome(self, s: str) -> bool:
        usedDelete = False
        def isPalindrome(s: str, l, r) -> bool:
            l, r = l, r
            while l < r:
                while not s[l].isalnum() and l < r:
                    l+=1
                while not s[r].isalnum() and l < r:
                    r-=1
                if s[l] != s[r]:
                    return False
                r-= 1
                l+= 1
            return True

        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            if s[r] == s[l]:
                l += 1
                r -= 1
            else:
                return isPalindrome(s, l, r - 1) or isPalindrome(s, l + 1, r)
            
        return True
            
            



            