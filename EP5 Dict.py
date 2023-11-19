Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao1 = turtle.Pen()
>>> tao1Dict = {'color':'green','dis':100}
>>> tao1.color(tao1Dict['color'])
>>> tao1.shape('turtle')
>>> def rect(tao_Obj,tao_Dict):
...     for i in range (4):
...         tao_Obj.forward(tao_Dict['dis'])
...         tao_Obj.left(90)
... 
...         
>>> rect(tao1,tao1Dict)
>>> tao2 = turtle.Pen()
>>> tao2Dict = {'color':'green','dis':50}
>>> tao2.color(tao2Dict['color'])
>>> rect(tao2,tao2Dict)
