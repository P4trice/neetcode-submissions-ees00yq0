class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = {}
        for i  in range(len(numbers)):
            if target - numbers[i] in m:
                return [m[target-numbers[i]]+1, i+1]
            else:
                m[numbers[i]] = i
        return [0,1]