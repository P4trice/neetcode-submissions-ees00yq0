class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < low:
                return nums[i]
        return nums[0]