# sstart with users that need to be verified
# an empty list to hold confirmed users

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
 #verify each useer until there are no more unconfirmed users
 #move each verified user into the list of cnfirmed users

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verified user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users

print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


