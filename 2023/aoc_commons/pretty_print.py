

def two_d_list(two_dimension_list):
    for row in two_dimension_list:
        for element in row:
            print(element, end='')
        print(' ')
    return


def dict_new_line(dict):
    for i, e in dict.items():
        print(i, ' : ', e)