import random
from config import lvl_size, PERCENT_BOMBS
field = []

def show_field_without_bombs():
    for i in field:
        for j in i:
            print(j if j!=2 else 0, end=" ")
        print()
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
def init():
    generate_field()
    generate_bomb()
def player_step():
    try:
        row=int(input("введите номер строки: "))
        column = int(input("введите номер столбца: "))
        if row not in range (1,len(field)+1) or column not in range (1,len(field)+1):
            raise Exception
        else:
            return {"row": row - 1, "column": column - 1}
    except:
        print("некорректные данные")
        return player_step()

def game():
    size=len(field)
    count_bomb = int(size*size*PERCENT_BOMBS/100)
    count_step = size*size-count_bomb
    while count_step>0:
        show_field_without_bombs()
        step = player_step()
        if field[step["row"]][step["column"]]==2:
            show_field()
            print("BOOM")
            exit()
        field[step["row"]][step["column"]] = 1
        count_step-=1
    show_field()
    print("WIN")
    exit()


if __name__ == '__main__':
    init()
    game()

