# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:
    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    star_param =[]
    for i in line.split():
        star_param.append(i)
    star.R = int(star_param[1])
    star.color = star_param[2]
    star.m = int(normal_numbers(star_param[3]))
    star.x = int(normal_numbers(star_param[4]))
    star.y = int(normal_numbers(star_param[5]))
    star.Vx = int(normal_numbers(star_param[6]))
    star.Vy = int(normal_numbers(star_param[7]))


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """

    star_param = []
    for i in line.split():
        star_param.append(i)
    planet.R = int(star_param[1])
    planet.color = star_param[2]
    planet.m = int(normal_numbers(star_param[3]))
    planet.x = int(normal_numbers(star_param[4]))
    planet.y = int(normal_numbers(star_param[5]))
    planet.Vx = int(normal_numbers(star_param[6]))
    planet.Vy = int(normal_numbers(star_param[7]))


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            pass
            #print(out_file, "%s %d %s %f" % ('1', 2, '3', 4.5), file=sys.stdout)
            # FIXME: should store real values


# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

def normal_numbers(line):
    """
    Превращает числа из тектовых файлов в удобочитаемый формат
    На вход str, на выход str
    """
    if "E" in line:
        line_1 = line.split("E")
        value = int(float(line_1[0]) * 10 ** int(line_1[1]))
        return value
    else:
        return line


if __name__ == "__main__":
    print("This module is not for direct call!")
