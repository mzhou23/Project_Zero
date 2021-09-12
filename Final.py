#Minghao Zhou
#Nov 29
#CS 152
import graphicsPlus as gr
import physics_objects as pho
import collision as coll
import math
import time
from graphicsPlus import *
def StartScene():
    '''the start scene takes no parameter and would return True or False depending on where users click'''
    win=gr.GraphWin('start scene',500,500,False)#create window for start scene

    block1=pho.Block(win,x0=25,y0=40,width=10,height=8)#start button
    block2=pho.Block(win,x0=25,y0=30,width=10,height=8)#quit button
    block3=pho.Block(win,x0=25,y0=20,width=10,height=8)#quit button
    block4=pho.Block(win,x0=25,y0=10,width=10,height=8)#quit button
    textbox1=gr.Text(gr.Point(250,100),'practice mode')#name the button
    textbox2=gr.Text(gr.Point(250,200),'Player vs. Computer')#name the button
    textbox3=gr.Text(gr.Point(250,300),'Player vs. Player')#name the button
    textbox4=gr.Text(gr.Point(250,400),'quit')#name the button
    p1=block1.getPosition()#assign local variables for judge click
    p2=block2.getPosition()
    p3=block3.getPosition()
    p4=block4.getPosition()
    w1=block1.getWidth()
    w2=block2.getWidth()
    w3=block3.getWidth()
    w4=block4.getWidth()
    h1=block1.getHeight()
    h2=block2.getHeight()
    h3=block3.getHeight()
    h4=block4.getHeight()
    textbox2.draw(win)
    textbox1.draw(win)
    textbox3.draw(win)
    textbox4.draw(win)
    shapes=[block1,block2,block3,block4]
    
    for item in shapes:
        item.draw()#draw the object
    while True:
        click=win.checkMouse()
        if click!=None:
            x=click.getX()/10#convert it to simulation scene
            y=win.getHeight()/10-click.getY()/10
            print(x,y)
            if x<p1[0]+1/2*w1 and x>p1[0]-1/2*w1 and y<p1[1]+1/2*h1 and y>p1[1]-1/2*h1:#if it is in the start button
                win.close()
                scene1()
            if x<p2[0]+1/2*w2 and x>p2[0]-1/2*w2 and y<p2[1]+1/2*h2 and y>p2[1]-1/2*h2:#if it is in the quit button
                win.close()
                scene2()
            if x<p3[0]+1/2*w3 and x>p3[0]-1/2*w3 and y<p3[1]+1/2*h3 and y>p3[1]-1/2*h3:#if it is in the quit button
                win.close()
                scene3()
            if x<p4[0]+1/2*w4 and x>p4[0]-1/2*w4 and y<p4[1]+1/2*h4 and y>p4[1]-1/2*h4:#if it is in the quit button
                win.close()
                
        
        
        time.sleep(0.033)#30 loop per sec
        win.update()
def final(success,scene,p=None):
    win=gr.GraphWin('start scene',500,500,False)#create window for start scene
    
    
    block2=pho.Block(win,x0=25,y0=30,width=10,height=8)#quit button
    block3=pho.Block(win,x0=25,y0=20,width=10,height=8)#quit button
    if p!=None:
        if p==3:
            textbox1=gr.Text(gr.Point(250,100),'tie game!!!')#name the button
        else:
            textbox1=gr.Text(gr.Point(250,100),'player'+str(p)+'win')#name the button
    else:
        if success==True:

            textbox1=gr.Text(gr.Point(250,100),'you win!')#name the button
        else:
            textbox1=gr.Text(gr.Point(250,100),'you lose!')#name the button


    textbox2=gr.Text(gr.Point(250,200),'Replay')#name the button
    textbox3=gr.Text(gr.Point(250,300),'Menu')#name the button
    
    
    p2=block2.getPosition()
    p3=block3.getPosition()
    
    w2=block2.getWidth()
    w3=block3.getWidth()
    
    
    h2=block2.getHeight()
    h3=block3.getHeight()

    textbox2.draw(win)
    textbox1.draw(win)
    textbox3.draw(win)

    shapes=[block2,block3]
    
    for item in shapes:
        item.draw()#draw the object
    while True:
        click=win.checkMouse()
        if click!=None:
            x=click.getX()/10#convert it to simulation scene
            y=win.getHeight()/10-click.getY()/10
            print(x,y)
        
            if x<p2[0]+1/2*w2 and x>p2[0]-1/2*w2 and y<p2[1]+1/2*h2 and y>p2[1]-1/2*h2:#if it is in the quit button
                win.close()
                if scene==1:
                    scene1()
                elif scene==2:
                    scene2()
                elif scene==3:
                    scene3()
            if x<p3[0]+1/2*w3 and x>p3[0]-1/2*w3 and y<p3[1]+1/2*h3 and y>p3[1]-1/2*h3:#if it is in the quit button
                win.close()
                StartScene()

                
        
        
        time.sleep(0.033)#30 loop per sec
        win.update()
def scene1():
    
        win = gr.GraphWin('final game', 1000, 600, False)

        #win.setBackground('blue')
        man=pho.MatchMan(win)
        ground=pho.Block(win,x0=50,y0=5,width=100,height=10)
        ground.setColor('green')
       
        ground.draw()
        ground.setElasticity(0)
        block1=pho.Block(win,x0=50,y0=40,width=20,height=5)
        block1.setElasticity(0)
        block1.draw()
        list=[ground,block1]
        man.setPosition(25,10)
        man.setAcceleration(0,-10)
        man.draw()
        pig=pho.Pig(win,5,4)
        pig.setPosition(80,20)
        pig.draw()
        i=0
        dt=0.02
        bullet=[]
        Hp=100
        textbox1=gr.Text(gr.Point(500,100),'the pig has'+str(Hp)+'Hp')
        textbox2=gr.Text(gr.Point(200,100),'Level 1, practice mode \n'+'use a,w,d to jump and move, use j to shoot, click to change the weapon')
        textbox2.draw(win)
        textbox1.draw(win)
        success=False
        while True:
            key='start'
            v=man.getVelocity()
            
            
            key=win.checkKey()
            click=win.checkMouse()
            if click!= None:
                w=1-man.getWeapon()
                man.setWeapon(w)

		
            if key=='q':
                break
            if key=='d':
                posX=man.getPosition()[0]
                posY=man.getPosition()[1]
                man.setPosition(posX+2.5,posY)
            elif key=='a':
                posX=man.getPosition()[0]
                posY=man.getPosition()[1]
                man.setPosition(posX-2.5,posY)
            elif key=='w':
                if man.getWeapon()==0:
                    man.setVelocity(0,10)
                else:
                    man.setVelocity(0,20)
            
            if man.getWeapon()==0:
                if key=='j':
                    c=pho.Ball(win,r=0.5)
                    posX=man.getPosition()[0]
                    posY=man.getPosition()[1]
                    c.setPosition(posX+3*man.getRadius(),posY)
                    c.setVelocity(20,0)
                    bullet.append(c)
                    c.draw()
            man.update(dt)
            
            for item in list:
                item.update(dt)
                if coll.collision(man, item, dt):
                    if item.getType()=='pig':
                        count+=1
            
            for item in bullet:
                pig.update(dt)
                if coll.collision(item,pig,dt):
                    Hp-=10
                    print(Hp)

                    item.undraw()
                    if Hp<=0:
                        pig.undraw()
                        textbox1.setText('congratulation')
                        success=True
                        win.close()
                        final(success,scene=1)
                    else:
                        textbox1.setText('the pig has  '+str(Hp)+'  Hp')

                else:
                    item.update(dt)

            if i % 10:
                win.update()
                time.sleep(0.01)
            
            
            i+=1


        win.close()
        
        
    
def scene2():
    
    
      
        win = gr.GraphWin('final game', 1000, 600, False)
        #win.setBackground('blue')
        man=pho.MatchMan(win)
        ground=pho.Block(win,x0=50,y0=5,width=100,height=10)
        ground.setColor('green')
        
        ground.draw()
        ground.setElasticity(0)
        wall=pho.Block(win,x0=2,y0=35,width=4,height=50)
        wall.setElasticity(0.5)
        wall.draw()
        rot=pho.RotatingBlock(win,40,30,15,5)
        rot.setElasticity(0)
        rot.draw()
        rot.setRotVelocity(108)
        list=[ground,rot,wall]
        man.setPosition(25,10)
        man.setAcceleration(0,-20)
        man.draw()
        pig=pho.Pig(win,5,4)
        pig.setPosition(80,20)
        pig.draw()
        i=0
        dt=0.02
        bullet=[]
        humanHp=3
        Hp=100
        textbox1=gr.Text(gr.Point(500,100),'the pig has'+str(Hp)+'Hp')
        textbox1.draw(win)
        textbox2=gr.Text(gr.Point(200,100),'PVC mode\n''you have 3 HP, jump to avoid getting shot from the pig')
        textbox2.draw(win)
        success=False
        ball1=gr.Circle(gr.Point(30,10),5)
        ball2=gr.Circle(gr.Point(40,10),5)
        ball3=gr.Circle(gr.Point(50,10),5)
        blood=[ball1,ball2,ball3]
        for item in blood:
            item.setFill('red')
            item.draw(win)
        while True:
            key='start'
            
            
            #print(v)
            key=win.checkKey()
            click=win.checkMouse()
            if click!= None:
                w=1-man.getWeapon()
                man.setWeapon(w)


            if key=='q':
                break
            if key=='d':
                posX=man.getPosition()[0]
                posY=man.getPosition()[1]
                man.setPosition(posX+2.5,posY)
            elif key=='a':
                posX=man.getPosition()[0]
                posY=man.getPosition()[1]
                man.setPosition(posX-2.5,posY)
            elif key=='w':
                if man.getWeapon()==0:
                    man.setVelocity(0,10)
                else:
                    man.setVelocity(0,20)
            
            if man.getWeapon()==0:
                if key=='j':
                    c=pho.Ball(win,r=0.5)
                    posX=man.getPosition()[0]
                    posY=man.getPosition()[1]
                    c.setPosition(posX+3*man.getRadius(),posY)
                    c.setVelocity(20,0)
                    bullet.append(c)
                    c.draw()
            man.update(dt)
            
            for item in list:
                item.update(dt)
                if coll.collision(man, item, dt):
                    if item.getType()=='ball':
                        if man.getWeapon()==0:
                            
                            humanHp-=1
                            blood[humanHp].setFill('black')
                            if humanHp<=0:
                                man.undraw()
                                success=False
                                textbox1.setText('haha you are dead')
                                final(success,scene=1)
                            
            for item in bullet:
                pig.update(dt)
                if coll.collision(item,pig,dt):
                    Hp-=10
                    print(Hp)

                    item.undraw()
                    if Hp<=0:
                        pig.undraw()
                        textbox1.setText('congratulation')
                        success=True
                        win.close()
                        final(success,scene=2)
                    else:
                        textbox1.setText('the pig has  '+str(Hp)+'  Hp')

                else:
                    item.update(dt)
            if i%200==0:
                c=pho.Ball(win,r=0.5)
                posX=pig.getPosition()[0]
                posY=pig.getPosition()[1]
                c.setPosition(posX-2*pig.getWidth(),posY)
                c.setVelocity(-20,0)
                c.setColor('yellow')
                c.setElasticity(0.5)
                list.append(c)
                c.draw()

            if i % 10:
                win.update()
                time.sleep(0.01)
            
            
            i+=1


        win.close()

        return success  

def scene3():
    
        win = gr.GraphWin('final game', 1000, 600, False)
        #win.setBackground('blue')
        background=Image(Point(500,300),'sky.png')
        background.draw(win)

        man=pho.MatchMan(win)
        man2=pho.MatchMan(win,p=1)
        ground=pho.Block(win,x0=50,y0=5,width=100,height=10)
        ground.setColor('green')
        
        ground.draw()
        ground.setElasticity(0)
        wall=pho.Block(win,x0=1,y0=35,width=2,height=50)
        wall2=pho.Block(win,x0=99,y0=35,width=2,height=50)
        wall2.setElasticity(0.5)
        wall2.draw()
        wall.setElasticity(0.5)
        wall.draw()
        block1=pho.Block(win,x0=25,y0=20,width=10,height=2)
        block1.setElasticity(0)
        block1.draw()
        block2=pho.Block(win,x0=75,y0=20,width=10,height=2)
        block2.setElasticity(0)
        block2.draw()
        block3=pho.Block(win,x0=50,y0=38,width=15,height=2)
        block3.setElasticity(0)
        
        block3.draw()
        list=[ground,wall2,wall,block1,block2,block3]
        man.setPosition(15,14)
        man2.setPosition(85,14)
        man.setAcceleration(0,-20)
        man2.setAcceleration(0,-20)
        man2.draw()
        man.draw()
        
        i=0
        dt=0.02
        bullet=10
        bullet2=10
        humanHp=3
        humanHp2=3

        Hp=100
        textbox1=gr.Text(gr.Point(500,100),'You only have 10 bullets, kill the ohter player!!!')
        
        textbox1.draw(win)
        success=False
        ball1=gr.Circle(gr.Point(30,10),5)
        ball2=gr.Circle(gr.Point(40,10),5)
        ball3=gr.Circle(gr.Point(50,10),5)
        blood=[ball1,ball2,ball3]
        ball4=gr.Circle(gr.Point(970,10),5)
        ball5=gr.Circle(gr.Point(960,10),5)
        ball6=gr.Circle(gr.Point(950,10),5)
        blood2=[ball4,ball5,ball6]
        for item in blood:
            item.setFill('red')
            item.draw(win)
        for item in blood2:
            item.setFill('red')
            item.draw(win)
        listp1=list[:]
        listp2=list[:]
        while True:
            key='start'
            counter=0
            counter1=0
            
            #print(v)
            key=win.checkKey()
            click=win.checkMouse()
            if click!= None:
                w=1-man.getWeapon()
                man.setWeapon(w)


            if key=='q':
                break
            if key=='d':
                posX=man.getPosition()[0]
                posY=man.getPosition()[1]
                man.setPosition(posX+2.5,posY)
            elif key=='a':
                posX=man.getPosition()[0]
                posY=man.getPosition()[1]
                man.setPosition(posX-2.5,posY)
            elif key=='w':
                if man.getWeapon()==0:
                    man.setVelocity(0,10)
                else:
                    man.setVelocity(0,20)
            if key=='Left':
                posX=man2.getPosition()[0]
                posY=man2.getPosition()[1]
                man2.setPosition(posX-2.5,posY)
            elif key=='Right':
                posX=man2.getPosition()[0]
                posY=man2.getPosition()[1]
                man2.setPosition(posX+2.5,posY)
            elif key=='Up':
                if man2.getWeapon()==0:
                    man2.setVelocity(0,10)
                else:
                    man2.setVelocity(0,20)
            if man.getWeapon()==0 and bullet>0:
                if key=='space':
                    bullet-=1
                    c=pho.Ball(win,r=0.5)
                    posX=man.getPosition()[0]
                    posY=man.getPosition()[1]
                    c.setPosition(posX+1.5*man.getRadius(),posY)
                    c.setVelocity(20,0)
                    c.setColor('red')
                    listp2.append(c)
                    c.draw()
            if man2.getWeapon()==0 and bullet2>0:
                if key=='p':
                    bullet2-=1
                    c=pho.Ball(win,r=0.5)
                    posX=man2.getPosition()[0]
                    posY=man2.getPosition()[1]
                    c.setPosition(posX-1.5*man2.getRadius(),posY)
                    c.setVelocity(-20,0)
                    c.setColor('blue')
                    listp1.append(c)
                    c.draw()
            man.update(dt)
            man2.update(dt)
            
            for item in listp1:
                
                item.update(dt)
                if coll.collision(man, item, dt):
                    if item.getType()=='ball':
                        listp1.pop(counter)
                        item.undraw()
                        if man.getWeapon()==0 and humanHp>=1:
                            
                            humanHp-=1
                            blood[humanHp].setFill('black')
                            if humanHp<=0:
                                man.undraw()
                                textbox1.setText('winner is p2!')
                                win.close()
                                final(success,3,p=2)
                    else:
                        counter+=1
                
            for item in listp2:
                item.update(dt)
                if coll.collision(man2, item, dt):
                    if item.getType()=='ball':
                        listp2.pop(counter1)
                        item.undraw()
                        if man2.getWeapon()==0 and humanHp2>0:
                            
                            humanHp2-=1
                            blood2[humanHp2].setFill('black')
                            if humanHp2<=0:
                                man2.undraw()
                                textbox1.setText('winner is p1!') 
                                win.close()
                                final(success,3,p=1)               
                else:
                    counter1+=1
            if bullet==0 and bullet2==0 and humanHp>0 and humanHp2>0:
                textbox1.setText('tie game!')
                win.close()
                final(success,3,p=3)

            if i % 10:
                win.update()
                time.sleep(0.01)
            
            
            i+=1


        win.close()

        return success       


if __name__ == "__main__":
    StartScene()

    