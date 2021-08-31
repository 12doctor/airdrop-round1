import csv
import json
import sqlite3

csvreader = csv.reader(open('data/4_result.csv', newline=''))
csvwriter = csv.writer(open('data/5_result.csv', 'w', newline=''))

result = []

# twitter id
tid_set = set()
# discord id
did_set = set()
# principal id
pid_set = set()

def is_duplicate(row):
    tid = row[0]
    if '@' in tid:
        tid = row[0].split("@")[1]
    if tid in tid_set:
        return True
    did = row[1]
    if did in did_set:
        return True
    if row[2] in pid_set:
        return True

count = 0
for row in csvreader:
    if is_duplicate(row):
        continue
    result.append(row)
    tid = row[0]
    if '@' in tid:
        tid = row[0].split('@')[1]
    tid_set.add(tid)
    did = row[1]
    did_set.add(did)
    pid_set.add(row[2])
    count += 1
print(count)

for row in result:
    csvwriter.writerow(row)
