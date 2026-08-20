class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for a in range(len(nums)):
            nums[a]=nums[a]**2
        
        for a in range(len(nums)-1):
            minindex=a
            for b in range(a+1,len(nums)):
                if nums[b]<nums[minindex]:
                    minindex=b

            nums[a], nums[minindex] = nums[minindex], nums[a]
        return nums