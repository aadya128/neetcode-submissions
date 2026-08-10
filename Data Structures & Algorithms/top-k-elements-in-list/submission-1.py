class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst=[]
        dict1={}
        count=1
        max_key = None
        max_value = -1 

        for i in nums:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        while count<=k:
            max_key = None
            max_value = -1 
            for key, value in dict1.items():
                if value > max_value:
                    max_value = value 
                    maxx = key
            del dict1[maxx]
            lst.append(maxx)
            count+=1
        return lst