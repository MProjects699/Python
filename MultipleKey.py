from operator import itemgetter

users = [
    {'fname':'Bucky', 'lname':'Roberts'},
    {'fname': 'Bucky', 'lname': 'Roberts'},
    {'fname': 'Bucky', 'lname': 'Roberts'},
    {'fname': 'Bucky', 'lname': 'Roberts'},
    {'fname': 'Bucky', 'lname': 'Roberts'},
]

for x in sorted(users, key=itemgetter('fname')):
    print(x)

    print('-----------')
    for x in sorted(users, key=itemgetter('fname', 'lname')):
        print(x)