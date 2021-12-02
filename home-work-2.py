''' 2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
   - щось своє :)
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
'''

def valid_ator(user_data=[' ', ' ']):
   def num_cheker(x):
      for i in x:
         if i.isdigit() == True:
            return True
      return False

   class ExceptionLongName(Exception):
      # 3<50
      pass
   class ExceptionLongPassword(Exception):
      #password 8< and 0-9
      pass
   class ExceptionBadPassword(Exception):
      # bad password 12345678
      pass
   try:

      if  not 3 < len(user_data[0]) <= 50:
         raise ExceptionLongName('Error login < 3 or >50')
      if 8 > len(user_data[1]):
         raise ExceptionLongPassword('Error password > 8 char ')
      if num_cheker(user_data[1]) == False:
         raise ExceptionLongPassword('Error password  non type int ')
      if user_data[1] == '12345678':
         raise ExceptionBadPassword('Error your password 12345678 ')       

   except ExceptionLongName as error:
      print(error)
   except ExceptionLongPassword as error:
      print(error)
   except ExceptionBadPassword as error:
      print(error)
   else:
      print('OK')

user_data_login = input('Entar login ')
uaer_data_password = input('Enter password')
valid_ator([user_data_login, uaer_data_password])
