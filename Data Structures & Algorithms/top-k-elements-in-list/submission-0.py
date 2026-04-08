class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        occurances = {}
        for num in nums:
            if num in occurances:
                occurances[num] += 1
            else:
                occurances[num] = 1
            
        occurances = list(occurances.items())
        occurances_sorted = sorted(occurances, key= lambda num:num[1], reverse=True)
        print(occurances_sorted)
        result = []
        for i in range(k):
            result.append(occurances_sorted[i][0])
        return result