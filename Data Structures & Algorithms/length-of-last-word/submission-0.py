class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst=[]
        s=s.strip()
        lst = s.split()
        return len(lst[-1])