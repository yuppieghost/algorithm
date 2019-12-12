from itertools import permutations, chain, zip_longest, product

arr = [3, 9, 0, 8]
operators = "+-*/"


class BF:
    def __init__(self, li):
        self.nums = self.get_nums(li)

    @staticmethod
    def get_nums(li):
        for i in range(len(li)):
            li[i] = str(li[i])

        for i in permutations(li):
            yield i

    @staticmethod
    def get_ops():
        for i in product(operators, repeat=3):
            yield i

    def compute(self):
        for n in self.nums:
            ops = self.get_ops()
            for op in ops:
                s = zip_longest(n, op, fillvalue='')
                res_s = chain.from_iterable(s)
                calculate_str = ''
                for i in res_s:
                    calculate_str += i
                try:
                    if eval(calculate_str) == 24:
                        print(calculate_str)
                except ZeroDivisionError:
                    pass


bf = BF(arr)
bf.compute()
