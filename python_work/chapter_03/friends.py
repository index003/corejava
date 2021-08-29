my_friends = [
    'Rachel Greene',
    'Monica Geller',
    'Joey Tribbiani',
    'Ross Geller',
    'Chandler Bing',
    'Phoebe Buffay'
    ]
print(my_friends)
friends_leave = "Joey Tribbiani"
print(my_friends)
print(f"{friends_leave} was unable to come.")
my_friends[2] = "Amber Zhou"
print(my_friends)
print(f"Hello {my_friends[0]}, welcome to the meeting.")
print(f"Hello {my_friends[1]}, welcome to the meeting.")
print(f"Hello {my_friends[2]}, welcome to the meeting.")
print(f"Hello {my_friends[3]}, welcome to the meeting.")
print(f"Hello {my_friends[4]}, welcome to the meeting.")
print(f"Hello {my_friends[5]}, welcome to the meeting.")
print("I found a bigger table.")

my_friends.insert(0, "Victor Wu")
my_friends.insert(3, "Jack")
my_friends.append("Mike")
print(my_friends)
print("Sorry, only 2 people can be invited to the party.")
popped_friends = my_friends.pop()
print(f"{popped_friends},sorry")
print(my_friends)

popped_friends = my_friends.pop()
print(f"{popped_friends},sorry")
print(my_friends)

popped_friends = my_friends.pop()
print(f"{popped_friends},sorry")
print(my_friends)

print(f"{my_friends[0]}, welcome.")
print(f"{my_friends[1]}, welcome.")

print(my_friends)
del(my_friends[0])
del(my_friends[1])
print(my_friends)
