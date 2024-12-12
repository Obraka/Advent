import os

def read_file():
    file_path = os.path.dirname(os.path.realpath(__file__))
    file_path += '\input4'
    file = open(file_path, 'r')
	
    values = file.read()
    file.close()
    return values

def listify(input):
    # Create a listitem for every line
    output =input.splitlines()

    for i in range(int(len(output))):
    # Split the lines into list items
        output[i] = list(output[i])
    
    return output

def part_one(input):
    word = list("XMAS")
    count = 0
    for i in range(int(len(input))):
        for j in range(int(len(input[i]))):
            # Find the first letter
            if (input[i][j] == word[0]):  
                # Check if left is possible
                if(j >= len(word)-1):
                    for k in range(1, int(len(word))):
                        if (input[i][j-k]==word[k]):
                            if (k == int(len(word))-1):
                                count = count +1
                        else:
                            break

                # Check if right is possible
                if(j+len(word)-1 < len(input[i])):
                    for k in range(1, int(len(word))):
                        if (input[i][j+k]==word[k]):
                            if (k == int(len(word))-1):
                                count = count +1
                        else:
                            break                   

                # Check if up is possible
                if(i-(len(word)-1) >= 0):
                    for k in range(1, int(len(word))):
                        if (input[i-k][j]==word[k]):
                            if (k == int(len(word))-1):
                                count = count +1
                        else:
                            break                   

                # Check if down is possible
                if(i+len(word)-1 < len(input)):
                    for k in range(1, int(len(word))):
                        if (input[i+k][j]==word[k]):
                            if (k == int(len(word))-1):
                                count = count +1
                        else:
                            break 

                # Check if diag up left is possible
                if(i-(len(word)-1) >= 0 and j >= len(word)-1):
                    for k in range(1, int(len(word))):
                        if (input[i-k][j-k]==word[k]):
                            if (k == int(len(word))-1):
                                count = count +1
                        else:
                            break   

                # Check if diag up right is possible
                if(i-(len(word)-1) >= 0 and j+len(word)-1<len(input[i])):
                    for k in range(1, int(len(word))):
                        if (input[i-k][j+k]==word[k]):
                            if (k == int(len(word))-1):
                                count = count +1
                        else:
                            break     
                # Check if diag down left is possible
                if(i+len(word)-1 < len(input) and j >= len(word)-1):
                    for k in range(1, int(len(word))):
                        if (input[i+k][j-k]==word[k]):
                            if (k == int(len(word))-1):
                                count = count +1
                        else:
                            break   
              
                # Check if diag down right is possible
                if(i+len(word)-1 < len(input) and j+len(word)-1 < len(input[i])):
                    for k in range(1, int(len(word))):
                        if (input[i+k][j+k]==word[k]):
                            if (k == int(len(word))-1):
                                count = count +1
                        else:
                            break   
                                                                 
    return count

def part_two(input):
    word = list("MAS")
    extr = int((len(word)-1)/2)
    count = 0
    for i in range(int(len(input))):
        for j in range(int(len(input[i]))):
            # Find the middle letter
            if (input[i][j] == word[1]):  

                # Check if diag up left is possible
                if(i-extr >= 0 and j >= extr):
                    # Check if diag up right is possible
                    if(i-extr >= 0 and j+extr<len(input[i])):
                        # Check if diag down left is possible
                        if(i+extr < len(input) and j >= extr):
                            # Check if diag down right is possible
                            if(i+extr < len(input) and j+extr < len(input[i])):

                                # Left Top and Bottom right check
                                    if ((input[i-1][j-1] == word[0] and input[i+1][j+1] == word[2]) or ((input[i-1][j-1] == word[2] and input[i+1][j+1] == word[0]))):
                                    # Top Right and Bottom left check
                                        if ((input[i-1][j+1] == word[0] and input[i+1][j-1] == word[2]) or ((input[i-1][j+1] == word[2] and input[i+1][j-1] == word[0]))):   
                                            count = count + 1                                     
                                
                                                                 
    return count
def main():
    raw = read_file()
    fine = listify(raw)
    print("Pt 1: ",part_one(fine))
    print("Pt 2: ",part_two(fine))
main()