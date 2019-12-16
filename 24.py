from itertools import permutations, chain, zip_longest, product
import math
import itertools

arr = [2, 3, 4, 5]
operators = "+-*/"


class BF:
    # this algorithm doesn't consider bracket
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


# bf = BF(arr)
# bf.compute()

from operator import truediv, mul, add, sub


class Leetcode:

    def judgePoint24(self, A):
        if not A:
            return False
        if len(A) == 1:
            return abs(A[0] - 24) < 1e-6

        for i in range(len(A)):
            for j in range(len(A)):
                if i != j:
                    B = [A[k] for k in range(len(A)) if i != k != j]
                    for op in (truediv, mul, add, sub):
                        if (op is add or op is mul) and j > i: continue
                        if op is not truediv or A[j]:
                            B.append(op(A[i], A[j]))
                            if self.judgePoint24(B):
                                return True
                            B.pop()
        return False


# lc = Leetcode()
# lc.judgePoint24(arr)

class Solution1(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import itertools
        TARGET = 24
        EQN_LEN = 3 # (Operand, Operator, Operand) triplet.
        # Generate all possible number sequences. Convert to float string so that
        # division does not result in truncation.
        number_orders = set(tuple(itertools.permutations([str(num) + '.0' for num in nums])))
        # print(number_orders)
        # Generate all possible operator sequences.
        operator_orders = set(tuple(itertools.permutations('***///+++---', len(nums) - 1)))
        print(operator_orders)

        # Evaluate an equation with different permutation of brackets
        # and return True if any of them evaluate to the target.
        def possible(equation):
            found = [False]
            def evaluate(eqn):
                # Reduces an equation by length 2 each time:
                # An equation of ['1.0', '*', '2.0', '+', '3.0', '/', '4.0'] becomes:
                # - [2.0', '+', '3.0', '/', '4.0'] (1.0 * 2.0 reduced to 2.0)
                # - [1.0', '*', '5.0', '/', '4.0'] (2.0 + 3.0 reduced to 5.0)
                # - [1.0', '*', '2.0', '+', '0.75'] (3.0 / 4.0 reduced to 0.75)
                if found[0]:
                    return
                if len(eqn) == EQN_LEN:
                    val = eval(''.join(eqn))
                    # Compare against a delta because of floating point inaccuracies.
                    if abs(val - TARGET) < 0.0001:
                        found[0] = True
                    return
                # Recursively try different permutations
                # of operands + operators triplets, simulating brackets.
                for i in range(0, len(eqn) - 1, 2):
                    try:
                        # Wrap in try/except as there can be a division by 0 error.
                        evaluate(eqn[:i] + [str(eval(''.join(eqn[i:i + EQN_LEN])))] + eqn[i + EQN_LEN:])
                    except:
                        pass
            evaluate(equation)
            return found[0]

        for number_order in number_orders:
            for operator_order in operator_orders:
                equation = [None] * (len(number_order) + len(operator_order))
                for i, number in enumerate(number_order):
                    equation[0 + i * 2] = number
                for i, operator in enumerate(operator_order):
                    equation[1 + i * 2] = operator
                # Generate an equation to test whether it is possible to get 24 using it.
                # Example equation: ['1.0', '*', '2.0', '+', '3.0', '/', '4.0']
                if possible(equation):
                    return True
        return False

s = Solution1()
s.judgePoint24(arr)