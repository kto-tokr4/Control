import random

map = [['', '', ''], ['', '', ''], ['', '', '']]


def show_map():
    for row in map:
        print(row)
    return 0


def check_all_map():
    '''Возвращает True если на карте еще есть свободные места и False если нет'''
    for row in map:
        if '' in row:
            return True
    return False


def check_motion(row, column):
    '''Возвращает True если во время хода была указана свободная клетка и False если нет'''
    return True if map[row][column] == '' else False


def player_motion():
    row = int(input('Ваш ход || Укажите номер строки:'))
    column = int(input('Ваш ход || Укажите номер столбца:'))
    if not check_motion(row, column):
        return False
    else:
        map[row][column] = '0'
        return True


def pc_motion():
    row = random.randint(0, 2)
    column = random.randint(0, 2)
    if not check_motion(row, column):
        return False
    else:
        map[row][column] = 'X'
        return True


def check_line(line):
    if line[0] == '0' and line[1] == '0' and line[2] == '0':
        return 'Win'
    elif line[0] == 'X' and line[1] == 'X' and line[2] == 'X':
        return 'Lose'


def check_win():
    lines = []
    column1 = []
    column2 = []
    column3 = []
    for row in map:
        lines.append(row)
        column1.append(row[0])
        column2.append(row[1])
        column3.append(row[2])
    horizont1 = [map[0][0], map[1][1], map[2][2]]
    horizont2 = [map[0][2], map[1][1], map[2][0]]
    lines.append(column1)
    lines.append(column2)
    lines.append(column3)
    lines.append(horizont1)
    lines.append(horizont2)

    for line in lines:
        if check_line(line):
            return check_line(line)


print('''Добро пожаловать в игру "Крестики-нолики"
В начале игры вы имеете право первого хода
Вы можете ставить "0" в любое свободное место поля 3x3
Нумерация столбцов и строк начинается от 0 и заканчивается 2
Победит тот, кто первый выстроит целую линию из трех одинаковых символов
     ''')

while True:
    while True:
        if not player_motion():
            print('Вами была указана занятая клетка')
        else:
            break
    show_map()
    print('-' * 20)
    if check_win() == 'Win':
        print('Вы победили! Поздравляем')
        break
    if check_all_map():
        while True:
            if pc_motion():
                break
        show_map()
        if check_win() == 'Lose':
            print('К сожалению, вы проиграли =(')
            break
    else:
        print('Все игровое поле занято. Объявлена ничья!')
        break
    print('Конец хода')
    print('*' * 20)


