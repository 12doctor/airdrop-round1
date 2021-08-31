import csv
import json
import sqlite3

csvreader = csv.reader(open('rawdata/airdrop1.csv', newline=''))
csvwriter = csv.writer(open('data/1_result.csv', 'w', newline=''))

def is_eth_addr(addr):
    # has to be principal id
    if len(addr) < 63:
        return True
    return False

count = 0
result = []
for row in csvreader:
    if is_eth_addr(row[2]):
        continue
    result.append(row)
    count += 1
print(count)

for row in result:
    csvwriter.writerow(row)
