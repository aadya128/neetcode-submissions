class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx=0
        c=0
        for i in nums:
            if i==1:
                maxx+=1
            elif i==0:
                if c<maxx:
                    c=maxx
                maxx=0
        if c<maxx:
            c=maxx
        return c