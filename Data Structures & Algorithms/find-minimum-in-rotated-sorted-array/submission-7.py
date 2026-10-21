class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0]:
            return nums[0]

        l, r = 0, len(nums) - 1
        min_elem = nums[0]

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1 
            else:
                r = mid - 1

            min_elem = min(min_elem, nums[mid])
            
        return min_elem
