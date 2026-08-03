class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)

        if x.startswith("-"):
            x = x.replace("-", "")
            x = x[::-1]
            res = int("-" + x)
        else:
            x = x[::-1]
            res = int(x)

        if res >= 2**31 or res < -2**31:
            return 0

        return res