startYear = 1953
endYear = 2022

from webpage.models import YearSlide

for i in range(startYear, endYear + 1):
    YearSlide.objects.create(year=i)
