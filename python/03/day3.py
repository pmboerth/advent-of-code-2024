# Part 1

import re

with open('multiply.txt', 'r') as file:
    pattern = r"mul\((\d+),(\d+)\)"
    matches = []
    for line in file:
        line_matches = re.findall(pattern, line)
        matches.extend((int(x), int(y)) for x, y in line_matches)

count = 0
for pair in matches:
    count += pair[0] * pair[1]
    
print(count)

# Part 2
with open('multiply.txt', 'r') as file:
    start_pattern = r"do\(\)"
    end_pattern = r'don\'t\(\)'
    collecting = True
    matches = []
    for line in file:
        if collecting and not re.search(line, end_pattern):
            line_matches = re.findall(pattern, line)
            matches.extend((int(x), int(y)) for x, y in line_matches)
        if collecting and re.search(line, end_pattern):
            line_matches = re.findall(pattern, line[:end_pattern])
    
