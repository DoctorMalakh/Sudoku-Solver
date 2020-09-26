'''sudoku solver'''

#%%
board = [
    [7,8,5,4,3,9,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]



#%%

def print_board(bo):
    for i in range(len(bo)):
        if i%3 == 0 and i != 0:
            print("--------------------")

        for j in range(len(bo[0])):
            if j%3 == 0 and j!=0:
                print('|', end='')
                
            if j != 8:
                print(str(bo[i][j]) + ' ', end='')
                
            else: 
                print(bo[i][j])
                
    print("", '~~~~~~~~~~~~~~~~~~~~',"",sep='\n')

#%%

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:

                return (i,j)
    return None




#%%
def validation(bo, pos, num):
    row = pos[0]
    column = pos[1]

    #check row
    for i in range(len(bo[0])):
        if num == bo[row][i] and i != column:
            return False
                
    #check column
    for i in range(len(bo)):
        if num == bo[i][column] and i != row:
            return False

    #check box
    box_row = row//3
    box_column = column//3

    for i in range(box_row*3, box_row*3 + 3):
        for j in range(box_column*3, box_column*3 + 3):
            if num == bo[i][j] and (i,j) != pos:
                return False


    return True






#%%
def solve(bo):
    if find_empty(bo) == None:
        return True

    row, column = find_empty(bo)



    for i in range(1,10):
        if validation(bo,(row, column),i):
            bo[row][column] = i


            if solve(bo):
                return True

            bo[row][column] = 0


    return False








#    print(row, column, sep=' ')

print("","","","", sep='\n')
print_board(board)

solve(board)

print_board(board)
# %%
