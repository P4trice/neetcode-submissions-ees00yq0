class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sequence consecutive but can have in-between elements
        if len(nums) == 0:
            return 0
        nums.sort()
        longest_seq = 1
        current_seq = 1
        current = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == current:
                pass
            elif nums[i] == current + 1:
                current_seq += 1
                if current_seq > longest_seq:
                    longest_seq = current_seq
            else:
                current_seq = 1
            current = nums[i]

        return longest_seq
