import sys
import time
from random import randint, seed

from bogoSorter import BogoSorter as bs

if len(sys.argv) == 1 or len(sys.argv) < 5:
    print(
        f"\n   usage: python {sys.argv[0]} [seed elementsCount minVal maxVal].\n\n"
        "Failing to provide all 4 arguments results in the following queries:\n"
    )
    s = int(input("Seed : "))

    n = int(input("Enter number elements to generate : "))
    minVal = int(input("Enter minimum allowed value for all elements : "))
    maxVal = int(input("Enter maximum allowed value for all elements : "))
else:
    s = int(sys.argv[1])
    n = int(sys.argv[2])
    minVal = int(sys.argv[3])
    maxVal = int(sys.argv[4])

seed(s)

a = []

for _ in range(n):
    a.append(randint(minVal, maxVal))

sorter = bs(a)

print("\nList is - ", a)
print("\nSorted list is - ")

startTime = time.time()
sortedlist = sorter.doSort()
print(f"elapsed Time = {time.time() - startTime}")
print(sortedlist)
