from config import lvl_size
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


if __name__ == '__main__':
    generate_field()
    show_field()
