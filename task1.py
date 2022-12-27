# Сделать программу расписание - делаем расписание занятий\тренировок или что-то своё.
# Для хранения информации используем текстовые файлы (сохраняем, перезаписываем в них и т.д.) , бесконечный цикл, функции и прочий функционал.
# Программа будет, как консольный бот, который будет нас спрашивать что и как нужно сделать - вывести, показать, перезаписать , добавить событие в определенный день недели

def check_usr_input_num(prase):
    '''
    Бесконечно просит ввести число пока оно не будет введено
    В аргумент prase передаем строку (приглашение для ввода)
    '''
    while True:
            input_usr = input(prase)
            if input_usr == '':
                return ''
            try:
                int(input_usr)
                return int(input_usr)
            except ValueError:
                print('Ввод не верный, попробуйте еще раз!')
                continue

def print_my_day(day):
    '''
    Выводит все задачи на день из файла
    '''
    with open(day, encoding='utf-8') as f:
        print(f.read())

def get_len_lines_file(day):
    '''
    Возвращает количество строк в файле
    '''
    with open(day, encoding='utf-8') as f:
        len_list = len(f.readlines())
    return len_list

def get_list_lines_file(day):
    '''
    Возвращает список из строк, которые были в файле
    '''
    with open(day, encoding='utf-8') as f:
        lines_list = f.readlines()
    return lines_list

days_dict = {1: 'mo.txt', 2:'tu.txt', 3:'we.txt', 4:'th.txt', 5:'fr.txt', 6:'sa.txt', 7:'su.txt'}

while True:
    num_day_input = check_usr_input_num('Выберете день недели 1-пн, 2-вт, 3-ср, 4-чт, 5-пт, 6-сб, 7-вс: ')
    if num_day_input == '' or (num_day_input < 1 or num_day_input > 7):
        print('Такого дня в неделе нет, попробуйте еще раз!')
        continue
    correct_day = days_dict[num_day_input]
    print_my_day(correct_day)
    do = check_usr_input_num('Введите, что нужно сделать: 1-добавить новую задачу, 2-изменить созданую задачу, 3-заново заполнить день задачами или нажмите Enter чтобы вернуться к списку дней: ')
    if do == 1:
        while True:
            len_task = get_len_lines_file(correct_day)
            usr_txt = input('Введите описание задачи или нажмите Enter чтобы закончить добавление: ')
            if usr_txt == '':
                break
            with open(correct_day, 'a', encoding='utf-8') as f:
                f.write(f'{len_task+1}) {usr_txt}\n')
            print_my_day(correct_day)

    elif do == 2:
        while True:
            len_task = get_len_lines_file(correct_day)
            usr_correct_task = check_usr_input_num('Введите номер задачи, которую нужно изменить или нажмите Enter чтобы закончить добавление: ')
            if usr_correct_task == '':
                break
            elif usr_correct_task < 1 or usr_correct_task > len_task:
                print('Задачи под таким номером нет, попробуйте еще раз!')
                print_my_day(correct_day)
                continue
            usr_txt = input('Введите новое описание задачи: ')
            list_lines = get_list_lines_file(correct_day)
            list_lines[usr_correct_task-1] = f'{usr_correct_task}) {usr_txt}\n'
            with open(correct_day, 'w', encoding='utf-8') as f:
                for i in list_lines:
                    f.write(i)
            print_my_day(correct_day)

    elif do == 3:
        len_arr_task = check_usr_input_num('Введите сколько задач нужно создать или нажмите Enter чтобы закончить: ')
        if len_arr_task == '':
                continue
        elif len_arr_task < 1:
                print('Нельзя создать меньше одной задачи, возвращаю на список дней!')
                continue
        arr_task = []
        count = 1
        while count <= len_arr_task:
            usr_txt = input(f'Введите описание задачи номер {count} или нажмите Enter чтобы закончить: ')
            if usr_txt == '':
                break
            arr_task.append(f'{count}) {usr_txt}\n')
            count+=1
        with open(correct_day, 'w', encoding='utf-8') as f:
                for i in arr_task:
                    f.write(i)
        print_my_day(correct_day)

    else:
        print('Возвращаю на список дней!')