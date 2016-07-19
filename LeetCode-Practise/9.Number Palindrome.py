class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or x > 0x7fffffff:return False
        copy,result =x, 0
        while x:
            result = result * 10 + x%10
            x /= 10
        return copy == result
