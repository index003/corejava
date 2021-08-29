players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

for player in players[-3:]:
    print(f"\t{player.title()}")

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('ice cream')
friend_foods.append('cannoli')
print(f"\tMy favorite foods is {my_foods}")
print(f"\n\tMy friend's favorite foods is {friend_foods}")
for my_food in my_foods:
    print(f"\tMy favorite foods is {my_food}")

for friend_food in friend_foods:
    print(f"\n\tMy friend's favorite foods is {friend_food}")

list_temp = ['hello', 'world', 'abc']




