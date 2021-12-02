''' 1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
   Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
   Логіка наступна:
       якщо введено коректну пару ім'я/пароль - вертається <True>;
       якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, інакше (<silent> == <False>) - породжується виключення LoginException '''

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
