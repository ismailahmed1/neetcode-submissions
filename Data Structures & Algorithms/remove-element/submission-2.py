class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[r] == val:
                r -= 1
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
        
        return l
        


    

        # if r pointer on val, decrease r 
        # if l pointer on val, swap r and l 