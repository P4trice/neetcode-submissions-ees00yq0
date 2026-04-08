class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxes = []
        d = deque()
        #nums=[1,2,1,0,4,2,6]
        
        for i in range(len(nums)):
            while d and nums[d[-1]] < nums[i]: 
                # if d has an entry, remove the rightest element as long 
                # as the element is smaller than the currently viewed i
                d.pop() #pop from right
            
            # 2. Add current index
            d.append(i)
            
            # 3. Remove from front if it's outside the window
            if d[0] < i - k + 1:
                d.popleft()
            
            # 4. Once i >= k-1, we have a full window — record the max
            if i >= k - 1:
                maxes.append(nums[d[0]])

        return maxes