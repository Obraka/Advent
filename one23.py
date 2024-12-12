import os
import re

def task_one(raw):
    orders = 0
    for line in raw:
        # remove all non letters
        line = re.sub('\D', '', line) 
        # first and last number
        nums = int(line[0] + line[-1])
        orders += nums
    return orders

def task_two(raw):
    orders = 0
    for line in raw:
        # replace number words (one) with numbers (1)
        line = re.sub("one", "one1one", line)
        line = re.sub("two", "two2two", line)
        line = re.sub("three", "three3three", line)
        line = re.sub("four", "four4four", line)
        line = re.sub("five", "five5five", line)
        line = re.sub("six", "six6six", line)
        line = re.sub("seven", "seven7seven", line)
        line = re.sub("eight", "eight8eight", line)
        line = re.sub("nine", "nine9nine", line)
        # Feed the new line back to task 1
        orders += task_one([line])
    return orders



def main():
    file = os.path.dirname(os.path.realpath(__file__))
    file += "\input123"

    with open(file) as inputfile:
        raw = [line.rstrip() for line in inputfile]
    print("Task 1: ", task_one(raw))
    print("Task 2: ", task_two(raw))
    
    

    

main()