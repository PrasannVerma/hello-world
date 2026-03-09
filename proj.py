class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.loggedin=False
        self.menu()

    def menu(self):
        user_input=input("""Welcome. How to proceed?"
                         1. 1 to signup
                         2. 2 to signin
                         3. 3 to write a post
                         4. 4 to msg a friend
                         5. any other key to exit""")
        
        if user_input=="1":
            pass
        elif user_input=='2':
            pass
        elif user_input=='3':
            pass
        elif user_input=='4':
            pass
        else:
            exit()


obj=chatbook()
