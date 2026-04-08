class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = []
        current_max = 0
        for i in range(len(height)):
            max_left.append(current_max)
            if height[i] > current_max:
                current_max = height[i]

        max_right = []
        current_max = 0
        for i in range(len(height)-1, -1, -1):
            max_right.insert(0, current_max)
            if height[i] > current_max:
                current_max = height[i]

        volume = 0
        for i in range(len(height)):
            temp = max((min(max_left[i], max_right[i]) - height[i]), 0)
            print("i: ", i, ": max_left: ", max_left[i], ", max_right: ", max_right[i], " => vol: ", temp)

            volume += max((min(max_left[i], max_right[i]) - height[i]), 0)

        return volume