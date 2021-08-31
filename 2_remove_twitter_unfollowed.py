import csv
import json
import sqlite3

csvreader = csv.reader(open('data/1_result.csv', newline=''))
csvwriter = csv.writer(open('data/2_result.csv', 'w', newline=''))

followers = set()
t_reader = csv.reader(open('rawdata/followers.csv', newline=''))
for row in t_reader:
    followers.add(row[2])
print('all followers:', len(followers))

result = []

def twitter_followed(username):
    if '@' in username:
        username = username.split('@')[1]
    return username in followers

count = 0
for row in csvreader:
    if not twitter_followed(row[0]):
        continue
    result.append(row)
    count += 1
print(count)

for row in result:
    csvwriter.writerow(row)
