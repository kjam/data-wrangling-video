from __future__ import print_function
import csv
import pandas as pd


my_reader = csv.DictReader(open('data/eu_revolving_loans.csv', 'r'))

for line in my_reader:
    print(line)


df = pd.read_csv('data/eu_revolving_loans.csv', header=1)

print(df)
