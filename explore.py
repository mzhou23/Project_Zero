#Minghao Zhou
import graphicsPlus as gr
import time
import random
def test1():
	win=gr.GraphWin('test window',500,500,False)
	pos=win.getMouse()
	print(pos)
	print(pos.getX(),pos.getY())
	win.close()

def test2():
	win=gr.GraphWin('test window2',500,500,False)
	shapes=[]
	while True:
		click=win.checkMouse()
		if click!=None:
			print(click)
			c=gr.Circle(click,10)
			c.setFill(gr.color_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
			shapes.append(c)
			c.draw(win)
		key = win.checkKey()
		
		if key=='q':
			break
		for item in shapes:
			item.move(random.randint(-5,5),random.randint(-5,5))
		
		time.sleep(0.033)#30 loop per sec
		win.update()
	win.close()
	
if __name__=="__main__":
	test2()