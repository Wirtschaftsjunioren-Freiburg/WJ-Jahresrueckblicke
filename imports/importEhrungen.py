# Load csv file with Vorsitzende data into database

import csv
from webpage.models import Honour,YearSlide

with open('../data/Ehrungen.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        vorsitzende = Honour.objects.create(year=YearSlide.objects.get(year=row[0]), person=row[2], honour=row[1])