# Part 1

entries = []

with open('levels.txt', 'r') as file:
    for line in file:
        string_values = line.split()
        int_values = [int(value) for value in string_values]
        entries.append(int_values)

safe_reports = 0

for report in entries:
    if all(report[i] <= report[i+1] and abs(report[i] - report[i+1]) in {1,2,3} for i in range(len(report) - 1)):
        safe_reports += 1
    elif all(report[i] >= report[i+1] and abs(report[i] - report[i+1]) in {1,2,3} for i in range(len(report) - 1)):
        safe_reports += 1
        
print(safe_reports)

# Part 2

safe_reports_2 = 0

def check_valid_report_removing_entries(report):
    for i in range(len(report)):
        report_copy = report[:i] + report[i+1:]
        if all(report_copy[j] <= report_copy[j+1] and abs(report_copy[j] - report_copy[j+1]) in {1,2,3} for j in range(len(report_copy) - 1)):
            return True
        elif all(report_copy[j] >= report_copy[j+1] and abs(report_copy[j] - report_copy[j+1]) in {1,2,3} for j in range(len(report_copy) - 1)):
            return True

for report in entries:
    if check_valid_report_removing_entries(report):
        safe_reports_2 += 1
        
print(safe_reports_2)