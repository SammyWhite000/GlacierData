import csv
import os
def addToCSV(data):
    with open(os.getcwd()+'/data/LatAndLong.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def extraction(filename):
    data = []
    with open(os.getcwd()+'/data/'+filename, 'r') as f:
        csv_reader = csv.reader(f) 
        for row in csv_reader:
           data.append([row[4], row[5]]) 
    data.pop(0)
    addToCSV(data)

def main():
    filename = 'wgi_glacier_data.csv'
    extraction(filename)

main()
