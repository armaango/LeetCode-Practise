class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(s , l , r):
            L ,R = l,r
            while L >= 0 and R < len(s) and s[L] == s[R]:
                L -= 1
                R += 1
            return R-L-1


        st , end = 0,0
        for i in range(len(s)):
            len1 = expand(s,i,i)
            len2 = expand(s,i,i+1)
            length = max(len1,len2)
            if(length > end - st):
                st = i - (length-1)/2
                end = i+length/2
        return s[st:end+1]