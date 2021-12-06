'''
6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
'''

def my_range(start_r, finish_r = None, step_r=1):
    if finish_r == None:
        start_r, finish_r = 0, start_r
    if step_r == 0:
        raise ValueError
    if step_r > 0:
        while start_r < finish_r:
            yield start_r
            start_r += step_r
    else:
        while start_r > finish_r:
            yield start_r
            start_r += step_r
        

for item in my_range(10,2,-1):
   print(item)
for item in my_range(10):
   print(item)
for item in my_range(10,20):
   print(item)
for item in my_range(2,10,2):
   print(item)
