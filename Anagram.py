# this use the hashmap - dict concept
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count={}
        for ch_s, ch_t in zip(s,t):
            count[ch_s]=count.get(ch_s,0) +1
            count[ch_t]=count.get(ch_t,0) -1
        for _ in count.values():
            if _!=0:
             return False
        return True


        
        