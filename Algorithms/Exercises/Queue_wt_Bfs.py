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

