class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0 and len(nums2) == 0:
            return 0.0

        if len(nums1) == 0:
            if len(nums2) % 2 == 1:
                return nums2[len(nums2)//2]
            else:
                return (nums2[len(nums2)//2] + nums2[len(nums2)//2 - 1]) / 2

        if len(nums2) == 0:
            if len(nums1) % 2 == 1:
                return nums1[len(nums1)//2]
            else:
                return (nums1[len(nums1)//2] + nums1[len(nums1)//2 - 1]) / 2

        k = (len(nums1) + len(nums2)) // 2

        # Make nums1 always be the short array
        if (len(nums1) > len(nums2)):
            temp = nums1
            nums1 = nums2
            nums2 = temp

        lo = 0
        hi = len(nums1)

        while lo <= hi:
            i = (hi + lo) // 2
            j = k - i

            nums1_left  = nums1[i-1] if i > 0 else float('-inf')
            nums1_right = nums1[i]   if i < len(nums1) else float('inf')
            nums2_left  = nums2[j-1] if j > 0 else float('-inf')
            nums2_right = nums2[j]   if j < len(nums2) else float('inf')

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                left = max(nums1_left, nums2_left)
                right = min(nums1_right, nums2_right)
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return right
                else:
                    return (left+right)/2
                
            if nums1_left > nums2_right:
                hi = i - 1
            else:
                lo = i + 1

        return 0.0