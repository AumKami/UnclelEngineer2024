tilecolor = {'red':100,'gold':200,'white':90, 'grey':30}


print('-----ราคากระเบื้อง------')
for c,t in tilecolor.items(): #c เป็น Key
    print('สี: {} ราคา: {}'.format(c,t))

print('-----โปรแกรมคำนวณกระเบื้อง v2 by Uncle---')
try:
    tiles = int(input('คุณต้องการปูกระเบื้องทั้งหมดกี่แผ่น: '))
    row = int(input('1 แถวต้องปูกระเบื้องกี่แผ่น: ')) # 3ชิ้นต่อแถว
    color = input('กระเบื้องสีอะไร? [red/gold/white]: ')
except:
    print('กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น!')
    tiles = int(input('คุณต้องการปูกระเบื้องทั้งหมดกี่แผ่น: '))
    row = int(input('1 แถวต้องปูกระเบื้องกี่แผ่น: ')) # 3ชิ้นต่อแถว
    
total_row = tiles//row
remaining_tiles = tiles % row



buy_more = row - remaining_tiles

print(f'มีกระเบื้องทั้งหมด: {tiles} แผ่น')
print(f'1 แถวปูกระเบื้องได้ {row} แผ่น')
print('----------คำนวณ---------')
print('ปูกระเบื้องได้ {} แถว'.format(total_row))
print('เหลือกระเบื้องที่ยังไม่ได้ปูเต็มแถว {} แผ่น'.format(remaining_tiles))
print('ลูกค้าต้องซื้อกระเบื้องเพิ่ม {} แผ่น'.format(buy_more))
print('ยอดรวมทั้งหมดที่ต้องซื้อกระเบื้องเพิ่ม {} บาท'.format(buy_more * tilecolor[color]))
#ลูกค้าต้องซื้อกระเบื้องเพิ่มกี่แผ่น

print('---------------The End-------------------------')


