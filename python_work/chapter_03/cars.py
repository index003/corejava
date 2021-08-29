cars = ["bmw", "audi", "toyota", "subaru"]
print(f"Here is the original list:\n\t{cars}")
cars.sort()
print(f"Here is the sort list:\n\t{cars}")
cars.sort(reverse=True)
print(f"Here is the sort and reverse list:\n\t{cars}")

cars = ["bmw", "audi", "toyota", "subaru"]
print(f"Here is the original list:\n\t{cars}")
print(f"Here is the sorted list:\n\t{sorted(cars)}")
print(f"Here is the original list:\n\t{cars}")

cars.reverse()
print(f"Here is the reverse list:\n\t{cars}")
cars.reverse()
print(f"Here is the reverse again list:\n\t{cars}")

print(f"The list length is {len(cars)}")

