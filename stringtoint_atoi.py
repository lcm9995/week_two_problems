def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        n = len(s)
        i = 0
        res = 0
        while (i < n and s[i]==" "):
            i+=1
        if i == n:
            return 0
        if s[i]=="-":
            sign = -1
            i+=1
        elif s[i]=="+":
            sign = 1
            i+=1
        else:
            sign = 1
        
        digits = set("0123456789")
        limit = (2**31-1)
        while (i < len(s) and s[i] in digits):
            new_dig = int(s[i])
            if res > limit//10 or (res == limit//10 and new_dig > 7):
                if sign == -1:
                    if res > (limit+1)//10 or (res == (limit+1)//10 and new_dig > 7):
                        return -1 * (limit+1)
                else:
                    return limit 
            res *= 10
            res += new_dig
            i+=1
        if sign == -1:
            if res >= limit + 1:
                return (limit+1)-1
            else:
                return res* -1
        else:
            if res >= limit:
                return limit
            else:
                return res
        return res