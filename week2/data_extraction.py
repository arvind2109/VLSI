import re
fileread="fast.lib"
f=0
area=[]
cell=[]
pin=[]
pin_temp=[]
with open(fileread,"r") as readfile:
	file_con=readfile.read()
for line in file_con.split("\n"):
		cell_m=re.match("cell ((.*)) {",line)
		area_m=re.match("  area : (.*);",line)
		pin_m=re.match("  pin((.*))  {",line)
		if match:
			if f==1:
				pin.append(pin_temp)
				pin_temp=[]
			cell.append(cell_m.group(1))
		elif match1:
			area.append(area_m.group(1))
		elif match2:
			pin_temp.append(pin_m.group(1))
			f=1
pin.append(pin_temp)
for i in range(len(cell)):
	print(cell[i],area[i],pin[i])
