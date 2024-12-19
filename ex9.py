area = int(input())
import math
gallons = math.ceil(area / 350)
#round up the nearest whole gallon
print(f"You will need {gallons} gallons of paint to cover {area} square feet")