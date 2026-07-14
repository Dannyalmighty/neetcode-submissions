
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = [1] * (len(nums))

        # prefix = 1
        # for i in range(len(nums)):
        #     res[i] = prefix
        #     prefix *= nums[i]
        # postfix = 1
        # for i in range(len(nums)-1, -1, -1):
        #     res[i] *= postfix
        #     postfix *= nums[i]
        # return res

        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        answer = [1] * n

        # prefix[i] = product of all elements before index i
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # suffix[i] = product of all elements after index i
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # combine
        for i in range(n):
            answer[i] = prefix[i] * suffix[i]

        return answer