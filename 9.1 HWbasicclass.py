class Student:
    #Attribute
    school_nm = 'Turtle School'

    #Constructor
    def __init__(self,name,age,subject,score):
        self.name = name
        self.age = age
        self.subject = subject
        self.score = score

    # Method

    def calgrade(self):
        if self.score > 80:
            print('Grade A')
        elif self.score  > 70:
            print('Grade B')
        elif self.score  > 60:
            print('Grade C')
        elif self.score  > 50:
            print('Grade D')
        else:
            print('Grade F')

    def display_info(self):
        print(f'ชื่อนร.: {self.name}')
        print(f'อายุ: {self.age}')
        print(f'เกรด: {self.score}')
        print(f'วิชา: {self.subject}')

name01 = Student('Jazz',15,'Physic',80)
name01.display_info()
name01.calgrade()


