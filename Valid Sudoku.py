#stupid
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 0
        j = 0
        box = 0
        x = 0
        while(x < 9):
            li = [0]*10
            j = x
            while(i < 9):
                if board[i][j] == ".":
                    i += 1
                    continue
                #print(x,i,j)
                if li[int(board[i][j])] is 1:
                    print("A", "x: ", x, "i: ", i, "j: ", j)
                    return False
                li[int(board[i][j])] = 1
                i += 1
            j = 0
            li = [0]*10
            i = x
            while(j < 9):
                if board[i][j] == ".":
                    j += 1
                    continue
                if li[int(board[i][j])] is 1:
                    print("b", "x: ", x, "i: ", i, "j: ", j)
                    return False
                li[int(board[i][j])] = 1
                j += 1
            if x == 0 or x == 3 or x ==6:
                j = 0
            elif x == 1 or x == 4 or x == 7:
                j = 3
            elif x == 2 or x == 5 or x == 8:
                j = 6
            if x == 0 or x == 1 or x == 2:
                i = 0
            elif x == 3 or x == 4 or x == 5:
                i = 3
            elif x == 6 or x == 7 or x == 8:
                i = 6
            temp = j
            li = [0]*10
            while(box < 9):
                if box == 3 or box == 6:
                    i += 1
                    j = temp
                print("d", x,i,j)
                if board[i][j] == ".":
                    box += 1
                    j += 1
                    continue
                if li[int(board[i][j])] is 1:
                    print(li)
                    return False
                li[int(board[i][j])] = 1
                j += 1
                box += 1
            box = 0
            i = 0
            j = 0
            x += 1
        return True
#smart
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boards=[[set() for _ in range(3)] for _ in range(3)]
        for row,row_ in enumerate(board):
            for col,num in enumerate(row_):
                if num!='.':
                    in_1=row//3
                    in_2=col//3
                    if num in (rows[row] |cols[col] |boards[in_1][in_2]):
                        return False
                    rows[row].add(num)
                    cols[col].add(num)
                    boards[in_1][in_2].add(num)
        return  True
