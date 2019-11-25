# Jackson J.
# 11/23/19
# This is the driver for the classRacecarDriver
from classRacecarDriver import RacercarDriver
from random import *
rn = randint(1, 3)

first = "Jared"
last = "Jackson"
age = 18
weight = 180
height = 69
trophies = 20
make = "Mclaren"
model = "F1 GTR"
year = 2019
speed = "Fast"

first_racer = RacercarDriver(first, last, age, weight, height, trophies, make, model, year, speed)

first = "T."
last = 'M.'
age = "39"
weight = 150
height = 63
trophies = 10
make = "Tesla"
model = "Roadster"
year = 2018
speed = "Medium"

second_racer = RacercarDriver(first, last, age, weight, height, trophies, make, model, year, speed)

first = "P."
last = 'B.'
age = "58"
weight = 200
height = 73
trophies = 15
make = "Lexus"
model = "LFA"
year = 2017
speed = "Medium"

third_racer = RacercarDriver(first, last, age, weight, height, trophies, make, model, year, speed)

first = ""
last = ''
age = 13
weight = 120
height = 62
trophies = 5
make = "Bicycle"
model = "Bmx"
year = 2017
speed = "Slow"

fourth_racer = RacercarDriver(first, last, age, weight, height, trophies, make, model, year, speed)

input("CLICK HERE, THEN PRESS ENTER")
