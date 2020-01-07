from typing import List


def solution(time_info: List):
    n = len(time_info)
    time_info.sort()
    if n <= 2:
        return time_info[n]
    if n == 3:
        return time_info[1] + time_info[2] + time_info[3]
    f2 = time_info[2]
    f1 = time_info[1] + time_info[2] + time_info[3]
    fn = 0
    for i in range(4, n):
        fn = time_info[1] + 2 * time_info[2] + time_info[i] + f2
        f2 = f1
        f1 = fn
    return fn


if __name__ == "__main__":
    time_info = [0, 1, 2, 5, 10]
    print(solution(time_info))
