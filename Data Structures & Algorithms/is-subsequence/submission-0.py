class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''for i in s:
            if i not in t:
                break
            return False
            for j in range(len(t)):
                next= t[index(i+1):]
            if i not in next:
                return False
            else:
                return True'''

        a=b=0
        while a<len(s) and b<len(t):
            if s[a]==t[b]:
                a+=1
            b+=1
        return a==len(s)
