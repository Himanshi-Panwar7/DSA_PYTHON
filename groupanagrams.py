from collections import defaultdict # initializes a hashmap which initializes the mising key with a list
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list) 
        for word in strs:
            signature=''.join(sorted(word)) # each uniue signature serve as the key and its anagrams are the values that too list
            groups[signature].append(word)
        return list(groups.values())