import os
import copy

def checka(input):
    answer = {}
    answer["Testing"] = 1
    #guard[line, colum, dir, visited, out]
    guard = []
    startguard = []
    obstacles = {}
    tmpobst = {}
    mlines = len(input)-1

    # Read in map, get guard location and obstacles
    for index, data in enumerate(input):
        mcol = len(data)-1
        obstacles[index] = []
        for columindex, columdata in enumerate(data):
            # Check if obstacle
            if (columdata == "#"):
                obstacles[index].append(columindex)
            # Check if empty
            elif (columdata == "."):
                pass
            # Else it's the guard
            else:
                guard.append(index)
                guard.append(columindex)
                # Dir up = 1, left 2, right 3, down 4
                if (columdata == '^'):
                    guard.append(1)
                elif (columdata == '<'):
                    guard.append(2)
                elif (columdata == '>'):
                    guard.append(3)
                elif (columdata == 'v'):
                    guard.append(4)
                guard.append({})
                guard.append(0)
                startguard = guard[:]
    guard[4] = 0
    while guard[4] < 1:
        guard = move(guard, obstacles, mlines, mcol)
    
    # Task 1

    answer[1] = int()
    for line, data in enumerate(guard[3]):
        answer[1] += len(guard[3][line])

    # Task 2

    answer[2] = int()

    for line, data in enumerate(guard[3]):
        print ("Line ", line+1, "of ", len(guard[3]))
        for item, rdata in enumerate(guard[3][data]):
            # Add current visited square to obstacles
            tmpobst = copy.deepcopy(obstacles)
            tmpobst[data].append(rdata)

            loop: int
            tmpguard = copy.deepcopy(startguard)
            # Check if loop
            for i in range(50000):
                tmpguard = move(tmpguard, tmpobst, mlines, mcol)
                if (tmpguard[4]):
                    loop = 0
                    break
                else:
                    loop = 1            

            if (loop > 0):
                answer[2] += 1


    return answer

def move(mguard, obstacles, mlines, mcol):
    # Check direction
    gline = mguard[0]
    gcol = mguard[1]
    cline: int
    ccol: int
    ndir: int
    match mguard[2]:
        # Up
        case 1:
            cline = gline-1
            ccol = gcol
        # Left
        case 2:
            cline = gline
            ccol = gcol - 1
        # Right
        case 3:
            cline = gline
            ccol = gcol + 1
        #Down
        case 4:
            cline = gline + 1
            ccol = gcol
    # Check for obstacle
    try:
        if (int(ccol) in obstacles[cline]):
            match mguard[2]:
                case 1:
                    ndir = 3              
                case 2:
                    ndir = 1        
                case 3:
                    ndir = 4   
                case 4:
                    ndir = 2

            if (ndir):
                mguard[2] = ndir
        else:
            mguard[0] = cline
            mguard[1] = ccol

    except:
        pass
    if not(gline in mguard[3]):
        mguard[3][gline] = set()
    mguard[3][gline].add(gcol)

    # Check if 'freedom'
    if ccol > mcol or ccol < 0 or cline < 0 or cline > mlines:
        mguard[4] = 1
    return mguard

def main():
    file = os.path.dirname(os.path.realpath(__file__))
    file += "\input6.txt"

    with open(file) as inputfile:
        raw = [line.rstrip() for line in inputfile]  
    fine = []
    for line in raw:
        fine.append(list(line))
    results = checka(fine)
    print("Task 1: ", results[1])
    print("Task 2: ", results[2]-1)

main()