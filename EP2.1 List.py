Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Pen()
>>> type(tao)
<class 'turtle.Turtle'>
>>> tao.shape('turtle')
>>> tao.color('red')
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.clear()
>>> 
>>> for i in range (4):
...     tao.forward(100)
...     tao.left(90)
... 
...     

>>> for i in range (8):
...      tao.forward(100)
...      tao.left(45)
... 
...      
>>> tao.clear()
>>> tao.reset()
>>> 
>>> for i in range (8):
...      tao.forward(100)
...      tao.left(45)
... 
...      
>>> for i in range (8):
...      tao.forward(100)
...      tao.left(45)

     
tao.up()
tao.goto(30,30)
tao.down()

for i in range (4):
    tao.forward(50)
    tao.left(90)

    
tao.list = []
taolist = []
tao1 = turtle.Pen()
tao2 = turtle.Pen()
taolist.append(tao)
taolist.append(tao1)
taolist.append(tao2)
taolist[0].forward(200)
taolist[1].backward(200)
taolist[2].color('Red')
taolist[2].left(90)
taolist[2].forward(200)


for t in taolist:
    for i in range (4):
        t.forward(50)
        t.left(90)

        

