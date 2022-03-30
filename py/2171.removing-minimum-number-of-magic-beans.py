
# @lc app=leetcode id=2171 lang=python3
#
# [2171] Removing Minimum Number of Magic Beans
#
# @lc code=start
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        n = len(beans)
        if n <= 1:
            return 0
        from itertools import accumulate
        sort_beans = sorted(beans)
        cum_beans = list(accumulate(sort_beans))
        # print(sort_beans)
        # print(cum_beans)
        cum_end = cum_beans[-1]
        min_cut = cum_end
        for i, val in enumerate(cum_beans):
            if i > 0:                
                cut1 = cum_beans[i-1]
                cut2 = cum_end - val - (n-i-1) * sort_beans[i]                
            elif i == 0:
                cut1 = 0
                cut2 = cum_end - val - (n-i-1) * sort_beans[i]
            # print(cut1, cut2)
            min_cut = min(min_cut, cut1 + cut2)
        return min_cut
# @lc code=end
