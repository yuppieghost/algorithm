d = {0: '零', 1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六', 7: '七', 8: '八', 9: '九'}
l = ['十', '百', '千', '万', '亿']

n = input()


def part(n):
    num = int(n)
    s = ''
    a = len(n) - 2
    if num % 10000 == 0:
        last = -4
    elif num % 1000 == 0:
        last = -3
    elif num % 100 == 0:
        last = -2
    elif num % 10 == 0:
        last = -1
    else:
        last = None
    for i in n[:last]:
        if i == '0':
            if s.endswith('零'):
                a -= 1
                continue
            s += "零"
            a -= 1
            continue
        _num = d[int(i)]
        if a >= 0:
            _s = l[a]
            a -= 1
        # 末尾不读
        else:
            _s = ''
        s += _num + _s
    return s


def zh(n):
    num_list = get_list(n)
    print(num_list)
    s = ''
    list_length = len(num_list)
    b = list_length
    for i in range(list_length):
        if i == '0000':
            b -= 1
            continue
        # todo 100000000000
        # ['1000', '0000', '0000']
        # 一千亿万
        if b > 1:
            s += part(num_list[i]) + l[b - 4]
            b -= 1
        else:
            s += part(num_list[i])
    print(s)


def get_list(num):
    num = num[::-1]
    s = [num[i:i + 4] for i in range(0, len(num), 4)]
    s = s[::-1]
    s = [i[::-1] for i in s]
    return s


zh(n)
