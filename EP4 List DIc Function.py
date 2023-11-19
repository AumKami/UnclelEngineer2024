Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
cars = ['toyota','honda','benz']
cars.append('byd')
print(cars)
['toyota', 'honda', 'benz', 'byd']
cars.remove('honda')
print(cars)
['toyota', 'benz', 'byd']
cars.insert(0,'tesla')
print(cars)
['tesla', 'toyota', 'benz', 'byd']
print(cars[1])
toyota
for c in cars:
    print(c)

    
tesla
toyota
benz
byd
print(*cars)
tesla toyota benz byd
for i,c in enumerate(cars):
    print(i,c)

    
0 tesla
1 toyota
2 benz
3 byd
for i,c in enumerate(cars,start=0):
    print('ลำดับ {} {}'.format(i,c))

    
ลำดับ 0 tesla
ลำดับ 1 toyota
ลำดับ 2 benz
ลำดับ 3 byd
for i,c in enumerate(cars,start=1):
    print('ลำดับ {} {}'.format(i,c))

    
ลำดับ 1 tesla
ลำดับ 2 toyota
ลำดับ 3 benz
ลำดับ 4 byd
print(cars)
['tesla', 'toyota', 'benz', 'byd']
for i,c in enumerate(cars,start=1):
    print(i,c)

    
1 tesla
2 toyota
3 benz
4 byd
cars[1]='isuzu'
print(cars)
['tesla', 'isuzu', 'benz', 'byd']
del cars[2]
print(cars)
['tesla', 'isuzu', 'byd']
len(cars)
3
ord('ก')
3585
ord('ข')
3586
ord('ฃ')
3587
chr(3587)
'ฃ'
chr(3588)
'ค'
for in range(10):
    
SyntaxError: invalid syntax
for i in range (10):
    print(chr(3585+i))

    
ก
ข
ฃ
ค
ฅ
ฆ
ง
จ
ฉ
ช
for i in range (3585,3595):
    print(chr(i))

    
ก
ข
ฃ
ค
ฅ
ฆ
ง
จ
ฉ
ช
number = {'1001':'สมชาย','1002':'สมศรี','1003':'สมศักดิ์'}
print(number['1001'])
สมชาย
for n in number:
    print (n)

    
1001
1002
1003
for n in number.items():
    print(n)

    
('1001', 'สมชาย')
('1002', 'สมศรี')
('1003', 'สมศักดิ์')
for n in number.items():
    print(n[0])

    
1001
1002
1003
for n in number.items():
    print(n[1])

    
สมชาย
สมศรี
สมศักดิ์
for n in number.keys():
    print(n)

    
1001
1002
1003
for n in number.values():
    print(n)

    
สมชาย
สมศรี
สมศักดิ์
>>> def hello():
...     print('hello world')
...     print('hello world')
...     print('hello world')
...     print('hello world')
...     print('hello world')
... hello()
SyntaxError: invalid syntax
>>> hello()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    hello()
NameError: name 'hello' is not defined. Did you mean: 'help'?
>>> def hello():
...     print('hello world')
...     print('hello world')
...     print('hello world')
...     print('hello world')
...     print('hello world')
... 
>>> hello()
hello world
hello world
hello world
hello world
hello world
>>> hello(1)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    hello(1)
TypeError: hello() takes 0 positional arguments but 1 was given
>>> 
>>> 
>>> hello(5)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    hello(5)
TypeError: hello() takes 0 positional arguments but 1 was given
