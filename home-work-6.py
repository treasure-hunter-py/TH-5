'''
6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
'''

def my_range(start_r, finish_r, step_r=1):
    while start_r < finish_r:
        yield start_r
        start_r += step_r


for item in my_range(0, 10, 2):
   print(item)
