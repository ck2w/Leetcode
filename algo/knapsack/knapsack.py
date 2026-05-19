from typing import NamedTuple


class Item(NamedTuple):
    name: str
    wt: int
    val: int


def knapsack(items: list[Item], W: int) -> tuple[int, list[str]]:
    n = len(items)
    # dp[0][w] = 0,  对所有 w ∈ [0, W]   // 没有物品可选，价值为 0
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        wt, val = items[i - 1].wt, items[i - 1].val
        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]
            if w >= wt:
                # // 不选物品 i: dp[i][w] = dp[i-1][w]
                # // 选物品 i（前提：w >= wt[i]）: dp[i][w] = dp[i-1][w - wt[i]] + val[i]
                dp[i][w] = max(dp[i][w], dp[i-1][w-wt] + val)

    # 回溯
    selected, w = [], W
    for i in range(n, 0, -1):
        # # 价值变化，说明第 i 个物品被选了
        if dp[i][w] != dp[i - 1][w]:
            selected.append(items[i - 1].name)
            w -= items[i - 1].wt

    return dp[n][W], selected[::-1]


if __name__ == "__main__":
    items = [
        Item("A", wt=2, val=3),
        Item("B", wt=3, val=4),
        Item("C", wt=4, val=5),
        Item("D", wt=5, val=6),
    ]
    best, chosen = knapsack(items, W=6)
    print(f"最大价值: {best}, 选中: {chosen}")