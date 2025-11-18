from turtle import *
import math

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



def snowflake_koch(order, size) -> None:
    '''
    The function draws the Koch snowflake - three copies of the Koch curve,
    built (with the tips facing out) on the sides of a regular triangle.

    Args:
        order (int):  The depth of the recursion  for Koch curves.
        if order=0 - straight line
        size (float): Length of the current curve segment

    Returns:
        None: Функция выполняет отрисовку, не возвращает значений
    '''

    for side in range(3):
        koch(order, size)
        right(120)

def draw_tree(depth: int, size: float, angle: float) -> None:
    '''
    The function draws a colored fractal tree recursively.

    Args:
        depth (int): Depth of recursion (defines the number of branching levels)
        size (float):  Length of the current branch
        angle (float): The angle between the left and right branches

    Returns:
        None: The function only draws branches.
    '''

    if depth == 0:
        return

    colormode(255)
    green_component = 255 - int(depth * (250 / 6)) % 255
    color(0, green_component, 0)

    forward(size)

    right(angle)
    draw_tree(depth - 1, size / 2, angle)

    left(angle * 2)
    draw_tree(depth - 1, size / 2, angle)

    right(angle)
    backward(size)


def square_fractal(size, depth):
    """
    Recursively draws a fractal square.

    Args:
    size (float): side size of the square
    depth (int): recursion depth

    Returns:
        None: The function only draws squares.
    """

    if depth == 0:
        return

    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.forward(size * 0.1)
    turtle.right(10)
    square_fractal(size * 0.9, depth - 1)


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

def draw_branch(length: float):
    """
    Recursively draws a branch:
    1. Draw a line forward.
    2. Make two turns to the right and left.
    3. Reduce the length of the branch.
    4. Stop when the branch is too short.
    Args:
        length (int): First line length.

    Returns:
        None: The function only draws a branches.
    """

    if length < 5:
        return

    turtle.forward(length)

    turtle.right(30)
    draw_branch(length * 0.7)

    turtle.left(60)
    draw_branch(length * 0.7)

    turtle.right(30)
    turtle.backward(length)

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
        k_fractal(order - 1, 2 * size/ 5)
        rt(135)
        k_fractal(order - 1, (2 * size/ 5) * (2 ** 0.5))
        lt(45)
        k_fractal(order - 1, size / 5)
        lt(45)
        k_fractal(order - 1, (2 * size/ 5) * (2 ** 0.5))
        rt(135)
        k_fractal(order - 1, 2 * size/ 5)
        lt(90)


def spiral_triangle(order: int, size: float) -> None:
    """
    Draws a recursive spiral triangle fractal.

    Args:
        order (int): Recursion depth.
        size (float): Length of the triangle side.
    """

    if order == 0:
        for _ in range(3):
            forward(size)
            left(120)
    else:
        for _ in range(3):
            forward(size)
            left(120)
            penup()
            forward(size / 2)
            right(60)
            pendown()
            spiral_triangle(order - 1, size / 2)
            penup()
            left(60)
            backward(size / 2)
            pendown()


def main():
    fractals = {
        '1': 'Кривая Коха',
        '2': 'Ледяной 1',
        '3': 'Ледяной 2',
        '4': 'Кривая Леви',
        '5': 'Двоичное дерево',
        '6': 'Снежинка Коха',
        '7': 'Квадрат',
        '8': 'Уникальный фрактал 1',
        '9': 'Уникальный фрактал 2'
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

        case '5':
            try:
              angle = int(input('Угол ветвления:'))
            except ValueError:
              print("неправильно введён угол")
            x_coord = 0
            y_coord = 0
            setposition(x_coord, y_coord)
            left(90)
            down()
            draw_tree(depth, length, angle)

        case '6':
            x_coord = -length // 2
            y_coord = length // 2
            setposition(x_coord, y_coord)
            down()
            snowflake_koch(depth, length)

        case '7':
            x_coord = 0
            y_coord = 0
            setposition(x_coord, y_coord)
            down()
            square_fractal(depth, length)

        case '8':
            x_coord = -length // 2
            y_coord = 0
            setposition(x_coord, y_coord)
            down()
            k_fractal(depth, length)

        case '9':
            bgcolor("black")
            color("orange")
            x_coord = -length / 2
            y_coord = -length / (2 * math.sqrt(3))
            setposition(x_coord, y_coord)
            down()
            spiral_triangle(depth, length)







    update()
    done()

if __name__ == "__main__":
    main()
