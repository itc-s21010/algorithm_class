def walk(x, y):
    global goal
    maze[y][x] = 2
    print_maze()
    if x==gx and y==gy:
        goal = True
    if goal==False and maze[y-1][x]==0:
        walk(x, y-1)
    if goal==False and maze[y+1][x]==0:
