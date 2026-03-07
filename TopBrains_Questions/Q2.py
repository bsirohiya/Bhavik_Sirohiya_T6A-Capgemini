class Solution:
    def strong_passwords(self, passwords):
        strong = []
        ##Write your code here
        for i in passwords:
            if len(i) >= 8:
                upper = any(j.isupper() for j in i)
                digit = any(j.isdigit() for j in i)
                special = any(j in "@#$" for j in i)

            if upper and digit and special:
                strong.append(i)
       
        return strong