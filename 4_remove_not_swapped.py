import csv
import json
import sqlite3

csvreader = csv.reader(open('data/3_result.csv', newline=''))
csvwriter = csv.writer(open('data/4_result.csv', 'w', newline=''))

# dswap records
conn = sqlite3.connect('rawdata/history.db')
cursor = conn.execute("SELECT caller FROM history WHERE op=\"swap\"")
callers = cursor.fetchall()
pids = set()
for caller in callers:
    pids.add(caller[0])
print('all principal ids:', len(pids))
result = []

# account ids also removed
def swapped(pid):
    if pid in pids:
        return True
    return False

count = 0
for row in csvreader:
    if not swapped(row[2]):
        continue
    result.append(row)
    count += 1
print(count)

for row in result:
    csvwriter.writerow(row)
