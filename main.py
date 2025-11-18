from turtle import *


def koch(order, size):
    if order == 0:
        forward(size)
    else:
        koch(order-1, size/3)
        lt(60)
        koch(order-1, size/3)
        rt(120)
        koch(order-1, size/3)
        lt(60)
        koch(order-1, size/3)


def ice_1(dpth, size) -> None:
    """
    Draws a recursive ice-like fractal.

    Args:
        dpth (int): The recursion depth.
        size (float): The length of the current segment.
    """

    if dpth == 0:
        forward(size)
    else:
        ice_1(dpth - 1, size / 2)
        left(90)
        ice_1(dpth - 1, size / 4)
        left(180)
        ice_1(dpth - 1, size / 4)
        left(90)
        ice_1(dpth - 1, size / 2)


def ice_2(order, size):
    if order == 0:
        forward(size)
    else:
        ice_2(order-1, size)
        for _ in range(2):
          lt(120)
          ice_2(order-1, size/2)
          rt(180)
          ice_2(order-1, size/2)
        lt(120)
        ice_2(order-1, size)


def levi(order, size):
    if order == 0:
        forward(size)
    else:
        lt(45)
        levi(order-1, size / (2 ** 0.5))
        rt(90)
        levi(order - 1, size / 2 ** 0.5)
        lt(45)

def k_fractal(order, size):
    if order == 0:
        forward(size)
    else:

        lt(90)
        kris_2(order - 1, 2 * size/ 5)
        rt(135)
        kris_2(order - 1, (2 * size/ 5) * (2 ** 0.5))
        lt(45)
        kris_2(order - 1, size / 5)
        lt(45)
        kris_2(order - 1, (2 * size/ 5) * (2 ** 0.5))
        rt(135)
        kris_2(order - 1, 2 * size/ 5)
        lt(90)



def main():
    fractals = {
        '1': 'Кривая Коха',
        '2': 'Ледяной 1',
        '3': 'Ледяной 2',
        '4': 'Кривая Леви',
        '5': 'Двоичное дерево'
    }
    print("Выберите фрактал:")
    for key, name in fractals.items():
        print(f"{key}. {name}")

    choice = input("Введите номер (1-4): ").strip()

    if choice in fractals:
        pass
    else:
        print("Некорректный ввод.")
        exit()

    depth = int(input('Глубина рекурсии:'))
    length = int(input('Длина стороны:'))
    x_coord = 0
    y_coord = 0
    up()

    match choice:
        case '1':
            x_coord = -length // 2
            y_coord = 0
            setposition(x_coord, y_coord)
            down()
            koch(depth, length)

        case '2':
            x_coord = -2 * length
            y_coord = 0
            setposition(x_coord, y_coord)
            down()
            ice_1(depth, length)

        case '3':
            x_coord = -2 * length
            y_coord = 0
            setposition(x_coord, y_coord)
            down()
            ice_2(depth, length)

        case '4':
            x_coord = -length // 2
            y_coord = 0
            setposition(x_coord, y_coord)
            down()
            levi(depth, length)

    update()
    done()

if __name__ == "__main__":
    main()
