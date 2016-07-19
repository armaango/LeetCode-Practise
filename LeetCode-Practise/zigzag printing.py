class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        else:
            rStr = ""
            i, k = 0 , 0
            for j in range(0,numRows):
                while i < len(s):
                    rStr += s[i]
                    if(j%2==0):
                        i += (2*numRows-2)
                    else:
                        i += (2*numRows-4)
                k +=1
                i = k
            return rStr