#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == "__main__":

    # 切片

    s = 'bicycle'
    print(s[::3])
    print(s[::-1])
    print(s[::-2])

    invoice = """
    0.....6................................40........52...55........
    1909 Pimoroni PiBrella                 $17.50    3    $52.50
    1489 6mm Tactile Switch x20            $4.95     2    $9.90
    1510 Panavise Jr. - PV-201             $28.00    1    $28.00
    1601 PiTFT Mini Kit 320x240            $34.95    1    $34.95
    """
    SKU = slice(0, 6)
    DESCRIPTION = slice(6, 40)
    UNIT_PRICE = slice(40, 52)
    QUANTITY = slice(52, 55)
    ITEM_TOTAL = slice(55, None)
    line_items = invoice.split('\n')[2:]
    for item in line_items:
        print(item[UNIT_PRICE], item[DESCRIPTION])

    l = list(range(10))
    print(l)
    l[2:5] = [20, 30]
    print(l)
    del l[5:7]
    print(l)
    l[3::2] = [11, 22]
    print(l)
    # l[2:5] = 100
    l[2:5] = [100]
    print(l)

    # 对切片赋值

    board = [['_'] * 3 for i in range(3)]
    print(board)
    board[1][2] = 'X'
    print(board)

    board = []
    for i in range(3):
        row = ['_'] * 3
        board.append(row)

    weird_board = [['_'] * 3] * 3
    print(weird_board)
    weird_board[1][2] = 'O'
    print(weird_board)

    row = ['_'] * 3
    weird_board = []
    for i in range(3):
        weird_board.append(row)

    # 增量赋值

    l = [1, 2, 3]
    print(id(l))
    l *= 2
    print(id(l))

    t = (1, 2, 3)
    print(id(t))
    t *= 2
    print(id(t))

    # +=

    t = (1, 2, [30, 40])
    # t[2] += [50, 60]
    # print(t)
    t[2].extend([70, 80])
    print(t)

    import dis
    dis.dis('s[a] += b')
    # TOS: Top Of Stack

    # 排序

    fruits = ['grape', 'raspberry', 'apple', 'banana']
    print(sorted(fruits))
    print(fruits)
    print(sorted(fruits, reverse=True))
    print(sorted(fruits, key=len))
    print(sorted(fruits, reverse=True, key=len))  # 并不是上面那个结果的反转，排序算法是稳定的。
    print(fruits)
    print(fruits.sort())
    print(fruits)
