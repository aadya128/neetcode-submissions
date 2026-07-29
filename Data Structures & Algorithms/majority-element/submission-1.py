class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lst = sorted(nums)
        n=len(lst)
        return lst[n//2]