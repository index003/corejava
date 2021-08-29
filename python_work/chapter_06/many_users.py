# 字典中存储字典

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'cuire',
        'location': 'paris'
    }
}

for username, userinfo in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{userinfo['first']} {userinfo['last']}"
    location = userinfo['location']
    print(f"\tFullname: {full_name.title()}")
    print(f"\tLocation: {location.title()}")