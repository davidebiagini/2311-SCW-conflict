import sys
"""
This script counts the lines in standard input
Input: text from the system
Output: output line numbers
Author: Biagini, Davide
"""
count = 0
for line in sys.stdin:
    count += 1

print(count, "lines in standard input")

