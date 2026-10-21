class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_elem = nums[0]

        while l <= r:
            if nums[r] > nums[l]:
                min_elem = min(min_elem, nums[l])
                break

            m = (l + r) // 2
            min_elem = min(min_elem, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1


        return min_elem