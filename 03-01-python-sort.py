import csv

with open('kadai.csv','rt') as input_csv:
    input = csv.reader(input_csv)
    for content in input:
        for i in content:
            print(i+' ',end='')
        print()
