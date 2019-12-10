from typing import List


# leetcode best solutions
class Solution1:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        left = 0
        right = n - 1
        maxleft = maxright = 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= maxleft:
                    maxleft = height[left]
                else:
                    res += maxleft - height[left]
                left += 1
            else:
                if height[right] >= maxright:
                    maxright = height[right]
                else:
                    res += maxright - height[right]
                right -= 1
        return res

    def mytrap(self, height: List[int]):
        res = 0
        left = 0
        n = len(height)
        right = n - 1
        max_left = max_right = 0
        while left <= right:
            if height[left] <= height[right]:
                if max_left <= height[left]:
                    max_left = height[left]
                else:
                    res += max_left - height[left]
                left += 1
            else:
                if max_right <= height[right]:
                    max_right = height[right]
                else:
                    res += max_right - height[right]
                right -= 1
        return res


# calculate by row
# easiest to understand,but time is O(n^2)
class Solution2:
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(1, len(height) - 1):
            min_wall = min(max(height[:i]), max(height[i + 1:]))
            if height[i] < min_wall:
                res += min_wall - height[i]

        return res


# dp solution, reduce time to O(n)
class Solution3:
    def trap(self, height):
        res = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        for i in range(1, n - 1):
            max_left[i] = max(max_left[i - 1], height[i - 1])

        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])

        for i in range(1, n - 1):
            min_wall = min(max_left[i], max_right[i])
            if height[i] < min_wall:
                res += min_wall - height[i]

        return res


# double point , reduce
class Solution4:
    def trap(self, height):
        res = 0
        n = len(height)
        max_left = 0
        max_right = 0
        left = 1
        right = n - 2

        for i in range(1, n - 1):
            if height[left - 1] < height[right + 1]:
                max_left = max(max_left, height[left - 1]);
                min_wall = max_left
                if height[left] < min_wall:
                    res += min_wall - height[left]
                left += 1
            else:
                max_right = max(max_right, height[right + 1])
                min_wall = max_right
                if min_wall > height[right]:
                    res += min_wall - height[right]
                right -= 1
        return res


if __name__ == '__main__':
    l = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    s = Solution1()
    res = s.mytrap(l)
    print(res)
