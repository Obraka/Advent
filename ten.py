import os

# Global variables are bad style, except this time!
peaks = set()

def mapmakea(raw):
    mapy = []
    for i in range(len(raw)):
        mapy.append(list(raw[i]))

    # Change all values to INT
    for i in range(len(mapy)):
        mapy[i] =  [ int(x) for x in mapy[i] ]

    return mapy

def headfinda(mapy):
    heads = []
    for index in range(len(mapy)):
        for indexi, data in enumerate(mapy[index]):
            if data == 0:
                location = []
                location.append(index)
                location.append(indexi)
                heads.append(location)
    return heads     

def pathfinda(value, row, column, mapy):
    score = 0
    # Get all legal neighboring positions (max 4)
    neighbors = neighbora(row, column, mapy)
    # If search value is 10 add to score and break
    if (value == 10):
        score += 1
        return score
    for i in range(len(neighbors)):
        # If point is legal run again with value + 1
        if pointchecka(value, neighbors[i][0], neighbors[i][1], mapy):
            score +=pathfinda(value+1, neighbors[i][0], neighbors[i][1], mapy)
    return score 

def neighbora(row, column, mapy):
    neighbors = []
    # Generate all legal neighboring positions (max 4)
    # Left right
    if column - 1 >= 0:
        cord = []
        cord.append(row)
        cord.append(column - 1)
        neighbors.append(cord)
    if column + 1 < len(mapy[row]):
        cord = []
        cord.append(row)
        cord.append(column + 1)
        neighbors.append(cord)
    # Up down
    if row - 1 >= 0:
        cord = []
        cord.append(row-1)
        cord.append(column)
        neighbors.append(cord)
    if row + 1 < len(mapy):
        cord = []
        cord.append(row+1)
        cord.append(column)
        neighbors.append(cord)
    return neighbors
    
def peakcounta(value, row, column, mapy):
    score = 0
    neighbors = neighbora(row, column, mapy) 
    # If search value is 10 add to seen peaks and break
    if (value == 10):
        string = "" 
        string += str(row)
        string += "/"
        string += str(column)
        peaks.add(hash(string))
        return score
    for i in range(len(neighbors)):
        # If point is legal run again with value + 1
        if pointchecka(value, neighbors[i][0], neighbors[i][1], mapy):
            score +=peakcounta(value+1, neighbors[i][0], neighbors[i][1], mapy)
    return score

def pointchecka(value, row, column, mapy):
    if mapy[row][column] == value:
        return True
    else:
        return False

if __name__ == "__main__":
    answer = 0
    file = os.path.dirname(os.path.realpath(__file__))
    file += "\input10"
    with open(file) as inputfile:
        raw = [line.rstrip() for line in inputfile]
    mapy = mapmakea(raw)
    heads = headfinda(mapy)
    # Part I 
    for i in range(len(heads)):
        peakcounta(1, heads[i][0], heads[i][1], mapy)
        answer += len(peaks)
        peaks.clear()
    print("Task 1:", answer)
    answer = 0
    # Part II
    for i in range(len(heads)):
        answer += pathfinda(1, heads[i][0], heads[i][1], mapy)
    print("Task 2:", answer)
    
