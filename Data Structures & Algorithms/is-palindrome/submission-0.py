class Solution:
    def isPalindrome(self, s: str) -> bool:
        is_reversed = ''.join(reversed(s))
        
        lst_1 =[]
        lst_2 = []

        for i in s:
            if i.isalnum():
                lst_1.append(i.lower())
        
        for i in is_reversed:
            if i.isalnum():
                lst_2.append(i.lower())

        
        return (lst_1 == lst_2)
