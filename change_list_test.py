from itertools import zip_longest

LIST_INIT = 'A, B, C, D, E, F, G, H, I, J, K, L, M, N'
LIST_MODI = 'B, C, D, A, F, E, Z, M, N, J, K, L'


def get_change_operation(list_init, list_modi, init, modi, index):
    """ get delta position of symbol init from list_init to list_modi """
    if modi in list_init:
        init_index = list_init.index(modi)
        return index - init_index
    else:
        # if replacement on index position
        if init not in list_modi:
            # new or replace
            return init
        else:
            return '+'
    

def list_change_test(list_init, list_modi):
    """ check if there is some changes of list elements from list0 to list1 """
    list_change = {}
    index = 0
    for init, modi in zip_longest(list_init, list_modi, fillvalue='?'):
        if init == modi:
            list_change[modi] = 0
        if modi == '?':
            if init not in list_modi:
                list_change[init] = '-'
        else:
            operation = get_change_operation(list_init, list_modi,
                                             init, modi, index)
            if init != '?' and init not in list_modi and init != operation:
                list_change[init] = '-'
            list_change[modi] = operation
        index += 1
    return list_change

if __name__ == '__main__':
    list_init = ''.join(LIST_INIT.split(', '))
    list_modi = ''.join(LIST_MODI.split(', '))
    change_list = list_change_test(list_init, list_modi)
    for key, value in change_list.items():
        description = ''
        if isinstance(value, int):
            if value == 0:
                description = 'нет изменений'
            elif value < 0:
                description = 'влево'
            else:
                description = 'вправо'
        elif value == '-':
            description = 'удалено'
        elif value == '+':
            description = 'добавлено'
        else:
            description = 'замена'
        print(f'{key}: {value} {description}')
