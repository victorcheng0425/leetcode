class Solution:
    #loop through array, search for '1'
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i , e in enumerate (grid):
            for j , element in enumerate (grid[i]):
                #print(j, element)
                if element == '1':
                    #print("In!!!!")
                    count += 1
                    self.DFS(grid, i, j)
                    #print(count)
        return count
    #DFS turn islands '1' to 2                
    def DFS(self, grid: List[List[str]], i, j):
        grid[i][j] = '2'
        left, right, top, down = 1, 1, 1, 1
        if i == 0 or grid[i-1][j] != '1':
            top = 0
        if i == len(grid) - 1 or grid[i+1][j] != '1':
            down = 0
        if j == 0 or grid[i][j-1] != '1':
            left = 0
        if j == len(grid[i]) - 1 or grid[i][j+1] != '1':
            right = 0
        #print(left, right, top, down)
        if top == 1:
            self.DFS(grid, i-1, j)
        if down == 1:
            self.DFS(grid, i+1, j)
        if left == 1:
            self.DFS(grid, i, j-1)
        if right == 1:
            self.DFS(grid, i, j+1)
        return
        

    
