from pyamaze import maze,agent,COLOR

def RCW():
    global direction
    k=list(direction.keys())
    v=list(direction.values()) 
    v_rotated=[v[-1]]+v[:-1]
    direction=dict(zip(k,v_rotated))

def RCCW():
    global direction
    k=list(direction.keys())
    v=list(direction.values()) 
    v_rotated=v[1:]+[v[0]]
    direction=dict(zip(k,v_rotated))

def moveForward(cell):
    if direction['forward']=='E':
        return (cell[0],cell[1]+1),'E'
    if direction['forward']=='W':
        return (cell[0],cell[1]-1),'W'
    if direction['forward']=='N':
        return (cell[0]-1,cell[1]),'N'
    if direction['forward']=='S':
        return (cell[0]+1,cell[1]),'S'

def wallFollower(m):
    global direction
    direction={'forward':'N','left':'W','back':'S','right':'E'}
    currCell=(m.rows,m.cols)
    path=''
    while True:
        if currCell==(1,1):
            break
        if m.maze_map[currCell][direction['left']]==0:
            if m.maze_map[currCell][direction['forward']]==0:
                RCW()
            else:
                currCell,d=moveForward(currCell)
                path+=d
        else:
            RCCW()
            currCell,d=moveForward(currCell)
            path+=d
    while 'EW' in path or 'WE' in path or 'NS' in path or 'SN' in path:
        path=path.replace('EW','')
        path=path.replace('WE','')
        path=path.replace('NS','')
        path=path.replace('SN','')

    return path


if __name__ == '__main__':
    myMaze=maze(20,30)
    myMaze.CreateMaze(theme=COLOR.light,loopPercent=20)

    b=agent(myMaze)
    a=agent(myMaze,shape='arrow',footprints=True,color=COLOR.green)
    path=wallFollower(myMaze)
    myMaze.tracePath({a:path})

    print(path)
    myMaze.run()