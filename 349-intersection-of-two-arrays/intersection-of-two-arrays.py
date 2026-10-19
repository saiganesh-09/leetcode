class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))
        '''r=[]
        m=len(nums1)
        n=len(nums2)
        if m>n:
            for num in nums1:
                if (num in nums2) and (num not in r):
                    r.append(num)
        else:
            for num in nums2:
                if (num in nums1) and (num not in r):
                    r.append(num)
        return r'''
