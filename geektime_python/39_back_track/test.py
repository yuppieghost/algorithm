# geektime 39 backtracking


# 0 - 1 bag 🎒

# 存储背包中物品总重量的最大值


def f(i, cw, items, n, w):
    """
    我们有一个背包，背包总的承载重量是 w。现在我们有 n 个物品，每个物品的重量不等，并且不可分割。
    我们现在期望选择几件物品，装载到背包中。在不超过背包所能装载重量的前提下，如何让背包中物品的总重量最大？
    i: 物品下标
    cw: 装进去物品重量总和
    items: 每个物品重量
    n: 物品个数
    w: 背包重量
    """
    global maxW
    global picks_with_max_weight

    if cw == w or i == n:
        if cw > maxW:
            picks_with_max_weight = picks.copy()
            maxW = cw
        return
    picks[i] = 0
    f(i + 1, cw, items, n, w)  # 不选该物品
    if cw + items[i] <= w:
        picks[i] = 1
        f(i + 1, cw + items[i], items, n, w)  # 选择该物品


maxW = 0
items = [7, 3, 9, 1, 6]
picks = [0] * len(items)
picks_with_max_weight = []
f(0, 0, items, 5, 8)
print('max weight', maxW)
print(picks_with_max_weight)
