class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print("slow: ", slow)
            print("fast: ", fast)
            if fast == slow:
                print("break")
                break
        
        fast = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            print("slow: ", slow)
            print("fast: ", fast)
        
        return slow