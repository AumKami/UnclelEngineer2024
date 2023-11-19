Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def sawasdee ():
    """ฟังก์ชันนี้ใช้สำหรับปริ้นสวัสดี"""
    print('สวัสดีจ้าาา')

dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'sawasdee']
#สามารถดูได้ว่า Program run อะไร

help(sawasdee)#อยากรู้ว่าคำว่าสวัสดีคืออะไร
Help on function sawasdee in module __main__:

sawasdee()
    ฟังก์ชันนี้ใช้สำหรับปริ้นสวัสดี

help(print) #อยากรู้ว่าคำว่าปริ้นคืออะไร
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.

def hello(freind):
    print('Hi, {}'.format(friend))

    
hello('John')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    hello('John')
  File "<pyshell#11>", line 2, in hello
    print('Hi, {}'.format(friend))
NameError: name 'friend' is not defined. Did you mean: 'freind'?
def hello(friend):
    print('Hi, {}'.format(friend))

    
hello('John')
Hi, John
hello('Robert')
Hi, Robert
Hi, Robert
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    Hi, Robert
NameError: name 'Hi' is not defined
def land(width,long):
    cal = width * long
    cal_wa = cal / 4
    print('ที่ดินพื้นนี้กว้าง: {} เมตร ยาว: {} เมตร'.format(width,long))
    print('ที่ดินพื้นนี้พื้นที่: {} ตารางเมตร'.format(cal))
    print('ที่ดินพื้นนี้พื้นที่: {} ตารางวา'.format(cal_wa))

    
land(5,15)
ที่ดินพื้นนี้กว้าง: 5 เมตร ยาว: 15 เมตร
ที่ดินพื้นนี้พื้นที่: 75 ตารางเมตร
ที่ดินพื้นนี้พื้นที่: 18.75 ตารางวา
ที่ดินพื้นนี้พื้นที่: 18.75 ตารางวา
SyntaxError: incomplete input
SyntaxError: incomplete input
SyntaxError: incomplete input

def land(width,long):
    cal = width * long
    cal_wa = cal / 4
    print('ที่ดินพื้นนี้กว้าง: {} เมตร ยาว: {} เมตร'.format(width,long))
    print('ที่ดินพื้นนี้พื้นที่: {} ตารางเมตร'.format(cal))
    print('ที่ดินพื้นนี้พื้นที่: {} ตารางวา'.format(cal_wa))
    return cal_wa

res = land(5,15)
ที่ดินพื้นนี้กว้าง: 5 เมตร ยาว: 15 เมตร
ที่ดินพื้นนี้พื้นที่: 75 ตารางเมตร
ที่ดินพื้นนี้พื้นที่: 18.75 ตารางวา
print(res)
18.75
>>> def land(width,long,price=999888):
...     cal = width * long
...     cal_wa = cal / 4
...     print('ที่ดินพื้นนี้กว้าง: {} เมตร ยาว: {} เมตร'.format(width,long))
...     print('ที่ดินพื้นนี้พื้นที่: {} ตารางเมตร'.format(cal))
...     print('ที่ดินพื้นนี้พื้นที่: {} ตารางวา'.format(cal_wa))
...     return cal_wa * price
... 
>>> res = land(5,15)
ที่ดินพื้นนี้กว้าง: 5 เมตร ยาว: 15 เมตร
ที่ดินพื้นนี้พื้นที่: 75 ตารางเมตร
ที่ดินพื้นนี้พื้นที่: 18.75 ตารางวา
>>> print(res)
18747900.0
>>> def land(width,long,price=999888):
...     cal = width * long
...     cal_wa = cal / 4
...     print('ที่ดินพื้นนี้กว้าง: {} เมตร ยาว: {} เมตร'.format(width,long))
...     print('ที่ดินพื้นนี้พื้นที่: {} ตารางเมตร'.format(cal))
...     print('ที่ดินพื้นนี้พื้นที่: {} ตารางวา'.format(cal_wa))
...     calprice = cal_wa * price
...     return 'ที่ดินผืนนี้ราคา: {:,.2f} บาท'.format(calprice)
... 
>>> res = land(5,15)
ที่ดินพื้นนี้กว้าง: 5 เมตร ยาว: 15 เมตร
ที่ดินพื้นนี้พื้นที่: 75 ตารางเมตร
ที่ดินพื้นนี้พื้นที่: 18.75 ตารางวา
>>> print(res)
ที่ดินผืนนี้ราคา: 18,747,900.00 บาท
>>> land(5,15)
ที่ดินพื้นนี้กว้าง: 5 เมตร ยาว: 15 เมตร
ที่ดินพื้นนี้พื้นที่: 75 ตารางเมตร
ที่ดินพื้นนี้พื้นที่: 18.75 ตารางวา
'ที่ดินผืนนี้ราคา: 18,747,900.00 บาท'
>>> land(5,15,1000000)
ที่ดินพื้นนี้กว้าง: 5 เมตร ยาว: 15 เมตร
ที่ดินพื้นนี้พื้นที่: 75 ตารางเมตร
ที่ดินพื้นนี้พื้นที่: 18.75 ตารางวา
'ที่ดินผืนนี้ราคา: 18,750,000.00 บาท'
