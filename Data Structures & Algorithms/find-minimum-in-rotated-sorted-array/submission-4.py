class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = nums[0]
        hi = len(nums) - 1
        lo = 0
        while lo <= hi:
            mid = (hi + lo) // 2
            if nums[mid] < low:
                hi = mid
                low = nums[mid]
            else:
                lo = mid + 1
            
        return low
