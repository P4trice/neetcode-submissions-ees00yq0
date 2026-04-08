class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        current_max = min(heights[i], heights[j]) * (j - i)
        while i != j:
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
            
            temp = min(heights[i], heights[j]) * (j - i)
            if current_max < temp:
                current_max = temp
        return current_max