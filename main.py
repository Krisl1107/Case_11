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


def ice(order, size):
    if order == 0:
        forward(size)
    else:
        ice(order-1, size)
        for _ in range(2):
          lt(120)
          ice(order-1, size/2)
          rt(180)
          ice(order-1, size/2)
        lt(120)
        ice(order-1, size)


def levi(order, size):
    if order == 0:
        forward(size)
    else:
        lt(45)
        levi(order-1, size / (2 ** 0.5))
        rt(90)
        levi(order - 1, size / 2 ** 0.5)
        lt(45)

    



def main():
    fractals = {
        '1': 'Кривая Коха',
        '2': 'Ледяной 1',
        '3': 'Ледяной 2',
        '4': 'Кривая Леви'
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

    match choice:
        case "1":
           x_coord = -length // 2
           y_coord = 0
           result = koch(depth,length)

        case "2":
           x_coord = - 2 * length
           y_coord = 0
           result = ice(depth, length)

        case "3":
           x_coord = - length // 2
           y_coord = 0
           result = ice(depth, length)

    up()
    setposition(x_coord, y_coord)
    down()
    turtle.speed(0)
    print(result)
    update()
    done()

if __name__ == "__main__":
    main()
