if __name__ == '__main__':

    users = [
        {
            'first_name': 'Aleksandr',
            'last_name': "Fam",
            'email': 'mm@justcode.kz',
            'age': 12
        }, {
            'first_name': 'Ulan',
            'last_name': "uuu",
            'email': 'hh@justcode.kz',
            'age': 23
        }
    ]


    for i in range(len(users)):
        d = users[i]
        for key, value in d.items():
            print(value)
        print("----------------------")
