''' 3. На основі попередньої функції створити наступний кусок кода:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і 
   надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
'''
user_data_list = [
   ['polnaref','janP12322'],
   ['muhamedAbdul','Mag1shenRead'],
   ['hu','janP12322'],
   ['JotaroKujo','StarPlat1num'],
   ['DioBrando','ZAWARLDO'],
   ['PanakotaFu','purH']]


def valid_ator(user_data=[' ', ' ']):
   status = ' '
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
         raise ExceptionLongPassword('Error password < 8 char ')

      if num_cheker(user_data[1]) == False:
         raise ExceptionLongPassword('Error password non type int ')

      if user_data[1] == '12345678':
         raise ExceptionBadPassword('Error your password 12345678 ')
         

   except ExceptionLongName as error:
      status = error
   except ExceptionLongPassword as error:
      status = error
   except ExceptionBadPassword as error:
      status = error
   else:
      status = 'OK'

   return status

for chek in range(len(user_data_list)): 

   flag = valid_ator([user_data_list[chek][0], user_data_list[chek][1]])



   print(f'Login - {user_data_list[chek][0]}')
   print(f'Password - {user_data_list[chek][1]}')
   print(f'Status: {flag}')
   print('_______________')
