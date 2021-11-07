from User import User

print(f"Numbers of Online User : {User.activeUserCount}")
print("--------------------------")

saha = User('saha','arjmand')
print(f"Numbers of Online User : {User.activeUserCount}")
print("--------------------------")

sara = User('sara','rahimi')
print(f"Numbers of Online User : {User.activeUserCount}")
print("--------------------------")

saha.logOut()
print(f"Numbers of Online User : {User.activeUserCount}")
print("--------------------------")

mohammad = User('mohammad','karimi')