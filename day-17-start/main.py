class User:
    def __init__(self, id):
        self.id = id
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1



user1 = User("001")

print(user1.id)
