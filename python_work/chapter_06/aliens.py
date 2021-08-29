# 列表中存储字典

alien_0 = {
    'color': 'green',
    'points': 5
}
alien_1 = {
    'color': 'yellow',
    'points': 10
}
alien_2 = {
    'color': 'red',
    'points': 15
}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

aliens = []

for alien_number in range(30):
    new_alien = {
        'color': 'green',
        'point': 5,
        'speed': 'slow'
    }
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print('....')

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['point'] = 15

for alien in aliens[:5]:
    print(alien)


print('....')

print(f"Total number of aliens:{len(aliens)}")
