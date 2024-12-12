import os	
score = 0

def read_file():
    file_path = 'C:\\Users\\rodle\\source\\repos\\Advent\\listtwo'
    file = open(file_path, 'r')
	
    values = file.read()
    file.close()
    return values

def safety(input):
    # dir 1 = asc, dir 0 = desc
    dir = 0
    scr = 0
    safeval = 1
    for i in input.splitlines():
        j = i.split(' ')
        # Check direction of first values
        if (j[1]>j[0]):
            dir = 1
        else:
            dir = 0

        for k in range(1,int(len(j))-1):
            
            tmp = int(j[k])-int(j[k-1])
            if (dir == 1 and tmp > 0 and tmp <= 3):
                safeval = 1
            elif (dir == 0 and tmp >=-3 and tmp < 0):
                safeval = 1
            else:
                safeval = 0
                break
        if (safeval == 1):
            scr=scr+1  
  
    return scr

def damp(input):
    safe = 0
    diffs = []
    for i in input.splitlines():
        values = i.split(" ")
        # Get all differences from a line
        for j in range(int(len(values))-1):
            diffs.insert(j,int(values[j])-int(values[j+1]))
        
        # Check if the test was safe without dampening
        if (check(diffs)):
            safe = safe + 1
        else:
        # Remove one result and try again
            for l in range(int(len(diffs))):
                # Refresh tmp differences
                tmpdif = diffs
                 # Remove item 
                
                tmpdif = tmpdif.pop(l)
                print(tmpdif)
                if (check(tmpdif)):
                    safe = safe + 1
                    break
       
        
        del diffs[:]
    return safe
        
        
        



def main():
    raw = read_file()
    # print(safety(raw))
    print(safety(raw))
    print(damp(raw))
main()