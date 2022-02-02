
#.......................Part1-(Algorithm)......................
import random
def gen():
	return [random.randrange(1,9) for i in range(8)]
def eval(lst):
	g = 0 
	for x in lst:
		index = lst.index(x)
		p = index
		while True:
			p = (p + 1) % 8
			if p == index:
				break
			if lst[p] != x + (p - index) and lst[p] != x - (p - index) and lst[p] != x:
				g = g + 1 
	return g
def succ(s):
		i_eval = eval(s)
		max = i_eval
		count = 0
		top = s.copy()
		for j in range(8):
				for r in range(1,9):
						d = s.copy()
						d[j] = r
						if eval(d) > max:
								max = eval(d)
								top = d
								count = count + 1
		s = top
		if max == 56:
				return max,s
		elif count != 0:
				return succ(s)
		else:
				return max , s

initial = gen()
solve = succ(initial)
ans = solve[1]
gaurd = 28 - solve[0]/2 

#.....................Part2-(Chess field)......................
import turtle
def bsq(m):
    m.down()
    m.color("black")
    m.begin_fill()
    for i in range(4):
        m.fd(l)
        m.lt(90)
    m.end_fill()
    m.forward(l)
def wsq(m):
    m.down()
    for i in range(4):
        m.fd(l)
        m.lt(90)
    m.forward(l)
def row_odd():
    col = 1
    while True:
        if col == 5:
            break
        if col % 2 != 0:
            for k in range(2):
                bsq(a)
                wsq(a)
                col = col + 1
        if col % 2 == 0:
            for k in range(2):
                wsq(a)
                bsq(a)
                col = col + 1
def row_even():
    col = 1
    while True:
        if col == 5:
            break
        if col % 2 == 0:
            for k in range(2):
                bsq(a)
                wsq(a)
                col = col + 1
        if col % 2 != 0:
            for k in range(2):
                wsq(a)
                bsq(a)
                col = col + 1
def chess():
    for i in range(4):
        row_odd()
        a.setx(a.pos()[0]-(l*8))
        a.sety(a.pos()[1]+l)
        row_even()
        a.setx(a.pos()[0]-(l*8))
        a.sety(a.pos()[1]+l)

l = 70
a = turtle.Turtle()
a.ht()
b = turtle.Screen()
b.tracer(False)
a.pensize(2)
a.pu()
a.setx(-280)
a.sety(-280)
chess()

#.....................Part3-(Locater)..........................
def setup(order):
	y = 0
	for x in order:
		colomun = order.index(x,y)
		a.up()
		a.setpos(-280 + (colomun * l) + l/2,-280)
		a.lt(90)
		a.fd((x-1)*l + l/2)
		a.down()
		a.color('#008080')
		a.rt(90)
		a.dot(40)
		if (x + colomun) % 2 != 0:
			a.color('black')
			a.dot(20)
		else:
			a.color('white')
			a.dot(20)
		y = y + 1

def exp():
	a.up()
	a.home()
	a.seth(180)
	a.fd(3*l-120)
	a.rt(90)
	a.fd(l * 4 + 7)
	a.down()
	a.color('black')
	a.write(str(int(gaurd*2))+' queens threaten each other!',font=['Arial', 10])
	a.up()
	a.home()
	a.seth(270)
	a.fd(l * 4 + 25)
	a.rt(90)
	a.fd(3*l-120)
	a.lt(180)
	a.write('best answer: '+str(ans),font=['Arial', 10])

setup(ans)
exp()
print(solve[0])
b.update()

input()






