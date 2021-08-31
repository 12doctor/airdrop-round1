import csv
import json
import sqlite3

csvreader = csv.reader(open('data/2_result.csv', newline=''))
csvwriter = csv.writer(open('data/3_result.csv', 'w', newline=''))

# discord members
dis_members = json.load(open('rawdata/members.json'))
members = set()
for mem in dis_members:
    members.add(mem)

result = []

def discord_joined(username):
    return username in members

count = 0
for row in csvreader:
    if not discord_joined(row[1]):
        continue
    result.append(row)
    count += 1
print(count)

for row in result:
    csvwriter.writerow(row)
