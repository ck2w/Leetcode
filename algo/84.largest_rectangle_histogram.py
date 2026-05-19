# brute force, O(N^2)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            min_height = inf
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                max_area = max(max_area, min_height * (j - i + 1))
        return max_area


# stack, O(N)
# 对每根柱子，最大矩形的高度 = 该柱子高度，宽度 = 向左右两侧能延伸多远（直到遇到比它矮的柱子为止）。

# 换句话说，对每个 i，找：
# left[i]：左边第一个严格小于 heights[i] 的位置
# right[i]：右边第一个严格小于 heights[i] 的位置

# 则以 i 为高度的矩形面积 = heights[i] * (right[i] - left[i] - 1)
# 单调栈可以在一次遍历中同时完成这两件事。
# 栈里存的不是随机元素，而是一个"候选左边界"序列，且保证从栈底到栈顶高度严格递增。

# 某时刻栈 = [1, 2, 3]，对应高度 [1, 5, 6]
# 含义：当前这些柱子"还没找到右边界"，它们按高度递增排列
# 栈顶 3 是最高的，最容易被后面的矮柱子"终结"
# 弹出时刻 = 同时确定了左右边界

def largestRectangleArea(self, heights: list[int]) -> int:
    stack = []   # 单调递增栈，存下标
    max_area = 0
    n = len(heights)

    for i in range(n + 1):
        # 哨兵：循环结束时用 h=0 强制清空栈
        current_h = heights[i] if i < n else 0

        while stack and current_h < heights[stack[-1]]:
        	# stack顶元素，找到了右边界
            height = heights[stack.pop()]
            # 左边界：新栈顶；右边界：当前 i
            if stack: 
            	width = i - stack[-1] - 1
            else:
            	width = i            
            max_area = max(max_area, height * width)

        stack.append(i)

    return max_area