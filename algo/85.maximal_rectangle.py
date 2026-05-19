
# 逐行构建高度数组，然后对每行跑一遍 Largest Rectangle in Histogram

# 第一步：理解高度数组
# 对矩阵每一列，计算「连续向上的 1 的个数」作为该列的高度

# 第二步：每行的高度数组 = 柱状图问题
# 对 row2: [3, 1, 3, 2, 2]，用单调栈求最大矩形面积 = 6（


def maximalRectangle(self, matrix: List[List[str]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    
    cols = len(matrix[0])
    heights = [0] * (cols + 1)  # 多一个哨兵0，方便清空栈
    max_area = 0
    
    for row in matrix:
        # 更新高度数组
        for j in range(cols):
            heights[j] = heights[j] + 1 if row[j] == '1' else 0
        
        # 单调栈求当前行柱状图的最大矩形
        stack = [-1]  # 哨兵，代表左边界
        for i in range(cols + 1):
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
            	# stack顶元素，找到了右边界
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
    
    return max_area