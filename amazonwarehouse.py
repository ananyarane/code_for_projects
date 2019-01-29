
import random
import string
import threading

def make_inventory(i_dict):
	items = []
	for k,v in i_dict.items():
		for i in range(v):
			items.append(k) 
	for i in range(25046):
		items.append(' ')
	return items
	

def warehouse_arrange(items,m,n):
	b=[]
	W= [[b for j in range(n)] for i in range(m)]
	for i in range(m):
		for j in range(n):
			b=[]
			for k in range(10):
				x = random.choice(items)
				ind = items.index(x)
				b.append(x)
				items.pop(ind)
			W[i][j] = b

	'''for i in range(m):
		for j in range(n):
			print(W[i][j],end= ' ')
		print(end = "\n")'''

	return W

def create_order():

	order=[]
	for i in range(10):
		x = random.choice(string.ascii_uppercase)
		order.append(x)
		#items.pop(ind)

	print(order)
	return order

def get_next_item(order,i):
	current_item = order[i]
	ind = order.index(current_item)

	return current_item

def get_route(W,current_item,picker_loc,path,speed,aisle_width):
	print("speed: "+str(speed))
	available = []
	if current_item >= 'A' and current_item <= 'H':
		time = 5
	elif current_item >= 'I' and current_item <= 'P':
		time = 10
	else:
		time = 12
	a = []
	x = picker_loc[0]
	y = picker_loc[1]
	for j in range(100):
		for k in range(100):
			if current_item in W[j][k]:
				a.append(j)
				a.append(k)
			if a:
				available.append(a)
			a = []

	if available:
		#print("time for size"+str(time))
		a = available[0]
		x1 = a[0]
		y1 = a[1]
		shortestdist = abs(x1-x) + aisle_width * abs(y1-y)
		dist = 0
		found =[]
		new_picker_location =[]
		l = len(available)
		searchtime = 0
		traveltime = 0
		for i in range(l):
			a = available[i]
			x1 = a[0]
			y1 = a[1]
			dist = abs(x1-x) + aisle_width * abs(y1-y)
			if dist <= shortestdist :
				m = available[i]
				shortestdist = dist
				traveltime = shortestdist/speed
				found = W[x1][y1]
				#print(found)
				for l in range(len(found)):
					if found[l] == current_item:
						found[l] = ' '
						if i >= 0 and i <= 2:
							searchtime = 5
						elif i >= 3 and i <= 5:
							searchtime =  3
						else:
							searchtime =  10
						break
		

		time = time + searchtime + traveltime

		#print(m)
		#print("travel"+str(traveltime))
		#print("search"+str(searchtime))
		#print("n"+str(new_picker_location))
		print("travel time: "+str(traveltime))
		print(shortestdist)
		return m,W,time

	else:
		m = picker_loc
		time = 100
		return m, W, time
	
	

def runorder(order,updated_warehouse,picker_loc,path,speed,aisle_width):
	finaltime = 0
	fatigue = 0.75
	for i in range(len(order)):
		current_item = get_next_item(order,i)
		if i%3 == 0:
			speed = speed - fatigue
		#print(speed)
		#print(current_item)
		picker_loc,updated_warehouse,time = get_route(updated_warehouse,current_item,picker_loc,path,speed,aisle_width)
		#print("after"+str(picker_loc))
		finaltime = finaltime + time
		path.append(picker_loc)

	print(finaltime)
	print(path)

def main():
	i_dict = {'A': 6610,'B':8635,'C':2356,'D':1265,'E':5634,'F':546,'G':19034,'H':10,'I':32,'J':422,'K':2712,'L':5678,'M':123,'N':76,'O':87,\
	'P':768,'Q':56,'R':30,'S':765,'T':164,'U':15,'V':671,'W':876,'X':623,'Y':4523,'Z':16543}
	m = 100
	n = 100

	picker_loc1 = [0,random.randint(0,100)]
	print(picker_loc1)
	picker_loc2 = [0,random.randint(0,100)]
	print(picker_loc2)

	#picker_loc1 = [0,0]
	#picker_loc2 = [0,0]
	items1 = make_inventory(i_dict)
	items2 = items1[::]
	items3 = items1[0:74927]
	W = warehouse_arrange(items2,m,n)
	path1 = []
	path2 = []
	updated_warehouse = W
	aisle_width = 8
	speed = 5


	#order1 = create_order()
	order2 = create_order()
	#t1 = threading.Thread(target = runorder, args = (order1,updated_warehouse,picker_loc1,path1,speed,aisle_width,))
	t2 = threading.Thread(target = runorder, args = (order2,updated_warehouse,picker_loc2,path2,speed,aisle_width,))

	#t1.start()
	t2.start()

	#t1.join()
	t2.join()



if __name__ == '__main__':
	main()