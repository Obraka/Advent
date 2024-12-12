import os
import copy

def get_unsorted(row):
    unsorted = []
    extindex = 0
    for index, value in enumerate(row):
        # Check if number is odd (information) or even (spaces)
        if index % 2 == 0:
            for indexd in range(int(value)):
                unsorted.append(extindex)
            extindex += 1
        else:
            # Write ID value times
            for indexd in range(int(value)):
                unsorted.append(None)
    return unsorted

def get_sorted_simple(unsorted):
    worklist = unsorted
    # Loop through the unsorted list
    for index, data in enumerate(unsorted):
        # Empty values get filled with the last item of the worklist
        if data == None:
            # Delete nones at the end
            while worklist[-1] == None:
                del worklist[-1]    
            worklist[index] = worklist[-1]
            # The last item is then deleted
            del worklist[-1]
    return worklist

def make_checksum(sorted):
    answer = 0
    for i, data in enumerate(sorted):
        # Added check for None for part 2
        if not(data == None):
            answer += i * int(data)
    return answer

def get_unsorted_frag(row):
    unsortednums = []
    unsortedspaces = []
    extindex = 0
    for index, value in enumerate(row):
        # Check if number is odd (information) or even (spaces)
        if index % 2 == 0:    
                unsortednums.append(int(value))
        else:
                unsortedspaces.append(int(value))
    unsorted = []
    unsorted.append(unsortednums)
    unsorted.append(unsortedspaces)
    return unsorted

def get_sorted_frag(unsorted):
    # Get nicer variables
    unsortednums = unsorted[0]
    unsortedspaces = unsorted[1]
    # Get file ids with same index as nums
    fileid = list(range(len(unsortednums)))
    # Add one 0 at the end of spaces for spaces after last item
    unsortedspaces.append(0)
    # Combine all 3 lists into one dict
    map = {}
    for data in fileid:
        map[data] = []
        map[data].append(data)
        map[data].append(unsortednums[data])
        map[data].append(unsortedspaces[data])

    finalorder = []
    checked = [0]
    # Check until you checked em all!
    while len(checked) <= len(map)-1:
        # Loop backwards through the dict 
        for index in reversed(list(range(0, len(map)))):
            # Every fileid map[index][0] may only be checked once
            if map[index][0] in checked:
                continue
            checked.append(map[index][0])
            # Loop forwards through the dict to check between 0 and the current-1
            for indexi in range(index):
                # Check if map[indexi][2] (spaces after) is same or larger than map[index][1] (Number of digits)
                if map[indexi][2] >= map[index][1]:
                    # Get current fileid, space left of hit and cache it, also cache whole original data
                    current = map[index][0]
                    hit = map[indexi][0]
                    curspace = map[index][2]
                    hitspace = map[indexi][2]
                    numlen = map[index][1]
                    cache = map[index].copy()

                    # Check if new position is new
                    if not(index == indexi+1):
                        # Copy all data between hit+1 and original position one row higher, map[index] gets overwritten
                        for i in reversed(list(range(indexi+1,index+1))):
                            map[i] = map[i-1]
                        # Insert original data back at new position (hit+1)
                        map[indexi+1] = cache
                    
                    # Change spaces left at data position (old-length)
                    map[indexi+1][2] = hitspace-numlen
                    
                    # Change hit spaces left to 0
                    map[indexi][2] = 0
                    # Change spaces left at old position
                    map[index][2] += curspace+numlen
                    break
            else:
                # Continue if no changes
                continue
            # Break loop if changes were made
            break
    return map

def make_list_frag(map):
    sorted = []
    for i in map:
        # Write map[i][0] map[i][1] times
        for a in range(map[i][1]):
            sorted.append(map[i][0])
        # Add spaces
        for a in range(map[i][2]):
            sorted.append(None)
    return sorted

if __name__ == "__main__":
    file = os.path.dirname(os.path.realpath(__file__))
    file += "\input9"
    with open(file) as inputfile:
        raw = [line.rstrip() for line in inputfile]
    # Task 1
    unsorted = get_unsorted(list(raw[0]).copy())
    sorted = get_sorted_simple(unsorted.copy())
    print ("Task 1", make_checksum(sorted))
    # Task 2
    unsorted = get_unsorted_frag(list(raw[0]).copy())
    sorted = get_sorted_frag(unsorted.copy())
    fraglist = make_list_frag(sorted)
    print ("Task 2", make_checksum(fraglist))