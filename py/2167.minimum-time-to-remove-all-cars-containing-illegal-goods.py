
# @lc app=leetcode id=2167 lang=python3
#
# [2167] Minimum Time to Remove All Cars Containing Illegal Goods
#
# @lc code=start
class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.data = [0] * size
        self.flip_data = [1] * size
        self.mode = True
        self.count_num = 0

    def fix(self, idx: int) -> None:        
        if self.mode:
            if self.data[idx] == 0:
                self.count_num += 1
            self.data[idx] = 1
            self.flip_data[idx] = 0            
        else:
            if self.flip_data[idx] == 0:
                self.count_num += 1            
            self.data[idx] = 0
            self.flip_data[idx] = 1

    def unfix(self, idx: int) -> None:
        if self.mode:
            if self.data[idx] == 1:
                self.count_num -= 1
            self.data[idx] = 0
            self.flip_data[idx] = 1
        else:
            if self.flip_data[idx] == 1:
                self.count_num -= 1
            self.data[idx] = 1
            self.flip_data[idx] = 0

    def flip(self) -> None:
        self.mode = not self.mode
        self.count_num = self.size - self.count_num

    def all(self) -> bool:        
        return self.count_num == self.size

    def one(self) -> bool:
        return self.count_num > 0      

    def count(self) -> int:
        return self.count_num

    def toString(self) -> str:
        if self.mode:
            return ''.join([str(x) for x in self.data])
        else:
            return ''.join([str(x) for x in self.flip_data])
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()   

# @lc code=end
