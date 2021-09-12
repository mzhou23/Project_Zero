#Minghao Zhou
#lab 152
#Oct 30
import graphicsPlus as gr
import time
import random
import math
class Thing:#parent class
	def __init__(self,win):
		'''The init method takes self and win as parameters and has no return value. it would create a Thing object'''
		self.type=""
		self.mass=0
		self.elasticity=1.01
		self.position=[0,0]
		self.velocity=[0,0]
		self.acceleration=[0,0]
		self.win=win
		self.scale=10
		self.vis=[]
		self.color='black'
		self.drawn=False
	def draw(self):
		'''The draw function takes self as function and has no return function, it would draw the item in the vis list in the window'''
		for item in self.vis:
			item.draw(self.win)
		self.drawn=True
	def undraw(self):
		'''The function takes self as the only parameter and has no return value, it would undraw the graph and update self.drawn'''
		for item in self.vis:
			item.undraw()
		self.drawn=False
	'''setter and getter method to set or get field value of the object'''
	def getPosition(self): # returns a 2-element tuple with the x, y position.
		return self.position[:]
	def getVelocity(self): # returns a 2-element tuple with the x and y velocities.
		return self.velocity[:]
	def getMass(self): # Returns the mass of the object as a scalar value
		return self.mass
	def getAcceleration(self): # returns a 2-element tuple with the x and y acceleration values.
		return self.acceleration[:]
	def getColor(self):
		return self.color
	def getElasticity(self):
		return self.elasticity
	def setVelocity(self, vx, vy): # vx and vy are the new x and y velocities
		self.velocity[0]=vx
		self.velocity[1]=vy
	def setMass(self, m): # m is the new mass of the object
		self.mass=m
	def getType(self):
		return self.type
	def setAcceleration(self, ax, ay): # ax and ay are new x and y accelerations.
		self.acceleration[0]=ax
		self.acceleration[1]=ay
	def setElasticity(self,newE):
		self.elasticity=newE
	def setPosition(self,px,py):
		'''The setPosition function takes self newX coordinates and new Y cooridinates to update self.position and move the graph in self.vis. It has no return value'''
		dx=px-self.position[0]
		dy=py-self.position[1]
		self.position[0]=px
		self.position[1]=py
		dx=dx*self.scale
		dy=-dy*self.scale
		for item in self.vis:#move the graph in self.vis to new position
			item.move(dx,dy)
	def setColor(self,c):
		'''setColor function takes self and c as parameters and have no return value, which would change the color of the graph in self.vis according to rgb rules.'''
		if c !=None:
			self.color=c
			for i in self.vis:
				i.setFill(c)
		
			
	def update(self,dt):
		'''The update function simulate the motion of the ball, it takes self and dt as parameters and has no return value. dt is the simulation time for calling the function 1 time'''
		x_old=self.position[0]
		y_old=self.position[1]
		x_new=self.position[0]+self.velocity[0]*dt+0.5*self.acceleration[0]*dt**2# update the x position using x_new = x_old + x_vel*dt + 0.5*x_acc * dt*dt
		y_new=self.position[1]+self.velocity[1]*dt+0.5*self.acceleration[1]*dt**2# update the y position using y_new = y_old + y_vel*dt + 0.5*y_acc * dt*dt 

		dx=(x_new-x_old)*self.scale# assign to dx the x velocity times dt times the scale factor (self.scale)
		dy=-(y_new-y_old)*self.scale# assign to dy the negative of the y velocity times dt times the scale factor (self.scale)
		self.position[0]=x_new
		self.position[1]=y_new
		for item in self.vis:# for each item in self.vis
			item.move(dx,dy)# call the move method of the graphics object with dx and dy as arguments..

		self.velocity[0]=self.velocity[0]+self.acceleration[0]*dt# update the x velocity by adding the acceleration times dt to its old value
		self.velocity[1]=self.velocity[1]+self.acceleration[1]*dt
	def setType(self,t):
		self.type=t
class Ball(Thing):
	def __init__(self,win,r=2):
		'''init method of Ball class, which is used to create ball object. It taks self, win , and defult value r=2 as parameters, and has no return values'''
		Thing.__init__(self,win)
		self.type='ball'
		self.radius=r
		self.refresh()
		#self.setColor()
	def refresh(self):
		'''Refresh method is used to change the self.vis after changing the value of self's field value. It takes self as parameters and has no return value'''
		drawn=self.drawn
		if drawn:
			self.undraw()
		self.vis=[gr.Circle( gr.Point(self.position[0]*self.scale, self.win.getHeight()-self.position[1]*self.scale), self.radius * self.scale )]
		if drawn:
			self.draw()
	'''setter and getter method to set or get field value of the object'''
	def getRadius(self):
		return self.radius
	def setRadius(self,r):
		self.radius=r
		self.refresh()
class TwoCircle(Ball):#child class of Ball class
	
	def __init__(self,win,r1=2,r2=1):
		'''The init method takes self, win, default value r1=2, r2=1 as parameters and have no return value. It would create TwoCircle objects which are the child object of Ball class. R1 is the radius for bigger circle, and r2 is the radius for smaller circle.'''
		Ball.__init__(self,win,r1)
		self.smallRadius=r2
		self.refresh()
		
	def refresh(self):
		'''Refresh method is used to change the self.vis after changing the value of self's field value. It takes self as parameters and has no return value'''
		drawn=self.drawn
		if drawn:
			self.undraw()
		self.vis=[gr.Circle( gr.Point(self.position[0]*self.scale, self.win.getHeight()-self.position[1]*self.scale), self.radius * self.scale ),
		gr.Circle(gr.Point(self.position[0]*self.scale, self.win.getHeight()-self.position[1]*self.scale), 1 * self.scale )]
		if drawn:
			self.draw()
	def setColor(self,color1,color2):
		'''setColor method would take self, color1, color2 as parameters and has no return value. It would set Color1 to the bigger circle and set color2 to smaller circle'''
		self.vis[0].setFill(color1)
		self.vis[1].setFill(color2)
class Block(Thing):
	def __init__(self,win,x0=0,y0=0,width=3,height=2,color=None):
		'''init function takes self, win ,dx, dy, color as parameters and has no return value, it would create a block object.
		dx is the length of the rectangle, dy is the height. '''
		Thing.__init__(self,win)
		self.type='block'
		self.position=[x0,y0]
		self.dx=width
		self.dy=height
		self.color=color
		self.reshape()
	def reshape(self):
		'''Reshape method is used to change the self.vis after changing the value of self's field value. It takes self as parameters and has no return value'''
		drawn=self.drawn
		if drawn:
			self.undraw()
		self.vis=[gr.Rectangle(gr.Point(self.scale*(self.position[0]+1/2*self.dx),self.win.getHeight()-self.scale*(self.position[1]+1/2*self.dy)),
		gr.Point(self.scale*(self.position[0]-1/2*self.dx),self.win.getHeight()-self.scale*(self.position[1]-1/2*self.dy)))]
		if drawn:
			self.draw()
	
	'''setter and getter method to set or get field value of the object'''
	def getWidth(self):
		return self.dx
	def getHeight(self):
		return self.dy
	def setWidth(self,x):
		self.dx=x
		self.reshape()
	def setHeight(self,y):
		self.dy=y
		self.reshape()
class Pig(Thing):#child class of Thing
	def __init__(self,win,dx=5,dy=4,color=(255,192,203)):
		'''The init method takes self,win,dx,dy,color as parameters and has no return value. It is used to create pig object. 
		dx is the length of the pig, dy is the height of the pig. The default value of color is pink.'''
		Thing.__init__(self,win)
		self.dx=dx
		self.dy=dy
		self.color=color
		self.type='pig'
		self.createPig()
		self.setColor(color)
	def createPig(self):
		'''createPig method is used to change the self.vis after changing the value of self's field value. It takes self as parameters and has no return value'''
		drawn=self.drawn
		if drawn:
			self.undraw()
		#head--a big oval
		head=gr.Oval(gr.Point(self.scale*(self.position[0]+1/2*self.dx),self.win.getHeight()-self.scale*(self.position[1]+1/2*self.dy)),
		gr.Point(self.scale*(self.position[0]-1/2*self.dx),self.win.getHeight()-self.scale*(self.position[1]-1/2*self.dy)))
		#nose-a smaller oval
		nose=gr.Oval(gr.Point(self.scale*(self.position[0]+1/5*self.dx),self.win.getHeight()-self.scale*(self.position[1]+1/6*self.dy)),
		gr.Point(self.scale*(self.position[0]-1/5*self.dx),self.win.getHeight()-self.scale*(self.position[1]-1/6*self.dy)))
		#eye1
		eye1=gr.Line(gr.Point(self.scale*(self.position[0]-3/10*self.dx),self.win.getHeight()-self.scale*(self.position[1]+1/3*self.dy)),
		gr.Point(self.scale*(self.position[0]-1/10*self.dx),self.win.getHeight()-self.scale*(self.position[1]+1/3*self.dy)))
		#eye2
		eye2=gr.Line(gr.Point(self.scale*(self.position[0]+1/10*self.dx),self.win.getHeight()-self.scale*(self.position[1]+1/3*self.dy)),
		gr.Point(self.scale*(self.position[0]+3/10*self.dx),self.win.getHeight()-self.scale*(self.position[1]+1/3*self.dy)))
		#nostril1
		nostril1=gr.Circle(gr.Point(self.scale*(self.position[0]-1/10*self.dx),self.win.getHeight()-self.scale*self.position[1]),0.1)
		#nostril2
		nostril2=gr.Circle(gr.Point(self.scale*(self.position[0]+1/10*self.dx),self.win.getHeight()-self.scale*self.position[1]),0.1)
		
		self.vis=[head,nose,eye1,eye2,nostril1,nostril2]
		if drawn:
			self.draw()
	def setColor(self,c):
		'''setColor method takes self and c as parameters, it would change the nose part in self.vis to pink.'''
		if c !=None:
			self.color=c
			i=self.vis[1]
			i.setFill(gr.color_rgb(c[0],c[1],c[2]))
	'''setter and getter method to set or get field value of the object'''	
	def getWidth(self):
		return self.dx
	def getHeight(self):
		return self.dy

	
		
class RotatingBlock(Thing):
	def __init__(self,win,x0,y0,width,height,Ax=None,Ay=None):
		Thing.__init__(self,win)
		self.type='rotating block'
		
		self.position=[x0,y0]
		self.width=width
		self.height=height
		if Ax!=None and Ay!= None:

			self.anchor=[Ax,Ay]
		else:
			self.anchor=[x0,y0]
		self.rvel=0.0
		self.win=win
		self.angle=0.0
		self.scale=10
		self.vis=[]
		self.drawn=False
		self.points=[[-width/2,-height/2],[-width/2,height/2],[width/2,height/2],[width/2,-height/2]]
	def render(self):
		'''The render functio only takes self as parameter, and has no return value. it would change the self.vis using the corner points after rotation'''
		theta=self.angle/180.0*math.pi# assign to theta the result of converting self.angle from degrees to radians
		cth=math.cos(theta)# assign to cth the cosine of theta
		sth=math.sin(theta)# assign to sth the sine of theta
		pts=[]# assign to pts the empty list
	
		for vertex in self.points:
			# for each vertex in self.points
			x=vertex[0]+self.position[0]-self.anchor[0]
			y=vertex[1]+self.position[1]-self.anchor[1]# (2 lines of code): assign to x and y the result of adding the vertex to self.pos and subtracting self.anchor

			xt=x * cth - y * sth# assign to xt the calculation x * cos(Theta) - y * sin(Theta) using your precomputed cos/sin values above
			yt=x*sth+y*cth# assign to yt the calculation x * sin(Theta) + y * cos(Theta)
			x=self.anchor[0]+xt
			y=self.anchor[1]+yt
			# (2 lines of code): assign to x and y the result of adding xt and yt to self.anchor
			
			pts.append(gr.Point(self.scale*x,self.win.getHeight() - self.scale*y))# append to pts a Point object with coordinates (self.scale * x, self.win.getHeight() - self.scale*y)
			#print(pts)
		self.vis=[gr.Polygon(pts[0],pts[1],pts[2],pts[3])]# assign to self.vis a list with a Zelle graphics polygon object using the Point objects in pts
	def refresh(self):
		'''Refresh method takes self as parameters, and has no return value. refresh method is used to change the visualized scene of the object after rotation'''
		if self.drawn:
			self.undraw()
		self.drawn=True
		self.render()
		if self.drawn:
			self.draw()
	
	'''getter and setter method, which is used to change the field of the object or return the value of a certain field'''
	def setAngle(self,a):
		self.angle=a
		self.refresh()
	def getAngle(self):
		return self.angle
	def rotate(self,p):
		self.angle+=p
		self.refresh()
	def setAnchor(self,p1,p2):
		self.anchor[0]=p1
		self.anchor[1]=p2
	def getPoints(self):
		return self.points[:]
	
	def setRotVelocity(self,a):
		self.rvel=a
	def getAnchor(self):
		return self.anchor[:]
	def getRotVelocity(self):
		return self.rvel
	
	
	def update(self,dt):
		'''the update method takes self and dt as parameters, it has no return value. This function is used to update the movement of rotating object when knowing the rotation speed and time'''
		da=self.rvel*dt
		if da!=0:
			self.rotate(da)
		Thing.update(self,dt)

class MatchMan(Thing):
	def __init__(self,win,r=4,weapon=0,p=0):
		Thing.__init__(self,win)
		self.type='ball'
		self.radius=r
		self.player=p
		self.weapon=weapon
		self.createMan()
		
		#self.setColor()
	def createMan(self):
		'''createPig method is used to change the self.vis after changing the value of self's field value. It takes self as parameters and has no return value'''
		drawn=self.drawn
		if drawn:
			self.undraw()
		x=self.position[0]
		y=self.position[1]
		r=self.radius
		s=self.scale
		h=self.win.getHeight()
		p=self.player
		if p==0:
			head=gr.Circle(gr.Point(x*s,h-(y+0.75*r)*s),0.25*r*s)
			body=gr.Line(gr.Point(x*s,h-s*(y+0.5*r)),gr.Point(x*s,h-(y-0.5*r)*s))
			leg1=gr.Line(gr.Point(s*(x-0.25*r),h-s*(y-r)),gr.Point(x*s,h-(y-0.5*r)*s))
			leg2=gr.Line(gr.Point(s*(x+0.25*r),h-s*(y-r)),gr.Point(x*s,h-(y-0.5*r)*s))
			arm=gr.Line(gr.Point(x*s,h-s*y),gr.Point((x+0.5*r)*s,h-s*y))
			if self.weapon==0:
				weapon1=gr.Rectangle(gr.Point((x+0.5*r)*s,h-s*(y+0.25*r)),gr.Point((x+0.6*r)*s,h-s*y))
				weapon2=gr.Rectangle(gr.Point((x+0.5*r)*s,h-s*(y+0.25*r)),gr.Point((x+r)*s,h-s*(y+0.15*r)))
				self.vis=[head,body,leg1,leg2,arm,weapon1,weapon2]
			if self.weapon==1:
				weapon1=gr.Polygon(gr.Point(s*(x+0.5*r),h-s*y),gr.Point(s*(x+0.6*r),h-s*y),gr.Point(s*(x+0.6*r+3/16*r),h-s*(y+0.75*r)),gr.Point(s*(x+0.8*r),h-s*(y+r)),gr.Point(s*(x+0.5*r+3/16*r),h-s*(y+0.75*r)))
				weapon2=gr.Rectangle(gr.Point(s*(x+0.45*r),h-s*(y+0.2*r)),gr.Point(s*(x+0.75*r),h-s*(y+0.3*r)))
				self.vis=[head,body,leg1,leg2,arm,weapon1,weapon2]
		elif p==1:
			head=gr.Circle(gr.Point(x*s,h-(y+0.75*r)*s),0.25*r*s)
			body=gr.Line(gr.Point(x*s,h-s*(y+0.5*r)),gr.Point(x*s,h-(y-0.5*r)*s))
			leg1=gr.Line(gr.Point(s*(x-0.25*r),h-s*(y-r)),gr.Point(x*s,h-(y-0.5*r)*s))
			leg2=gr.Line(gr.Point(s*(x+0.25*r),h-s*(y-r)),gr.Point(x*s,h-(y-0.5*r)*s))
			arm=gr.Line(gr.Point(x*s,h-s*y),gr.Point((x-0.5*r)*s,h-s*y))
			weapon1=gr.Rectangle(gr.Point((x-0.5*r)*s,h-s*(y+0.25*r)),gr.Point((x-0.6*r)*s,h-s*y))
			weapon2=gr.Rectangle(gr.Point((x-0.5*r)*s,h-s*(y+0.25*r)),gr.Point((x-r)*s,h-s*(y+0.15*r)))
			self.vis=[head,body,leg1,leg2,arm,weapon1,weapon2]
		if drawn:
			self.draw()
	def getRadius(self):
		return self.radius
	def setRadius(self,r):
		self.radius=r
		self.createMan()
	def getWeapon(self):
		return self.weapon
	def setWeapon(self,w):
		self.weapon=w
		self.createMan()

	
def test():
	win = gr.GraphWin( 'testament of the matchman', 500, 500, False )
	man=MatchMan(win)
	man.setPosition(25,25)
	man.draw()
	key=win.checkMouse()
	
	while True:
		click=win.checkMouse()
		if click!=None:
			w=1-man.getWeapon()
			man.setWeapon(w)
		key = win.checkKey()
		
		if key=='q':
			break
	
	win.close()

if __name__ == "__main__":
	test()
	