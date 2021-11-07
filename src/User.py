# in this class we write User code

class User:
    activeUserCount = 0
    allowedUser = ['saha','sara','milad','nazi','iman']
    loggedInUsers = []
    def __init__(self,gotUserName,gotUserFamily):
        if gotUserName not in User.allowedUser:
            raise ValueError(f"{gotUserName} can not login !!")

        self.name = gotUserName
        self.family = gotUserFamily
        User.activeUserCount += 1
        User.loggedInUsers.append(gotUserName)
        print(f"{self.name} logged in")
    def logOut(self):
        print(f"{self.name} has loged out")
        User.activeUserCount -= 1
        User.loggedInUsers.remove(self.name)