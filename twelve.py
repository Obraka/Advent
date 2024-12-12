import os
import copy
import time

def inputchecka(rowv, colv, letter, partof, groups, bounds, fine):
    tmpgrp = []
    # Checked item starts a new group
    tmpgrp.append(letter)
    # Area at the start is always 0
    tmpgrp.append(0)
    # Circumfence starts at 0
    tmpgrp.append(0)
    # Add dir changes
    tmpgrp.append(0)
    # Get neighbors of current pos
    neighbor_checka(rowv, colv, letter, partof, groups, bounds, tmpgrp, fine, 0)
    # Set original partof to 1 (even if all neighbors fail it's a plot)
    fine[rowv][colv][1] = 1
    # If no legal neighbors set area to 1
    if (tmpgrp[1] == 0):
        tmpgrp[1] = 1
    # Add plot to groups
    groups.append(tmpgrp)

def neighbor_checka(rowv, colv, letter, partof, groups, bounds, tmpgrp, fine, dir):
    corners = 0
    # Skip if part of plot
    if (partof == 1):
        return
    # dir, 1 = up, 2 = down, 3 = left, = right
    neighbors = [[rowv-1, colv, 1],[rowv+1, colv, 2], [rowv, colv-1, 3], [rowv, colv+1, 4]]
    # Make check for all neighboring fields
    for items in neighbors:
        if (same_letter(items[0], items[1], letter, bounds, fine)):
            # If the found letter is already part of the group (1) don't count it
            if fine[rowv][colv][1] == 0:
                tmpgrp[1] += 1
            # Set partof original search  to 1
            fine[rowv][colv][1] = 1
            # Run again for new values, old letter
            neighbor_checka(items[0], items[1], letter, fine[items[0]][items[1]][1], groups, bounds, tmpgrp, fine, items[2])    
        else:
            # Add to circumfence of plot
            tmpgrp[2] += 1

def same_letter(row, column, letter, bounds, fine):
    # If out of bounds, count as fence (return false)
    if (row < 0 or column < 0 or row > bounds-1 or column > bounds-1):
        return False
    # If same letter and not part of group set part of to 1 and return true    
    elif (fine[row][column][0] == letter):
        return True
    else:
        return False

def init_data(raw, fine):
    for index, line in enumerate(raw):
        columns = list(line)
        fine[index] = []
        for letter in columns:
            tmp= []
            tmp.append(letter)
            tmp.append(0)
            fine[index].append(tmp)


if __name__ == "__main__":
    start = time.time()
    groups = []
    file = os.path.dirname(os.path.realpath(__file__))
    file += "\input\input12s"
    with open(file) as inputfile:
        raw = [line.rstrip() for line in inputfile]
    fine = {}
    init_data(raw, fine)
    bounds = len(fine)    
    for row in fine.items():
        for colindex in range(len(row[1])):
            # Only check if not part of plot yet
            if row[1][colindex][1] == 0:
                inputchecka(row[0], colindex, row[1][colindex][0], row[1][colindex][1], groups, bounds, fine)
    answerone = 0
    answertwo = 0
    for values in groups:
        answerone += values[1]*values[2]
        answertwo += values[1]*(values[3]*2)
    end = time.time()
    print("Answer 1:", answerone, "in", round(((end-start)*1000), 5), "ms")
    init_data(raw, fine)

    print("Answer 2:", answertwo, "in", round(((end-start)*1000), 5), "ms")
    print(fine)
