#
# @lc app=leetcode id=170 lang=python3
#
# [170] Two Sum III - Data structure design
#
# @lc code=start
class TwoSum:

    def __init__(self):
        self.vals = []

    def add(self, number: int) -> None:
        self.vals.append(number)            

    def find(self, value: int) -> bool:
        s = set()
        for val in self.vals:
            if value - val in s:
                return True
            else:
                if val not in s:
                    s.add(val)            
            
        return False
        
# @lc code=end

