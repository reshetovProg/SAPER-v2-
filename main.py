import random
from config import lvl_size, PERCENT_BOMBS
field = []

def show_field():
    for i in field:
        for j in i:
            print(j, end=" ")
        print()
def generate_field():
    global field

    lvl = choose_lvl()
    size=lvl_size[lvl]
    field = [[0 for j in range(size)] for i in range(size)]
    # for i in range(size):
    #     field.append([])
    #     for j in range(size):
    #         field[i].append(0)
def choose_lvl():
    try:
        lvl = int(input("выберите уровень (1/2/3): "))
        if lvl not in [1, 2, 3]:
            raise Exception
    except:
        print("некорректные данные")
        choose_lvl()

    return lvl
def generate_bomb():
    size=len(field)
    count_bomb = int(size*size*PERCENT_BOMBS/100)
    while count_bomb>0:
        row = random.randint(0,size-1)
        column = random.randint(0, size - 1)
        if field[row][column]==2:
            continue
        field[row][column]=2
        count_bomb-=1

if __name__ == '__main__':
    generate_field()
    generate_bomb()
    show_field()
