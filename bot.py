import services

# instance of class Authentication is called
auth = services.Authentication()


class Bot:
    email = ''
    password = ''
    #method created for asking user choice
    def ask_auth_mode(self):
        user_choice = input('Do you want login or reister?\n 1 == login , 0 == register')
        if int(user_choice) == 1:
            self.user_input()
            if auth.check_for_password_lenght(self.password):
                self.log_in_user()
            else:
                print('Your password should be greater than 7')
        elif int(user_choice) == 0:
            self.user_input()
            if auth.check_for_password_lenght(self.password):
                self.register_user()
            else:
                print('Your password should be greater than 7')
        else:
            print('plzz choose a valid input')



    #method created for taking user input
    def user_input(self):
        self.email = input('enter your email: ')
        self.password = input('enter your password: ')

     #method created for registration of user
    def register_user(self):
        auth.create_user_account(self.email, self.password)


    # method created  for login user
    def log_in_user(self):
        auth.log_user_account(self.email, self.password)

#instance of class created
bot = Bot()
#called method in the class bot
bot.ask_auth_mode()




