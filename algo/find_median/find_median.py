import random

def quickselect_median(arr):
    a = arr[:]
    n = len(a)
    target = n // 2
    return _select(a, 0, n - 1, target)

def _select(a, lo, hi, target):
    if lo == hi:
        return a[lo]

    # 随机选 pivot，减少最坏情况概率
    # 固定选某个位置（比如总选第一个）会被特定输入稳定触发。
    pivot_idx = random.randint(lo, hi)
    a[pivot_idx], a[hi] = a[hi], a[pivot_idx] # pivot换到最右
    pivot = a[hi]

    slow = lo  # 左区下一个空位（所有 < slow 的位置都已填好）

    for fast in range(lo, hi):   # fast 逐个审查每个元素
        if a[fast] <= pivot:
            a[slow], a[fast] = a[fast], a[slow]
            slow += 1            # 左区扩张一位

    # pivot 归位：放到左区紧接着的位置
    a[slow], a[hi] = a[hi], a[slow]
    k = slow  # pivot 的最终索引

    if k == target:
        return a[k]
    elif k < target:
        return _select(a, k + 1, hi, target)
    else:
        return _select(a, lo, k - 1, target)


# 测试
arr = [7, 2, 10, 4, 3, 8, 1, 6, 5]
print(quickselect_median(arr))   # → 5
print(sorted(arr)[len(arr) // 2])  # → 5，验证