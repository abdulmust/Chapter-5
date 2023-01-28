usernames = []
if usernames:
    for username in usernames:
        print(f"Hello {username.title()}, would you like to see a status report?")
else:
    print("We need to find some users!")