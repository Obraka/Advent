import os
import string
import itertools

def get_locations(raw):
    # Make dict with all antennas
    symbols = list(string.ascii_letters+string.digits)
    locations = dict()
    for index, letter in enumerate(symbols):
        locations[letter] = list()

    # Loop through the input lines
    for index, row in enumerate(raw):
        # Turn the input str into a list
        rowdata = list(row)

        # Loop through the list with input data
        for indexc, column in enumerate(row):
            # Check if . if not, add coordinates to locations
            if not(column == "."):
                # Make pos into a new list to store
                pos = []
                pos.append(index)
                pos.append(indexc)
                locations[column].append(pos)

    return locations

def get_interference(locations, bounds):
    interferences = set()
    p = 0
    # Loop through the lines of the dict
    for index, data in enumerate(locations):
        # Loop through the locations
        # Get all location permutations to compare
        combis = list(itertools.permutations(locations[data], 2))

        for indexl, datal in enumerate(combis):
            difrow = datal[1][0]-datal[0][0]
            difcol = datal[1][1]-datal[0][1]

            # Check if possible interference upleft is within bounds
            if (datal[0][0]-difrow>=0 and datal[0][0]-difrow<bounds[0] and datal[0][1]-difcol<bounds[1] and datal[0][1]-difcol>=0):
                # Make a string out of the location to hash it into the set
                interferences.add(hash(strfy(datal[0][0]-difrow, datal[0][1]-difcol)))

            # Check if interference downright is within bounds
            if (datal[1][0]+difrow>=0 and datal[1][0]+difrow<bounds[0] and datal[1][1]+difcol<bounds[1] and datal[1][1]+difcol>=0):
                interferences.add(hash(strfy(datal[1][0]+difrow, datal[1][1]+difcol)))
    return interferences

def strfy(row, col):
    tmpstr = ""
    tmpstr += str(row)
    tmpstr += ":"
    tmpstr += str(col)
    return tmpstr

def get_interference_resonate(locations, bounds):
    interferences = set()
    p = 0
    # Loop through the lines of the dict
    for index, data in enumerate(locations):
        # Loop through the locations
        # Get all location permutations to compare
        combis = list(itertools.combinations(locations[data], 2))
        for indexl, datal in enumerate(combis):
            difrow = datal[1][0]-datal[0][0]
            difcol = datal[1][1]-datal[0][1]
            # Use the up left antenna as first point for the new locations
            nrow = datal[0][0]
            ncol = datal[0][1]

            # The upper antenna is always a node, 
            if difrow > 0:
                interferences.add(hash(strfy(nrow, ncol)))
            elif difrow < 0:
                interferences.add(hash(stryf(datal[1][0], datal[1][1])))

            # As long as the answer is within bounds record it
            while (1):
            # Move up left as far as possible within movement rules break if out of bounds after calc
                nrow -= difrow
                ncol -= difcol
                if not(nrow >= 0 and nrow < bounds[0] and ncol >= 0 and ncol < bounds[1]):
                    break
                interferences.add(hash(strfy(nrow, ncol)))
            
            # As long as the answer is within bounds record it    
            while ( 1):
            # Move down right as far as possible within movement rules break if out of bounds after calc
                nrow += difrow
                ncol += difcol
                if not(nrow >= 0 and nrow < bounds[0] and ncol >= 0 and ncol < bounds[1]):
                    break
                interferences.add(hash(strfy(nrow, ncol)))

    return interferences

def get_bounds(raw):
    bounds = []
    bounds.append(len(raw))
    bounds.append(len(list(raw[0])))
    return bounds

if __name__ == "__main__":
    file = os.path.dirname(os.path.realpath(__file__))
    file += "\input8"
    with open(file) as inputfile:
        raw = [line.rstrip() for line in inputfile]      
    # Task 1
    bounds = get_bounds(raw)
    locations = get_locations(raw)
    print("Task 1:", len(get_interference(locations, bounds)))
    print("Task 2:", len(get_interference_resonate(locations, bounds)))

