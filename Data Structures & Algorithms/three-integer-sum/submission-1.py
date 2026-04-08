class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums)):
            m = set([])
            if i > 0 and nums[i] == nums[i-1]:
                continue
            temp = nums[i+1:]
            prev_j = None
            for j in temp:
                if j == prev_j:
                    continue
                if -nums[i] - j in m:
                    output.append([nums[i], j, -nums[i]-j])
                    prev_j = j
                m.add(j)
        return output