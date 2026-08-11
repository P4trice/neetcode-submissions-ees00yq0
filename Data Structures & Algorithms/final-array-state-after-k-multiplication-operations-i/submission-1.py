class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            index = -1
            temp = 200
            for j in range(len(nums)):
                if nums[j] < temp:
                    index = j
                    temp = nums[j]
            
            nums[index] = nums[index] * multiplier


        return nums