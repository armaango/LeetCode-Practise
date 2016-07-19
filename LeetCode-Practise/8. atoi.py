class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign = "+"
        inp = str.strip()
        if inp == "":
            return 0

        if inp[0] == "+" or inp[0] == "-":
            sign = inp[0]
            inp = inp[1:]
        if inp == "":
            return 0

        for i in range(len(inp)):
            if inp[i].isdigit():
                continue
            else:
                inp = inp[:i]
                break
        try:
            result = int(inp)
            if result > 2147483647 and sign == "+":
                result = 2147483647
            if sign == "-":
                return -result if result <= 2147483648 else -2147483648
            return result
        except:
            return 0