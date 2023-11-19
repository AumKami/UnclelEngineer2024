Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = 'Somsak'
age = 12
age == 12
True
if age == 12:
    print('สามารถเรียนห้องป.6')

    
สามารถเรียนห้องป.6
age = 15
if age != 12:
    print('ต้องเรียนห้องอื่น')

    
ต้องเรียนห้องอื่น
age = 18
if age > 12:
    print('ต้องไปเรียนห้องอื่น')

    
ต้องไปเรียนห้องอื่น
age = 18
if age > 12:
    print('คุณต้องไปถามคุณครูว่าเรียนห้องไหนได้บ้าง')

    
คุณต้องไปถามคุณครูว่าเรียนห้องไหนได้บ้าง
age = 12
if age >= 12:
    print('ห้องนี้รับอายุ 12 ขึ้นไป คุณเข้าได้')

    
ห้องนี้รับอายุ 12 ขึ้นไป คุณเข้าได้
age = 7
if age <12:
    print('ต้องเรียน ป.4 ลงไปเท่านั้น')

    
ต้องเรียน ป.4 ลงไปเท่านั้น
KeyboardInterrupt
garage = ['toyota', 'isuzu','benz']
car = 'toyota'
car in garage
True
if car in garage:
    print('รถคันนี้อยู่ในโรงรถลุง')

    
รถคันนี้อยู่ในโรงรถลุง
mobile = {'loong': '0948929159', 'somsak' : '081111'}
'loong' in mobile #check key in Dict
True
listcheck = mobile.values()#check value in Dict
print(listcheck)
dict_values(['0948929159', '081111'])
'0948929159' in listcheck
True
Audi' == 'audi' #check ตัวอักษรโดยแปลงเป็นพิมพ์เล็ก
SyntaxError: unterminated string literal (detected at line 1)
>>> 'Audi' == 'audi'
False
>>> 'Audi'.lower() == 'audi'
True
>>> #check logic
>>> True and True
True
>>> True and False
False
>>> True or False
True
>>> True or True
True
>>> money = 200
>>> style = 'Yen'
>>> if money >= 200 and style = 'Yen'
SyntaxError: invalid syntax
>>> if money >= 200 and style = 'Yen':
...     
SyntaxError: invalid syntax
>>> if money >= 200 and style == 'Yen':
...     print('สามารถเข้าร้านได้')
... 
...     
สามารถเข้าร้านได้
>>> stylecheck = ['Thai','Japanese','Chinese']
>>> if money >= 200 and style == 'japanese':
...     print('คุณสามารถเข้าร้านได้จ้า')
... 
...     
>>> money = 200
>>> style = 'japanese'
>>> stylecheck = ['Thai','Japanese','Chinese']
>>> if money >= 200 and style == 'japanese':
...     print('คุณสามารถเข้าร้านได้จ้า')
... 
...     
คุณสามารถเข้าร้านได้จ้า
stylecheck = ['japanese','thai','chinese']
if money >= 200 and style in stylecheck:
    print('คุณสามารถเข้าร้านได้จ้า')


money = 200
style = 'japanese'
stylecheck = ['japanese','thai','chinese']
if money >= 200 and style in stylecheck:
    print('คุณสามารถเข้าร้านได้จ้า')

