from graphics import*
from random import*
from time import*

# I commented out the first two blocks of code for questions one and two since they have loops that go on forever.

#win = GraphWin("My Program", 600, 600)
#x=300
#y=300
#my_point=Point(x,y)
#my_circle = Circle(my_point,50)
#my_circle.setFill("blue")
#my_circle.draw(win)
#key = win.checkKey()
#while key in ["","w","s","a","d"]:
#	if key=="w":
#		y=y-50
#		my_point=Point(x,y)
#		my_circle.undraw()
#		my_circle = Circle(my_point,50)
#		my_circle.setFill("blue")
#		my_circle.draw(win)
#		key = win.checkKey()
#	if key=="s":
#		y=y+50
#		my_point=Point(x,y)
#		my_circle.undraw()
#		my_circle = Circle(my_point,50)
#		my_circle.setFill("blue")
#		my_circle.draw(win)
#		key = win.checkKey()
#	if key=="a":
#		x=x-50
#		my_point=Point(x,y)
#		my_circle.undraw()
#		my_circle = Circle(my_point,50)
#		my_circle.setFill("blue")
#		my_circle.draw(win)
#		key = win.checkKey()
#	if key=="d":
#		x=x+50
#		my_point=Point(x,y)
#		my_circle.undraw()
#		my_circle = Circle(my_point,50)
#		my_circle.setFill("blue")
#		my_circle.draw(win)
#		key = win.checkKey()
#	else:
#		key= win.checkKey()


#win2 = GraphWin("My Program2", 600, 600)
#x=300
#y=300
#my_point=Point(x,y)
#my_circle = Circle(my_point,50)
#my_circle.setFill("blue")
#my_circle.draw(win2)
#key = win2.checkKey()
#while key in ["","w","s","a","d"]:
#	if key=="w":
#		while key in ["","w"]:
#			sleep(1)
#			y=y-50
#			my_point=Point(x,y)
#			my_circle.undraw()
#			my_circle = Circle(my_point,50)
#			my_circle.setFill("blue")
#			my_circle.draw(win2)
#			key = win2.checkKey()
#	if key=="s":
#		while key in ["","s"]:
#			sleep(1)
#			y=y+50
#			my_point=Point(x,y)
#			my_circle.undraw()
#			my_circle = Circle(my_point,50)
#			my_circle.setFill("blue")
#			my_circle.draw(win2)
#			key = win2.checkKey()
#	if key=="a":
#		while key in ["","a"]:
#			sleep(1)
#			x=x-50
#			my_point=Point(x,y)
#			my_circle.undraw()
#			my_circle = Circle(my_point,50)
#			my_circle.setFill("blue")
#			my_circle.draw(win2)
#			key = win2.checkKey()
#	if key=="d":
#		while key in ["","d"]:
#			sleep(1)
#			x=x+50
#			my_point=Point(x,y)
#			my_circle.undraw()
#			my_circle = Circle(my_point,50)
#			my_circle.setFill("blue")
#			my_circle.draw(win2)
#			key = win2.checkKey()
#	else:
#		key= win2.checkKey()
#
win3 = GraphWin("My Program3", 600, 600)
x=300
y=300
my_point=Point(x,y)
my_circle = Circle(my_point,50)
my_circle.setFill("blue")
my_circle.draw(win3)
key = win3.checkKey()
while key in ["","w","s","a","d"] and y<600 and y>0 and x<600 and x>0:
	if key=="w":
		while key in ["","w"] and y<600 and y>0:
			sleep(.25)
			y=y-50
			my_point=Point(x,y)
			my_circle.undraw()
			my_circle = Circle(my_point,50)
			my_circle.setFill("blue")
			my_circle.draw(win3)
			key = win3.checkKey()
	if key=="s":
		while key in ["","s"] and y<600 and y>0:
			sleep(.25)
			y=y+50
			my_point=Point(x,y)
			my_circle.undraw()
			my_circle = Circle(my_point,50)
			my_circle.setFill("blue")
			my_circle.draw(win3)
			key = win3.checkKey()
	if key=="a":
		while key in ["","a"] and x<600 and x>0:
			sleep(.25)
			x=x-50
			my_point=Point(x,y)
			my_circle.undraw()
			my_circle = Circle(my_point,50)
			my_circle.setFill("blue")
			my_circle.draw(win3)
			key = win3.checkKey()
	if key=="d":
		while key in ["","d"] and x<600 and x>0:
			sleep(.25)
			x=x+50
			my_point=Point(x,y)
			my_circle.undraw()
			my_circle = Circle(my_point,50)
			my_circle.setFill("blue")
			my_circle.draw(win3)
			key = win3.checkKey()
	else:
		key= win3.checkKey()
win3.close()

win4 = GraphWin("My Program", 600, 600)
a=Point(300,300)
target=Circle(a,25)
target.setFill("red")
target.draw(win4)
x=450
y=450
my_point=Point(x,y)
my_circle = Circle(my_point,50)
my_circle.setFill("blue")
my_circle.draw(win4)
key = win4.checkKey()
a_1=300
a_2=300
while key in ["","w","s","a","d"] and ((x>a_1+50 or x<a_1-50) or (y>a_2+50 or y<a_2-50)):
	if key=="w":
		sleep(.25)
		y=y-50
		my_point=Point(x,y)
		my_circle.undraw()
		my_circle = Circle(my_point,50)
		my_circle.setFill("blue")
		my_circle.draw(win4)
		key = win4.checkKey()
	if key=="s":
		sleep(.25)
		y=y+50
		my_point=Point(x,y)
		my_circle.undraw()
		my_circle = Circle(my_point,50)
		my_circle.setFill("blue")
		my_circle.draw(win4)
		key = win4.checkKey()
	if key=="a":
		sleep(.25)
		x=x-50
		my_point=Point(x,y)
		my_circle.undraw()
		my_circle = Circle(my_point,50)
		my_circle.setFill("blue")
		my_circle.draw(win4)
		key = win4.checkKey()
	if key=="d":
		sleep(.25)
		x=x+50
		my_point=Point(x,y)
		my_circle.undraw()
		my_circle = Circle(my_point,50)
		my_circle.setFill("blue")
		my_circle.draw(win4)
		key = win4.checkKey()
	key = win4.checkKey()
win4.close()


win5 = GraphWin("My Program", 600, 600)
a=Point(300,300)
target=Circle(a,25)
target.setFill("red")
target.draw(win5)
x=450
y=450
my_point=Point(x,y)
my_circle = Circle(my_point,50)
my_circle.setFill("blue")
my_circle.draw(win5)
key = win5.checkKey()
a_1=300
a_2=300
while key in ["","w","s","a","d"] and ((x>a_1+50 or x<a_1-50) or (y>a_2+50 or y<a_2-50)):	
	c=randint(-25,25)
	d=randint(-25,25)
	a1=300
	a2=300
	while a1>0 and a1<600 and a2>0 and a2<600 and ((x>a_1+50 or x<a_1-50) or (y>a_2+50 or y<a_2-50)):
		key=win5.checkKey()
		if key=="w":
			y=y-50
			my_point=Point(x,y)
			my_circle.undraw()
			my_circle=Circle(my_point, 50)
			my_circle.setFill("blue")
			my_circle.draw(win5)
			key=win5.checkKey()
		if key=="s":
			y=y+50
			my_point=Point(x,y)
			my_circle.undraw()
			my_circle=Circle(my_point, 50)
			my_circle.setFill("blue")
			my_circle.draw(win5)
			key=win5.checkKey()
		if key=="a":
			x=x-50
			my_point=Point(x,y)
			my_circle.undraw()
			my_circle=Circle(my_point, 50)
			my_circle.setFill("blue")
			my_circle.draw(win5)
			key=win5.checkKey()
		if key=="d":
			x=x+50
			my_point=Point(x,y)
			my_circle.undraw()
			my_circle=Circle(my_point, 50)
			my_circle.setFill("blue")
			my_circle.draw(win5)
			key=win5.checkKey()
		sleep(.25)
		a=Point(a1+c,a2+d)
		target.undraw()
		target=Circle(a,25)
		target.setFill("red")
		target.draw(win5)
		a1=a1+c
		a2=a2+d
		a_1=a1
		a_2=a2
		a3=a1
		a4=a2
	while (a1<=0 or a1>=600 or a2<=0 or a2>=600) and (a3!=300 or a4!=300) and ((x>a_1+50 or x<a_1-50) or (y>a_2+50 or y<a_2-50)):
		key=win5.checkKey()
		if key=="w":
			y=y-50
			my_point=Point(x,y)
			my_circle.undraw()
			my_circle=Circle(my_point, 50)
			my_circle.setFill("blue")
			my_circle.draw(win5)
			key=win5.checkKey()
		if key=="s":
			y=y+50
			my_point=Point(x,y)
			my_circle.undraw()
			my_circle=Circle(my_point, 50)
			my_circle.setFill("blue")
			my_circle.draw(win5)
			key=win5.checkKey()
		if key=="a":
			x=x-50
			my_point=Point(x,y)
			my_circle.undraw()
			my_circle=Circle(my_point, 50)
			my_circle.setFill("blue")
			my_circle.draw(win5)
			key=win5.checkKey()
		if key=="d":
			x=x+50
			my_point=Point(x,y)
			my_circle.undraw()
			my_circle=Circle(my_point, 50)
			my_circle.setFill("blue")
			my_circle.draw(win5)
			key=win5.checkKey()
		sleep(.25)
		a=Point(a3-c, a4-d)
		target.undraw()
		target=Circle(a,25)
		target.setFill("red")
		target.draw(win5)
		a3=a3-c
		a4=a4-d
		a_1=a3
		a_2=a4
	while a3==300 and a4==300 and ((x>a_1+50 or x<a_1-50) or (y>a_2+50 or y<a_2-50)):
		a1=300
		a2=300
		a_1=a1
		a_2=a2
		a3=0
	key= win5.checkKey()
win5.close()

def func1():
	win5 = GraphWin("My Program", 600, 600)
	a=Point(300,300)
	target=Circle(a,25)
	target.setFill("red")
	target.draw(win5)
	x=450
	y=450
	my_point=Point(x,y)
	my_circle = Circle(my_point,50)
	my_circle.setFill("blue")
	my_circle.draw(win5)
	key = win5.checkKey()
	a_1=300
	a_2=300
	while key in ["","w","s","a","d"] and ((x>a_1+50 or x<a_1-50) or (y>a_2+50 or y<a_2-50)):	
		c=randint(-25,25)
		d=randint(-25,25)
		a1=300
		a2=300
		while a1>0 and a1<600 and a2>0 and a2<600 and ((x>a_1+50 or x<a_1-50) or (y>a_2+50 or y<a_2-50)):
			key=win5.checkKey()
			if key=="w":
				y=y-50
				my_point=Point(x,y)
				my_circle.undraw()
				my_circle=Circle(my_point, 50)
				my_circle.setFill("blue")
				my_circle.draw(win5)
				key=win5.checkKey()
			if key=="s":
				y=y+50
				my_point=Point(x,y)
				my_circle.undraw()
				my_circle=Circle(my_point, 50)
				my_circle.setFill("blue")
				my_circle.draw(win5)
				key=win5.checkKey()
			if key=="a":
				x=x-50
				my_point=Point(x,y)
				my_circle.undraw()
				my_circle=Circle(my_point, 50)
				my_circle.setFill("blue")
				my_circle.draw(win5)
				key=win5.checkKey()
			if key=="d":
				x=x+50
				my_point=Point(x,y)
				my_circle.undraw()
				my_circle=Circle(my_point, 50)
				my_circle.setFill("blue")
				my_circle.draw(win5)
				key=win5.checkKey()
			sleep(.25)
			a=Point(a1+c,a2+d)
			target.undraw()
			target=Circle(a,25)
			target.setFill("red")
			target.draw(win5)
			a1=a1+c
			a2=a2+d
			a_1=a1
			a_2=a2
			a3=a1
			a4=a2
		while (a1<=0 or a1>=600 or a2<=0 or a2>=600) and (a3!=300 or a4!=300) and ((x>a_1+50 or x<a_1-50) or (y>a_2+50 or y<a_2-50)):
			key=win5.checkKey()
			if key=="w":
				y=y-50
				my_point=Point(x,y)
				my_circle.undraw()
				my_circle=Circle(my_point, 50)
				my_circle.setFill("blue")
				my_circle.draw(win5)
				key=win5.checkKey()
			if key=="s":
				y=y+50
				my_point=Point(x,y)
				my_circle.undraw()
				my_circle=Circle(my_point, 50)
				my_circle.setFill("blue")
				my_circle.draw(win5)
				key=win5.checkKey()
			if key=="a":
				x=x-50
				my_point=Point(x,y)
				my_circle.undraw()
				my_circle=Circle(my_point, 50)
				my_circle.setFill("blue")
				my_circle.draw(win5)
				key=win5.checkKey()
			if key=="d":
				x=x+50
				my_point=Point(x,y)
				my_circle.undraw()
				my_circle=Circle(my_point, 50)
				my_circle.setFill("blue")
				my_circle.draw(win5)
				key=win5.checkKey()
			sleep(.25)
			a=Point(a3-c, a4-d)
			target.undraw()
			target=Circle(a,25)
			target.setFill("red")
			target.draw(win5)
			a3=a3-c
			a4=a4-d
			a_1=a3
			a_2=a4
		while a3==300 and a4==300 and ((x>a_1+50 or x<a_1-50) or (y>a_2+50 or y<a_2-50)):
			a1=300
			a2=300
			a_1=a1
			a_2=a2
			a3=0
		key= win5.checkKey()
	win5.close()

def circles_collide():
	n=0
	while n>-1:
		func1()
		print("You have the following number of points:")
		n=n+1
		print(n)

circles_collide()
	


input("press a key to continue")

