class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        list=[]
        for i in range(len(arr)):
            mid = arr[i+1:]
            if mid:
                m=max(mid)
                list.append(m)
            else:
                list.append(-1)
        return list