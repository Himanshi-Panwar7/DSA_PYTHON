class Solution:
    def reverseWords(self, s: str) -> str:
        s= s.split()
        i=0
        for j in range(len(s)-1,(len(s)//2)-1,-1):

            s[i], s[j]=s[j],s[i]
            i +=1
        return " ".join(s)
