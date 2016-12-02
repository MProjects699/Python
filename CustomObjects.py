from operator import attrgetter

class User:

    def __init__(self, x, y):
        self.name = x
        self.user_id = y


        def __repr__(self):
            return self.name+":"+str(self.user_id)

        users = [
            User('Bucky', 43),
            User('Bucky', 43),
            User('Bucky', 43),
            User('Bucky', 43),
        ]

        for user in users:
            print(users)

            print('--------')
            for user in sorted(users, key=attrgetter('name')):
                print(user)

                print('--------')
                for user in sorted(users, key=attrgetter('user_id')):
                    print(user)