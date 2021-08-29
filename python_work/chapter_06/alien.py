alien_0 = {
    'color': 'green',
    'points': 5
}

print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0['color'] = 'yellow'
print(alien_0)
del(alien_0['points'])
print(alien_0)

alien_1 ={
    'x_position': 0,
    'y_position': 25,
    'speed': 'medium'
}

print(f"Original position: {alien_1['x_position']}")
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 5
elif alien_1['speed'] == 'fast':
    x_increment = 25

alien_1['x_position'] = alien_1['x_position'] + x_increment
print(f"New position: {alien_1['x_position']}")

