#for i in (range(9,-1,-1)):
#    print(i)

#fave_drinks = ["Wine", "Gin", "Water"]

#for drinks in fave_drinks:
#    print(drinks)


fave_films = ["Dogma", "Lawnmower Man", "Ghostbusters", "The Lion King", "Star Wars"]

fave_films.append("Beauty and the Beast")
fave_films.append("The Room")

for films in fave_films:
    print(films)

def film_check(films):
    if films[2] == "Ghostbusters":
        return("Yay it's Ghostbusters")
    else:
        return("Boo, we want Ghostbusters")

print(film_check(fave_films))

#ACTIVITY 1

def sub_order(top1, top2, top3, top4, top5):
    print("On my sub I want {}, {}, {}, {} and {}".format(top1,top2,top3,top4,top5))

sub_order("ham","cheese","lettuce","tomatoes","cucumber")

#ACTIVITY 2

fave_food = ["Pizza", "Cake", "Cheese"]

fave_food.append("Pie")

print(fave_food)

#ACTIVITY 3

import random

for i in range(6):
    print(random.randint(1,50))
