import pyrebase

config = {
    "apiKey": "AIzaSyDOUI-nKfhSTfvYTd8CHyehsbyOE48vGEc",
    "authDomain": "personal-bot-14b45.firebaseapp.com",
    "databaseURL": "https://personal-bot-14b45.firebaseio.com",
    "projectId": "personal-bot-14b45",
    "storageBucket": "personal-bot-14b45.appspot.com",
}

#configures the connection with firebase
firebase = pyrebase.initialize_app(config)
#instance of auth is created
auth = firebase.auth()
#instance of database is created
db = firebase.database()

class Authentication:
        # method created for registration of user
    def create_user_account(self, email, password):
        # method present in auth class is called
        auth.create_user_with_email_and_password(email, password)


        # method created for login user
    def log_user_account(self, email, password):
        # method present in auth class is called
        auth.sign_in_with_email_and_password(email, password)

        # methood created for checking if password
    def check_for_password_lenght(self, password):
        if len(password) >= 7:
            return True
        else:
            return False




