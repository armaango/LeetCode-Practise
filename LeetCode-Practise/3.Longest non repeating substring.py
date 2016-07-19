class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = [False for _ in xrange(256)]
        cIndex , mlen = 0,0
        for i,char in enumerate(s):
            if not seen[ord(char)]:
                seen[ord(char)] = True
                mlen = max(mlen,i-cIndex+1)
            else:
                while char != s[cIndex]:
                    seen[ord(s[cIndex])]=False
                    cIndex +=1
                cIndex +=1
        return mlen