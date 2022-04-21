class Solution:
    #inputlst=['I', 'V', 'X', 'L', 'C', 'D' , 'M']
   # inputdict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    def romanToInt(self, s: str) :
        inputdict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum=0
        for i in range (len (s)):
          for j in range (0,len (s),2) :
           if (i + 1) < len (s):
            if s[i] < s[i + 1]:
                sum = inputdict[s[i+1]]-inputdict[s[i]]
            else:
                sum+=inputdict[s[i]]


        return sum


a=Solution()
print(a.romanToInt('III'))
print(a.romanToInt('IV'))