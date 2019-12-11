d = {0: '零', 1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六', 7: '七', 8: '八', 9: '九'}
l = ['十', '百', '千', '万', '亿']

# n = input()


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
    # print(num_list)
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
    # print(s)


def get_list(num):
    num = num[::-1]
    s = [num[i:i + 4] for i in range(0, len(num), 4)]
    s = s[::-1]
    s = [i[::-1] for i in s]
    return s


# zh(n)


num=['零','一','二','三','四','五','六','七','八','九']
kin=['十','百','千','万','零']
import time
 
def sadd(x):
    x.reverse()
    if len(x) >= 2:
        x.insert(1,kin[0])
        if len(x) >= 4:
            x.insert(3,kin[1])
            if len(x) >= 6:
                x.insert(5,kin[2])
                if len(x) >= 8:
                    x.insert(7,kin[3])
                    if len(x) >= 10:
                        x.insert(9,kin[0])
                        if len(x) >= 12:
                            x.insert(11,kin[1])
 
    x=fw(x)
    x=d1(x)
    x=d2(x)
    x=dl(x)
    return x
    
    
def rankis():
    rank=[]
    for i in range(9999999):
        i=list(str(i))
        for j in i:
            i[(i.index(j))]=num[int(j)]
        i=sadd(i)
        # s = zh(str(i))
        rank.append(i)
    return rank
 
 
def d1(x):
    if '零' in x:
        a=x.index('零')
        if a==0:
            del x[0]
            d1(x)
        else:
            if x[a+2] in ['十','百','千','万','零']:
                if x[a+1] != '万':
                    del x[a+1]
                    d1(x)     
    return x
def d2(x):
    try:
        a=x.index('零')
        if x[a-1] in ['十','百','千','零']:
            del x[a-1]
            d2(x[a+1])
    except:pass
    return x
 
def fw(x):
    if len(x) >= 9:
        if x[8] == '零':
            del x[8]
    return x
def dl(x):
    try:
        if x[0]=='零':
            del x[0]
            del(x)
    except:pass
    x.reverse()
    x=''.join(x)
    return x

start=time.time()
rank=rankis()
end=time.time()-start
print('程序共用时：%0.2f'%end)