import os
import random

badorders = []

def read_file():
    file_path = os.path.dirname(os.path.realpath(__file__))
    file_path += '\input5'
    file = open(file_path, 'r')
	
    values = file.read()
    file.close()
    return values

def read_data(input, flag):
    tmp = input.splitlines()
    outputdir = {}
    output = []
    indexint = 0
    # Check for | (rules)
    for i in range(int(len(tmp))):
        if (tmp[i].find("|")>0):
            val = tmp[i].split("|")
            if (int(val[0]) in outputdir):
                cache = outputdir[int(val[0])]
                cache.append(int(val[1]))
                outputdir[int(val[0])] = cache
            else:
                cache = []
                cache.append(int(val[1]))
                outputdir[int(val[0])] = cache
        elif (tmp[i].find(",")>0):
            val = tmp[i].split(",")
            cache = []
            for j in range(int(len(val))):
                cache.append(int(val[j]))

            output.append(cache)               
            
    if (flag == 0):
        return outputdir
    else:
        return output

def checka(rules, orders, flag):
    ordercnt = int(len(orders))
    ec = 0
    for j in range (ordercnt):
        # How many items after me?
        mcnt = ordercnt - j
        # Run the check for all items except the last one
        for k in range(1, mcnt):   
            active = rules[orders[j+k]]   
            for l in range(int(len(active))):
                if (active[l] == orders[j]):
                    ec = 1
            
    if (ec == 0):
        return orders
    elif (ec > 0 and flag == 1):
        badorders.append(orders)

def fix(rules, orders):
    fixed_job = []
    for index, page in enumerate(orders):
        # try inserting at every position until it fits
        for position in range(len(fixed_job) + 1):
            candidate_job = fixed_job[:position] + [page] + fixed_job[position:]
            if checka(rules, candidate_job,0):
                fixed_job = candidate_job
                break
    return fixed_job      
  
def counter(orders):
    result = 0
    for i in range(int(len(orders))):
        middle = int((len(orders[i])-1)/2)
        result = result + int(orders[i][middle])
    return result
                        

def main():
    countme = []
    raw = read_file()
    rules = read_data(raw, 0)
    orders = read_data(raw, 1)
    for i in range(int(len(orders))):
        tmp = checka(rules, orders[i], 1)
        if(tmp != None):
            countme.append(tmp)
    print("Task 1:", counter(countme))    
    countme.clear()
    for i in range(int(len(badorders))):
        countme.append(fix(rules, badorders[i]))
    print("Task 2:", counter(countme))
main()