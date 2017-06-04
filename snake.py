from juego import *
from Tkinter import *
from os import *
def sacar1(event):
    global serp
    if serp.direccion!="derecha":
        serp.direccion="izquierda"
def sacar2(event):
    global serp
    if serp.direccion!="izquierda":
        serp.direccion="derecha"
def sacar3(event):
    global serp
    if serp.direccion!="abajo":
        serp.direccion="arriba"
def sacar4(event):
    global serp
    if serp.direccion!="arriba":
        serp.direccion="abajo"
def task():
    sleep(0.1)
    global serp
    global space
    global pera
    global dif
    if serp.estado=="ganar":return 0
    if movimiento(serp,space,pera,dif)==False:
        system("clear")
        print "You Lose"
        return 0
    root.after(15,task)
cont=5
system("clear")
while(cont>0):
    print "el juego comienza en...",cont
    sleep(1)
    system("clear")
    cont-=1
space=espacio()
space.x=20
space.y=20
serp=serpiente()
serp.posicion=[[space.x/2,0],[space.x/2,1],[space.x/2,2]]
pera=fruta()
dif=obstaculos()
y=0
if y==0:
    y+=1
    aparecer_fruta(serp,space,pera,dif)
    dibujar(serp,space,pera,dif)
root=Tk()
root.bind('<Left>',sacar1)
root.bind('<Right>',sacar2)
root.bind('<Up>',sacar3)
root.bind('<Down>',sacar4)
root.after(15,task)
root.mainloop()
