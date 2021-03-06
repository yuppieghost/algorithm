#!/usr/bin/python
# -*- coding: UTF-8 -*-

is_match = False


def rmatch(r_idx: int, m_idx: int, ):
    global is_match

    if is_match:
        return

    if r_idx >= len(regex):  # 正则串全部匹配好了
        is_match = True
        return

    if m_idx >= len(main) and r_idx < len(regex):  # 正则串没匹配完，但是主串已经没得匹配了
        is_match = False
        return

    if regex[r_idx] == '*':  # * 匹配1个或多个任意字符，递归搜索每一种情况
        for i in range(m_idx, len(main)):
            rmatch(r_idx + 1, i + 1)
    elif regex[r_idx] == '?':  # ? 匹配0个或1个任意字符，两种情况
        rmatch(r_idx + 1, m_idx + 1)
        rmatch(r_idx + 1, m_idx, )
    else:  # 非特殊字符需要精确匹配
        if regex[r_idx] == main[m_idx]:
            rmatch(r_idx + 1, m_idx + 1)


if __name__ == '__main__':
    regex = 'ab*eee?d'
    main = 'abcdsadfkjlekjoiwjiojieeecd'
    rmatch(0, 0)
    print(is_match)
