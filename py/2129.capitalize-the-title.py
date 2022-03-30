
# @lc app=leetcode id=2129 lang=python3
#
# [2129] Capitalize the Title
#
# @lc code=start

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return ' '.join([x.lower().capitalize() if len(x)>2 else x.lower() for x in title.split(' ')])
                        

# @lc code=end
