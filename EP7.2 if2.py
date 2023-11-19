Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> money = 200
>>> style = 'japanese'
>>> stylecheck = ['japanese','thai','chinese']
>>> if money >= 200 and style in stylecheck:
...     print('คุณสามารถเข้าร้านได้จ้า')
... 
...     
คุณสามารถเข้าร้านได้จ้า
>>> def checkstyle(style,money):
...     stylecheck = ['japanese','thai','chinese']
...     if money >= 200 and style in stylecheck:
...     print('คุณสามารถเข้าร้านได้จ้า')
...     
SyntaxError: expected an indented block after 'if' statement on line 3
>>> def checkstyle(style,money):
...     stylecheck = ['japanese','thai','chinese']
...     if money >= 200 and style in stylecheck:
...         print('คุณสามารถเข้าร้านได้จ้า')
...     elif style not in stylecheck and money >= 300:
...         print('คุณต้องซื้อชุดของเราในราคา 100 บ.ถึงจะเข้าได้')
...     else:
...         print('ขออภัยค่ะ ทางร้านไม่สามารถให้เข้าได้')
... 
...         
>>> 
>>> checkstyle('japanese',400)
คุณสามารถเข้าร้านได้จ้า
>>> checkstyle('thai',100)
ขออภัยค่ะ ทางร้านไม่สามารถให้เข้าได้
>>> checkstyle('western',600)
คุณต้องซื้อชุดของเราในราคา 100 บ.ถึงจะเข้าได้
