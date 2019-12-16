def insert(arr):
    for i in range(1, len(arr)):
        k = arr[i]
        j = i - 1
        while k >= 0 and arr[j] > k:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = k
count = 0

class Solution:
    def diffWaysToCompute(self, input: str):
        global count
        # 如果只有数字，直接返回
        if input.isdigit():
            return [int(input)]

        res = []
        for i, char in enumerate(input):
            count+=1
            if char in ['+', '-', '*']:
                # 1.分解：遇到运算符，计算左右两侧的结果集
                # 2.解决：diffWaysToCompute 递归函数求出子问题的解
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                # 3.合并：根据运算符合并子问题的解
                for l in left:
                    for r in right:
                        res.append(eval(f"{str(l) + char + str(r)}"))


        return res


if __name__ == '__main__':
    input = '2*3-4*5'
    s = Solution()
    print(s.diffWaysToCompute(input))
    print(count)
