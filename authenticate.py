import pyrebase

config ={
   'apiKey': "AIzaSyC4hXZTTcsVoM829yGRGE8-9Nk2XZxXvAg",
  'authDomain': "ai-project-dd46a.firebaseapp.com",
  'projectId': "ai-project-dd46a",
  'storageBucket': "ai-project-dd46a.appspot.com",
  'messagingSenderId': "147560092840",
  'appId': "1:147560092840:web:9c7fb702122a90ea71de9d",
  'measurementId': "G-0BF99VWE5E",
  'databaseURL':"" 
}

firebase =pyrebase.initialize_app(config)
auth = firebase.auth()

email = 'test@gmail.com'
password = '123456'

# user = auth.create_user_with_email_and_password(email,password)
# print(user)


# info = auth.get_account_info(user['idToken'])
# print(info)

# auth.send_email_verification(user['idToken'])
# auth.send_password_reset_email(email)