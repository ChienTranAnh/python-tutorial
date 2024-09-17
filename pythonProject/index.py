print('Hello\nworld!')
"""
comment multi-line
"""
if 5 < 2:
    print('Five is less than two!')
else:
    print('Five is greater than two!')

a = 50
A = 100.0
print(type(a), type(A))

def in_ra_man_hinh(n):
    i = 1
    while i <= n:
        print(i, end=' ')
        i += 1

in_ra_man_hinh(100)


def tinh_tong_so_chan(n):
    i = 1
    tong = 0
    while i <= n:
        if i % 2 == 0:
            # print(i, end='-')
            tong = tong + i
        i += 1

    return tong

print(tinh_tong_so_chan(100))
