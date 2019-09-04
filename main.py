from building import Building
from city import City

eight_hundred_eighth = Building("800 8th Street", 12)
eight_hundred_eighth.purchase("Fred Flintstone")
eight_hundred_eighth.construct()
# print(eight_hundred_eighth)

three_hundred = Building("300 Plus Park Blvd", 6)
three_hundred.purchase("Barney Rubble")
three_hundred.construct()
# print(three_hundred)

five_hundred = Building("500 Interstate Blvd", 3)
five_hundred.purchase("Wilma Flintstone")
five_hundred.construct()
# print(five_hundred)

two_hundred = Building("200 28th Street", 20)
two_hundred.purchase("Betty Rubble")
two_hundred.construct()
# print(two_hundred)

megalopolis = City()
megalopolis.add_building(eight_hundred_eighth)
megalopolis.add_building(three_hundred)
megalopolis.add_building(five_hundred)
megalopolis.add_building(two_hundred)

for building in megalopolis.buildings:
    print(building)

