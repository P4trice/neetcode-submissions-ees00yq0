class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minimum = nums[0]
        lo = 0
        hi = len(nums) - 1
        offset = 0
        while lo < hi:
            offset = (lo + hi) // 2
            if nums[offset] < nums[hi]:
                minimum = nums[offset]
                hi = offset
            else:
                lo = offset + 1
        offset = lo
        print(offset)

        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            logical_mid = (lo + hi) // 2
            mid = (logical_mid + offset) % len(nums)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = logical_mid + 1
            else:
                hi = logical_mid -1

        return -1