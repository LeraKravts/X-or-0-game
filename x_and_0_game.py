
def main():
    field_size = give_me_field_size()
    print(draw_field(field_size))
    check_vertically(draw_field(field_size), field_size)
    possible_steps = get_possible_steps(field_size)
    previous_steps = []
    player_step(possible_steps, previous_steps, draw_field(field_size), field_size)


def draw_field(size: int) -> str:
    """создаем поле для игры"""

    line1 = '  '
    for i in range(1, size+1):
        line1 += str(i) + '   '
        i += 1

    my_letters = ['a', 'b', 'c', 'd', 'e']
    field = '''{}
'''.format(line1)
    for i in range(size):
        field += '{}   '.format(my_letters[i]) + '|   ' * (size-1)+'\n'
        if i < size - 1:
            field += '  --' + "---"*size + "\n"

    return field


def give_me_field_size():
    """просим у игрока размеры поля"""
    try:
        number = int(input('введи число от 3 до 5 '))

        if 3 <= number <= 5:
            return number
        else:
            return give_me_field_size()
    except TypeError and ValueError:
        return give_me_field_size()


def get_possible_steps(size: int):
    """собираем диапазон возможных шагов"""
    my_letters = ['a', 'b', 'c', 'd', 'e']
    possible_steps = []
    for i in range(1, size+1):
        for elem in my_letters[0:size]:
            a = '{}{}'.format(i, elem)
            possible_steps.append(a)

    return possible_steps


def player_step(possible_steps: list, previous_steps: list, field: str, field_size: int):
    """шаг игрока и проверка шага"""

    step = (input('Выбери ячейку - сначала число, потом буква, например, 1a. '
                  'Заполненные ячейки выбирать нельзя!\n''Твой ход -> ')).lower()

    if step in possible_steps and step not in previous_steps:
        line_array = field.split('\n')[1:][::2]

        for i in line_array:
            if i[0] == step[1]:

                step_place = 3 + 4*(int(step[0])-1)-1
                if len(previous_steps) % 2 == 0:
                    step_in_line = i[0:step_place]+'X'+i[step_place+1:]
                else:
                    step_in_line = i[0:step_place] + '0' + i[step_place + 1:]
                line_array[line_array.index(i)] = step_in_line

                previous_steps.append(step)

        line1 = '  '
        for i in range(1, field_size + 1):
            line1 += str(i) + '   '
            i += 1

        new_field = '''{}\n'''.format(line1)
        for i in line_array:
            new_field += i + '\n'
            if line_array.index(i) < len(line_array)-1:
                new_field += '  --' + "---" * field_size + "\n"

        print(new_field)

        if len(possible_steps) == len(previous_steps) and \
                check_horizontally(new_field, field_size) is False and \
                check_vertically(new_field, field_size) is False and \
                check_diagonally(new_field, field_size) is False:
            return print('Сегодня ничья')

        elif check_horizontally(new_field, field_size) is False \
                and check_vertically(new_field, field_size) is False and\
                check_diagonally(new_field, field_size) is False:
            player_step(possible_steps, previous_steps, new_field, field_size)

        elif (check_horizontally(new_field, field_size) == 'X' or
              check_horizontally(new_field, field_size) == '0'):
            print(check_horizontally(new_field, field_size) + " - выиграл")

        elif (check_vertically(new_field, field_size) == 'X' or
              check_vertically(new_field, field_size) == '0'):
            print(check_vertically(new_field, field_size) + " - выиграл")

        elif (check_diagonally(new_field, field_size) == 'X' or
              check_diagonally(new_field, field_size) == '0'):
            print(check_diagonally(new_field, field_size) + " - выиграл")

    else:
        player_step(possible_steps, previous_steps, field, field_size)


def check_horizontally(field: str, field_size: int):
    """проверяем победителя по горизонтали"""

    line_array = field.split('\n')[1:][::2]
    for i in line_array:
        if str(i).count('X') == field_size or str(i).count('0') == field_size:
            if str(i).count('X') == field_size:
                return "X"
            else:
                return "0"
    return False


def check_vertically(field: str, field_size: int):
    """проверяем победителя по вертикали"""
    line_array = field.split('\n')[1:][::2]
    possible_places = []

    for i in range(1, field_size+1):
        step_place = 3 + 4*(int(i) - 1)-1
        possible_places.append(step_place)

    for i in possible_places:
        column = []
        for elem in line_array:
            column.append(elem[i])
            if len(column) == len(line_array):
                if column.count('X') == field_size or column.count('0') == field_size:
                    return column[0]
    return False


def check_diagonally(field: str, field_size: int):
    """проверяем победителя по диагонали"""

    line_array = field.split('\n')[1:][::2]
    possible_places = []

    for i in range(1, field_size+1):
        step_place = 3 + 4*(int(i) - 1)-1
        possible_places.append(step_place)
    places_arr = []
    for elem in line_array:
        arr = []
        for i in possible_places:
            arr.append(elem[i])
            if len(arr) == len(possible_places):
                places_arr.append(arr)
    left_to_right = []
    right_to_left = []
    for i in range(0, len(places_arr)):
        left_to_right.append(places_arr[i][i])
    if left_to_right.count("X") == len(places_arr) or left_to_right.count("0") == len(places_arr):
        return left_to_right[0]
    for i in range(1, len(places_arr)+1):
        right_to_left.append(places_arr[i-1][-i])
    if right_to_left.count("X") == len(places_arr) or right_to_left.count("0") == len(places_arr):
        return right_to_left[0]
    else:
        return False


if __name__ == '__main__':
    main()
