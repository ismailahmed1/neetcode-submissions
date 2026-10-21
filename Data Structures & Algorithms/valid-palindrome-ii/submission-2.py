class Solution:
    def validPalindrome(self, s: str) -> bool:
        usedDelete = False
        def isPalindrome(l, r) -> bool:
            while l < r:
                print(l, r)
                if s[l] != s[r]:
                    return False
                r-= 1
                l+= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r] and usedDelete:
                return False
            elif s[l] != s[r]:
                pushL = isPalindrome(l+1, r)
                pushR = isPalindrome(l, r-1)
                return pushL or pushR
                usedDelete = True
            l += 1
            r -= 1
        return True
            
            



            