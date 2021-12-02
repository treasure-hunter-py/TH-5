def user_data_base(user_login, user_password, silent=False):
    
   class LoginException(Exception):
      pass

   user_list = [['Jotaro', 'YareYare'],
   ['Spidvagon', 'TruWaifu'],
   ['Polnaref', 'SilverCeriot'],
   ['Dio', 'ZAVARDO'],
   ['Muhamed', 'MajishenRed']]
   try:
      if [user_login, user_password] in user_list:
         silent = True
      else:
         if silent == True:
               silent = False
         else:
            print(' ')
            raise LoginException()
   except LoginException:
      print('Error LoginException')
   else:
      return silent

name = input('Enter Login ')
password = input('Enter passvord ')
silent_user = input('True/False ') == 'True'
print(user_data_base(name, password, silent = silent_user))
