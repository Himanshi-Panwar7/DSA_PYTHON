class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t={}
        t_map=set()
        for i, j in zip(s,t):
            if i in s_to_t:
                if s_to_t[i] != j:
                    return False
            else:
                if j in t_map:
                    return False
                s_to_t[i] =j
                t_map.add(j)

        return True
        