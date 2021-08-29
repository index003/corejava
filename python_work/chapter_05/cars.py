cars = ["bmw", "audi", "toyota", "subaru"]
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

name = 'jack'
if name.upper() == 'jack'.upper():
    print("True")
else:
    print("False")

requested_topping = 'mushroom'
if requested_topping != 'anchovies':
    print("Hello the anchovies!")

answers = 17
if answers != 42:
    print("The answer is not correct,please try again.")

age = 20
if (age > 21) and (age < 19):
    print(f"{age}")
else:
    print("not")

if (age > 21) or (age == 20):
    print(f"{age}")
else:
    print("not")

if (age >= 21) or (age <= 20):
    print(f"{age}")
else:
    print("not")

requested_topping = ['mushroom', 'onions', 'pineapple']
if 'mushroom' in requested_topping:
    print(True)

if 'onions' not in requested_topping:
    print(False)
else:
    print(True)

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"{price}")


requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("not null")
else:
    print("is null")

available_toppings = ['mushroom', 'ovlives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushroom', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("OK")
    else:
        print("Sorry")

