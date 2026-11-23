class Solution:
    def isPalindrome(self, s: str) -> bool:
        i= 0
        s=''.join(x.lower() for x in s if x.isalnum())
        for j in range (len(s)-1,(len(s)//2)-1,-1):
            if s[j]!=s[i]:
                return False
            i+=1
        return True