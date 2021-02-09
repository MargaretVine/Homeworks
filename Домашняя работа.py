#1
a=2/3+1
b=5/3
print (a, b)
if (a == b):
  print("True")
else:
    print("False")
    if (a > b):
      print("True")
    else: 
      print("False")
    if (a < b):
      print("True")
    else: 
      print("False")
#2
numbers_tuple = (1,2,3,4,5)
numbers_list = [1,2,3,4,5]

# Добавим число в кортеж
numbers_tuple.append(6)
# Здесь появится ошибка, так как нельзя добавлять новые элементы в кортеж (их неизменяемость)
#3
d = {'a': 1, 'b': 2}
d.pop('a')
#Элемент будет удален, потому что словари изменяемы
#4
x=321
print(sum(map(int,str(x))))
#5
N = int(input("Введите число="))
sum = 0 
while N > 0:  
   d = N%10   
   N = N // 10     
sum += d 
print("Сумма всех цифр этого числа =",sum)
#6
s = '+' + input()
print(sum([int(s[i : i + 2]) for i in range(0, len(s), 2)]))
#7
n = int(input ('Введите число: '))
s = input('Введите последовательность: ').split()
for i in range(n)[::-1]:
    print(s[i],end = ' ')
#8
months = {1:'Январь', 2:'Февраль', 3:'Март', 4:'Апрель', 5:'Май', 6:'Июнь', 7:'Июль', 8:'Август', 9:'Сентябрь', 10:'Октябрь', 11:'Ноябрь', 12:'Декабрь'}
def mesyaca(n):
    print(months[n])
 
while True:
    try: mesyaca (int(input('Введите номер месяца: \n')))
    except: break