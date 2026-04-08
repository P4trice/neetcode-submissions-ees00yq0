class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current_max = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                temp = (j-i) * (min(heights[i], heights[j]))
                if temp > current_max:
                    current_max = temp
        return current_max