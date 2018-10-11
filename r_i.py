class Solution:
    def reverse(self, x):
        if x > 0:
            t = int(str(x)[::-1])
            if t > 2**31 - 1:
                return 0
            else:
                return t
        elif x < 0:
            t = -int((str(x)[1:])[::-1])
            if t < - 2**31:
                return 0
            else:
                return t
        else:
            return 0