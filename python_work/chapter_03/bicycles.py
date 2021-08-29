bicycles = ["trek", "cannondale", "readline", "specialized"]
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[3].title())
print(bicycles[-1].title())
message = f"My first bicycle was a {bicycles[1].title()}"
print(message)

names = ["amber", "victor", "jack"]
print(names[0].title())
print(names[1].title())
print(names[2].title())
message = f"{names[0].title()}, you are my best friend"
print(message)
message = f"{names[1].title()}, you are my best friend"
print(message)
message = f"{names[2].title()}, you are my best friend"
print(message)

# 列表修改数据
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# 列表最后追加数据
motorcycles.append('add_new_value')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 向列表中插入数据
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 删除列表中的数据
motorcycles.append('add_new_value')
print(motorcycles)
del(motorcycles[-1])
print(motorcycles)

# 删除列表中最后一个数据，并且访问该值
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# 删除列表中指定位置的数据，并且访问该值
popped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle)

# pop() 和del都会将列表中的数据删除
# 如果删除了后不用了，用del
# 如果删除了后还要用，用pop（）

# 删除指定的内容,第一次出现的值
motorcycles.remove('ducati')
print(motorcycles)
