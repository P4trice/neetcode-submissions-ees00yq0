class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        flag = True
        i = 0
        print("original: ", nums)
        while flag:
            if i + 1 == nums[i]:
                i += 1
                print("nothing: ", nums)
            else:
                print("pre: ", nums)
                # swap
                temp = nums[i]
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp
                print("post: ", nums)
                if nums[i] == temp:
                    return temp
                else:
                    pass
            if i == len(nums):
                flag = False
            
        return -1