class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # (start_index, height)
    
        for i, h in enumerate(heights):
            start = i
            while stack and heights[i] < stack[-1][1]:  # when do you pop?
                idx, height = stack.pop()
                max_area = max(max_area, (i-idx)*height)  # area formula
                start = idx  # inherit the start index
            stack.append((start, h))
    
        # finish the stack
        for start, height in stack:
            max_area = max(max_area, (len(heights)-start)*height)  # what's the width here?
    
        return max_area