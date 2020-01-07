#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List, Tuple


def bag(items_info: List[int], capacity: int) -> int:
    """
    固定容量的背包，计算能装进背包的物品组合的最大重量

    :param items_info: 每个物品的重量
    :param capacity: 背包容量
    :return: 最大装载重量
    eg :
    items_info = [2，2，4，6，3]; // 物品重量
    n = 5; // 物品个数
    capacity = 9; // 背包承受的最大重量
    状态转移示例图:
    https://i.loli.net/2019/12/16/yiMZP1sTdYAFbtO.png
    https://i.loli.net/2019/12/16/ipTJFZVQNrax1hb.png

    """
    print(items_info)
    n = len(items_info)
    dp = [True] + [False] * capacity
    if items_info[0] <= capacity:
        dp[items_info[0]] = True
    for i in range(1, n):
        for j in range(capacity - items_info[i], -1, -1):
            if dp[j]:
                dp[j + items_info[i]] = True
    res = [i for i, c in enumerate(dp) if c == True][-1]
    return res


# public static int knapsack2(int[] items, int n, int w) {
#   boolean[] states = new boolean[w+1]; // 默认值false
#   states[0] = true;  // 第一行的数据要特殊处理，可以利用哨兵优化
#   if (items[0] <= w) {
#     states[items[0]] = true;
#   }
#   for (int i = 1; i < n; ++i) { // 动态规划
#     for (int j = w-items[i]; j >= 0; --j) {//把第i个物品放入背包
#       if (states[j]==true) states[j+items[i]] = true;
#     }
#   }
#   for (int i = w; i >= 0; --i) { // 输出结果
#     if (states[i] == true) return i;
#   }
#   return 0;
# }


# dp = [True] + [False] * capacity
# for i in items_info:
#     dp = [dp[c] or (c >= i and dp[c - i]) for c in range(capacity + 1)]
# res = [i for i, c in enumerate(dp) if c == True][-1]
# return res
# # 扩展成二维数组的解法
# # 创建 memo, (capacity + 1) * n 个 -1
# memo = [[-1] * (capacity + 1) for _ in range(n)]
# # 什么都不选
# memo[0][0] = 1
# if items_info[0] <= capacity:
#     # 选择第一个
#     # items_info[0] 即第一个物品的重量
#     memo[0][items_info[0]] = 1
#
# # 第0个物品决策完后的状态记录完毕
#
# for i in range(1, n):
#     for cur_weight in range(capacity + 1):
#         # 上一行存在
#         if memo[i - 1][cur_weight] != -1:
#             memo[i][cur_weight] = memo[i - 1][cur_weight]  # 不选
#             # 注意选择的前提条件,当前背包重量加上该物品后的总重量必须小于等于背包容量
#             if cur_weight + items_info[i] <= capacity:  # 选
#                 memo[i][cur_weight + items_info[i]] = 1
#
# # 选择最后一次状态的最大值
# for w in range(capacity, -1, -1):
#     if memo[-1][w] != -1:
#         return w


def bag_with_max_value(items_info: List[Tuple[int, int]], capacity: int) -> int:
    """
    固定容量的背包，计算能装进背包的物品组合的最大价值

    :param items_info: 物品的重量和价值
    :param capacity: 背包容量
    :return: 最大装载价值
    """
    n = len(items_info)
    memo = [[-1] * (capacity + 1) for i in range(n)]
    memo[0][0] = 0
    # items_info[0][0]: weight
    # items_info[0][1]: value
    if items_info[0][0] <= capacity:
        # 下标不变, 值从Boolean变为value
        # 选择第0个物品, 记录值为第0个物品的价值
        memo[0][items_info[0][0]] = items_info[0][1]

    for i in range(1, n):
        for cur_weight in range(capacity + 1):
            if memo[i - 1][cur_weight] != -1:
                memo[i][cur_weight] = memo[i - 1][cur_weight]  # 不选
                if cur_weight + items_info[i][0] <= capacity:
                    # 选择并保留最大value ,比较当前位置**本来的值**跟新值
                    memo[i][cur_weight + items_info[i][0]] = max(
                        memo[i][cur_weight + items_info[i][0]],
                        memo[i - 1][cur_weight] + items_info[i][1],
                    )

    return max(memo[-1])


if __name__ == "__main__":
    # [weight, ...]
    items_info = [2, 2, 4, 6, 3]
    capacity = 9
    print(bag(items_info, capacity))

    # # [(weight, value), ...]
    # items_info = [(3, 5), (2, 2), (1, 4), (1, 2), (4, 10)]
    # # (3,5) (1,4) (4,10)
    # capacity = 8
    # print(bag_with_max_value(items_info, capacity))
