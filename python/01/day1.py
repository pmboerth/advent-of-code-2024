# PART 1

column1 = []
column2 = []

with open('locations.txt', 'r') as file:
    for line in file:
        entry1, entry2 = line.split()
        column1.append(int(entry1))
        column2.append(int(entry2))
        
column1.sort()
column2.sort()

difference = []
for i in range(len(column1)):
    value = abs(column1[i] - column2[i])
    difference.append(value)

total = 0
for num in difference:
    total += num
    
print(total)
    
# PART 2

total = 0
for num in column1:
    frequency = 0
    for value in column2:
        if num == value:
            frequency += 1
    total += num * frequency

print(total)