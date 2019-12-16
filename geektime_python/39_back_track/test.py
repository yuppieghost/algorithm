# geektime 39 backtracking


# 0 - 1 bag 🎒

# 存储背包中物品总重量的最大值
maxW = 0


def f(i, cw, items, n, w):
    """
    i: 物品下标
    cw: 装进去物品重量总和
    items: 每个物品重量
    n: 物品个数
    w: 背包重量
    """
    global maxW
    if cw == w or i == n:
        if cw > maxW:
            maxW = cw
        return

    f(i + 1, cw, items, n, w)  # 不选该物品
    if cw + items[i] <= w:
        f(i + 1, cw + items[i], items, n, w)  # 选择该物品


items = [3, 2, 1, 1, 4]
f(0, 0, items, 5, 8)
print(maxW)
