class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        non_zeros=[num for num in nums if num!=0]
        zeros =n-len(non_zeros)
        result=non_zeros+[0]*zeros
        for i in range(n):
            nums[i]=result[i]
        return nums