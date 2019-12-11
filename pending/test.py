import pysnooper

@pysnooper.snoop()
class Solution:
    def trap(self, height) -> int:
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


l = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
s = Solution()
print(s.trap(l))
