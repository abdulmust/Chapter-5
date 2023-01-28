current_users = ['admin', 'abdullah', 'muadh', 'maryam', 'halima']
new_users = ['admin', 'abdullah', 'kamal', 'jamal', 'mahfuz']
for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user.title()} will need to enter a new username")
    else:
        print("the username is available")