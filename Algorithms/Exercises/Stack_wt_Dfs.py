
maze = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
        [1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1],
        [1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1],
        [1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,1],
        [1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1],
        [1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1],
        [1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1],
        [1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1],
        [1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1],
        [1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1],
        [1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

dirs = [
    lambda x,y: (x-1,y),
    lambda x,y: (x,y+1),
    lambda x,y: (x+1,y),
    lambda x,y: (x,y-1)
]

def Maze_dfs(x1,y1,x2,y2):
    path = []
    path.append((x1,y1))
    while len(path)>0:
        CurNode = path[-1]
        #print(path)
        if CurNode[0] == x2 and CurNode[1] == y2:
            for p in path:
                print(p,end='->')
            print('End')
            return True
        for dir in dirs:
            NextNode = dir(CurNode[0],CurNode[1])
            if maze[NextNode[0]][NextNode[1]] == 0:
                path.append(NextNode)
                maze[NextNode[0]][NextNode[1]] = 2
                break
        else:
            maze[NextNode[0]][NextNode[1]] = 2
            path.pop()
    else:
        print("There is No one Path")
        return False

Maze_dfs(1,1,5,13)