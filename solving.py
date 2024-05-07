'''
อลิสต้องการส่งรหัสบัตรATM ไปให้บ๊อบแต่เพื่อความปลอดภัยจึงได้นำตัวเลขเหล่านั้นมาซ่อนไว้ในประโยคเช่น

HE45L32LO458T6H359ISIS1BO589RNT34ODEVN80AJA

ซึ่งตัวเลขที่ถูกซ่อนอยู่จะถูกนำมาบวกกันเป็น

45+32+458+6+359+1+589+34+80 = 1604

นั้นคือบ๊อบจะสามารถใช้รหัส 1604 ในการกดรหัสบัตร ATM ได้นั้นเอง

เมื่อทราบดังนี้ จงถอดรหัสต่อไปนี้ :

MS2007ET35GUTUB4BASGUME4KHOWPUN596BOXERME7GITHOPEJOKER999HASAUTSO888_WE_ARE_MSET
'''

num = "MS2007ET35GUTUB4BASGUME4KHOWPUN596BOXERME7GITHOPEJOKER999HASAUTSO888_WE_ARE_MSET"
ls = [digit if digit.isdigit() else " " for digit in str(num)]
txt = "".join(ls).split()
print(txt)
op = sum(int(i) for i in txt if i)
print(f"{op:04d}")