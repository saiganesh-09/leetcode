class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        expect_sum=n*(n+1)//2
        actual_sum=sum(nums)
        return expect_sum-actual_sum