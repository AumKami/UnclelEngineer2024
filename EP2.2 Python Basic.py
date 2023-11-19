Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = 'Uncle'
>>> name = name.upper
>>> print(name)
<built-in method upper of str object at 0x000002269BC2BD50>
>>> name.upper
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    name.upper
AttributeError: 'builtin_function_or_method' object has no attribute 'upper'
>>> name = 'Uncle'
>>> name = name.upper()
>>> print(name)
UNCLE
>>> number ='1'
>>> number.zfill(5)
'00001'
>>> print('ลุงครับผมชื่อ {} นามสกุล {} อายุ {} ขวบ'.format(name,lastname,age))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print('ลุงครับผมชื่อ {} นามสกุล {} อายุ {} ขวบ'.format(name,lastname,age))
NameError: name 'lastname' is not defined
>>> name = 'สมชาย'
>>> lastname = 'ดีมาก'
>>> age = 10
>>> print('ลุงครับผมชื่อ {} นามสกุล {} อายุ {} ขวบ'.format(name,lastname,age))
ลุงครับผมชื่อ สมชาย นามสกุล ดีมาก อายุ 10 ขวบ
>>> print(f'ลุงครับผมชื่อ {name} นามสกุล {lastname} อายุ {age} ขวบ')
ลุงครับผมชื่อ สมชาย นามสกุล ดีมาก อายุ 10 ขวบ
