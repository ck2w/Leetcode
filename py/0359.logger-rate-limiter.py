#
# @lc app=leetcode id=359 lang=python3
#
# [359] Logger Rate Limiter

# @lc code=start
class Logger:
    def __init__(self):
        self.d = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.d:
            if timestamp >= self.d[message]:
                self.d[message] = timestamp + 10
                return True
            else:
                return False
        else:
            self.d[message] = timestamp + 10
            return True
# @lc code=end

