print(22*"-","\n\tПриветствуем вас\n\t\t в игре\n\tкрестики-нолики", '\n',22*"-")
print(' формат ввода: x y\n x - номер строки\n y - номер столбца\n')
'''
A = list(('   | 0 | 1 | 2 | \n',
      15*'-', '\n 0 |   |   |   | \n',
      15*'-', '\n 1 |   |   |   | \n',
      15*'-', '\n 2 |   |   |   | \n', 15*'-'))

print(A)
'''
board = list(range(1,10))
print(board)

def draw_board(board):
    print('-------------')
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3], "|", board[2+i*3], "|" )
        print('-------------')
        
draw_board(board)

dict1 = dict()
list2=[]

for i in range(3):
    for j in range(3):
        list1 = []
        list1.append(i)
        list1.append(j)
        list2.append(list1)


        
list3 = list(range(1,10))

dict1 = dict.fromkeys(list3)
for k, v in dict1:
    print(k,v)



        

