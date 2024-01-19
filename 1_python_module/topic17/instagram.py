class Instagram:
    accounts = [('John', 'qwerty123'), ]

    def sign_in(self, username, password):
        signed_in = False
        for account in self.accounts:
            if account[0] == username:
                print("Username found")
                if account[1] == password:
                    signed_in = True
                    print("You are now signed in")
                else:
                    print("Wrong password!")
        if not signed_in:
            print("Wrong username!")
