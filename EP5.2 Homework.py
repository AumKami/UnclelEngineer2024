ResultScore = {'Mr.A':{'score':60}, 
               'Mr.B':{'score':68}, 
               'Mr.C':{'score':75}}
while True:
    print('------กรุณากรอกชื่อนักเรียน-----')
    name = input('ชื่อนักเรียน: ')
    print(f'ชื่อ {name} \n ได้คะแนน: {ResultScore[name]['score']}')
    scoreStu = ResultScore[name]['score']
    if scoreStu > 80:
        print('Grade A')
    elif scoreStu > 70:
        print('Grade B')
    elif scoreStu > 60:
        print('Grade C')
    elif scoreStu > 50:
        print('Grade D')
else:
    print('Grade F')