import sys
def add_area(a, b, move):
    if area[a-1][b-1] != '*':
        return '-'
    if move == True:
        area[a-1][b-1] = 'X'
    else:
        area[a-1][b-1] = '0'

def draw():
    for i in range(3):
        print(area[i][0], area[i][1], area[i][2])

def check_winner():
    for i in area:
        if i[0] == i[1] and i[1] == i[2]:
            if i[0] == 'X':
                return 'X'
            elif i[0] == '0':
                return '0'
    for i in range(3):
        if area[0][i] == area[1][i] and area[1][i] == area[2][i]:
            if area[0][i] == 'X':
                return 'X'
            elif area[0][i] == '0':
                return '0'
    if (area[0][0] == area[1][1] and area[1][1] == area[2][2]) or (area[0][2] == area[1][1] and area[1][1] == area[2][0]):
            if area[1][1] == 'X':
                return 'X'
            elif area[1][1] == '0':
                return '0'

area = [["*" , "*" , "*"], ["*" , "*" , "*"], ["*" , "*" , "*"]]
count = 9
move = True


print ("  Добро пожаловать !")
print ("B крестики - нолики !")
print ("=====================")
print(' ')

while count > 0:
    if move == True:
        print('Ходят крестики:')
        a,b = map(int,input(' Введите координаты x,y: ').split())
        s = add_area(a, b, move)
        if s == '-':
            print('Занято! Ходите заново')
            continue
        draw()
        move = False
        count -= 1
    else:
        print('Ходят нолики :')
        a,b = map(int,input(' Введите координаты x,y: ').split())
        s = add_area(a,b, move)
        if s == '-':
            print('Занято! Ходите заново')
            continue
        draw()
        move = True
        count -= 1
    if check_winner() == 'X':
        print('win X')
        sys.exit()
    elif check_winner() == '0':
        print('win 0')
        sys.exit()

print('Ничья!')
