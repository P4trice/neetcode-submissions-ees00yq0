class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:          # ✅ clean termination
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                hi = mid - 1     # ✅ exclude mid
            else:
                lo = mid + 1
        return -1
