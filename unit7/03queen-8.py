
#Define empty grid 
grid=[[0 for x in range(8)] for y in range(8)]


def possible(grid,y,x): #is it possible to place a queen into y,x?
    l=len(grid) #how big is our grid?
    for i in range(l): #check for queens on row y and column x
        if grid[y][i]==1 or grid[i][x] == 1:
            return False
    for i in range(l): #loop through all rows
        for j in range(l): #and columns
            if grid[i][j]==1 and abs(i - y) == abs(j - x): #if there is a queen diagonal
                return False #return false
    return True #if every check clears, we can return true


def solve(grid):
    l=len(grid) #length of our grid  
    for y in range(l): #for every row
        for x in range(l): #for every column
            if grid[y][x]==0: # we can place if there is no queen in given position
                if possible(grid,y,x): #if empty, check if we can place a queen
                    grid[y][x]=1 #if we can, then place it
                    solve(grid) #pass grid for recursive solution
                    #if we end up here, means we searched through all children branches
                    if sum(sum(a) for a in grid)==l: #if there are 8 queens
                        return grid #successfully find one
                    grid[y][x]=0 #remove the previous placed queen and continue search
    return # if comes here means finish all search did not find a solution


def print_solution(grid):
    l=len(grid) 
    for i in range(l):
        for j in range(l):
            print (grid[i][j],end=',')
        print()


solution = solve(grid) #get the solution
print_solution(solution)


