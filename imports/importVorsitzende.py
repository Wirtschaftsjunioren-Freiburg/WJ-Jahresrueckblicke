# Load csv file with Vorsitzende data into database

import csv
from webpage.models import Position,YearSlide

with open('../data/Vorsitzende.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        vorsitzende = Position.objects.create(year=YearSlide.objects.get(year=row[0]), person=row[1], position=row[2], chairman=True)