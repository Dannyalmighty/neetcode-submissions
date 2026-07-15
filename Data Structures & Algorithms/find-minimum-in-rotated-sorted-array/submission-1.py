"""
[3,4,5,1,2]
 l
     m
         r

"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                # minimum is to the r of m
                l = m + 1
            else:
                # minimum is at m or to the l
                r = m

        return nums[l]


        # l, r = 0, len(nums) - 1
        # res = nums[0]

        # while l <= r:
        #     if nums[l] < nums[r]:
        #         res = min(res, nums[l])
        #         break
        #     m = (l + r) // 2
        #     res = min(res, nums[m])
        #     if nums[m] >= nums[l]:
        #         l = m + 1
        #     else:
        #         r = m - 1
        # return res

