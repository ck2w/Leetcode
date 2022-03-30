#
# @lc app=leetcode id=288 lang=python3
#
# [288] Unique Word Abbreviation

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.d = {}
        for word in dictionary:
            abb = self.abbrev(word)
            if abb in self.d:
                self.d[abb].add(word)
            else:
                self.d[abb] = set([word])                

    def isUnique(self, word: str) -> bool:
        abb = self.abbrev(word)
        if (abb not in self.d) or (abb in self.d and word in self.d[abb] and len(self.d[abb])==1):
            return True
        return False
        
        
    def abbrev(self, word):
        if len(word) == 2:
            return word
        else:
            return word[0] + str(len(word)-2) + word[-1]

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_2 = obj.isUnique(word)
# @lc code=end# @lc code=end

