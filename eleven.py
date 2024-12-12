import os
import math
import copy
import time
import functools

def initializa(raw):
    tmplist =  raw[0].split(" ")
    tmplist = list(map(int, tmplist))
    numcnt = {}
    for x in tmplist:
        numcnt[x] = numcnt.get(x, 0) + 1
    return numcnt

# Cache functions for checking digit count and even/odd status for faster runtime (saves about 25%)
@functools.cache
def get_digits(number):
    if number <= 999999999999997:
        return int(math.log10(number)) + 1
    else:
        return len(str(number))

@functools.cache
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def blinka(blinks, stones):
    for i in range(blinks):
        # Make copy of current working dict as original dict
        origstones = stones.copy()
        for value, count in origstones.items():
            # Ignore if count is 0
            if count == 0:
                continue
            # Remove count of item from the new list                
            stones[value] -= count
            # Add (stones.get(1, 0) - origstones.get(1, 0)) to remember temporary changed count
            # All 0 become 1
            if value == 0:
                # Reset all zeros and add their number to 1 of the new list
                stones[1] = (stones.get(1, 0) - origstones.get(1, 0)) + origstones.get(1, 0) + count
            # All numbers with an even digit count get split
            elif is_even(get_digits(value)):
                # Get changes value
                left = int(value / (10 ** (get_digits(value)/2)))
                right = int(value % (10 ** (get_digits(value)/2)))
                stones[left] = (stones.get(left, 0) - origstones.get(left, 0)) + origstones.get(left, 0) + count
                stones[right] = (stones.get(right, 0) - origstones.get(right, 0)) +origstones.get(right, 0) + count
            # All other numbers get multiplied by 2024
            else:             
                stones[value*2024] = (stones.get(value*2024, 0) - origstones.get(value*2024, 0)) + origstones.get(value*2024, 0) + count

if __name__ == "__main__":
    # Blink settings
    b1 = 25
    b2 = 10000
    file = os.path.dirname(os.path.realpath(__file__))
    file += "\input11"
    with open(file) as inputfile:
        raw = [line.rstrip() for line in inputfile]

    # Task 1
    start = time.time()
    stones = initializa(raw)
    blinka(b1, stones)    
    answer = 0
    for count in stones.values():
        answer += count
    end = time.time()
    print("Task 1 (newer):", answer, "Ran in", (end-start)*1000, "ms")

    # Task 2
    # Reset stones
    start = time.time()
    stones = initializa(raw)
    blinka(b2, stones)
    answer = 0
    for count in stones.values():
        answer += count
    end = time.time()
    print("Task 2 (newer):", answer, "Ran in", (end-start)*1000, "ms")
