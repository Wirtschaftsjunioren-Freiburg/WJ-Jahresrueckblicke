startYear = 1953
endYear = 2022
from .models import *

for (i in range(startYear, endYear + 1)) {
    YearSlide.objects.create(year=i)
}   

import .importEhrungen
import .importVorsitzende
import .importVorstand