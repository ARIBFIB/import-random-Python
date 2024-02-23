# random function
import random

display_cards = ["J","K","Q","A",1,2,3,4,5,6,7,8,9]

random_cards_1 = random.sample(display_cards, 1)
print("The First Card is: ", random_cards_1)

random_cards_2 = random.sample(display_cards, 1)
print("The First Card is: ",random_cards_2)
# ---
new_ran = display_cards.random()
print(new_ran)
