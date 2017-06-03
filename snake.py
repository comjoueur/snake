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
    if movimiento(serp,space,pera)==-1:
        system("clear")
        print "You Lose"
        return 0
    root.after(30,task)
serp=serpiente()
space=espacio()
pera=fruta()
y=0
space.x=15
space.y=15
if y==0:
    y+=1
    aparecer_fruta(serp,space,pera)
    dibujar(serp,space,pera)
root=Tk()
root.bind('<Left>',sacar1)
root.bind('<Right>',sacar2)
root.bind('<Up>',sacar3)
root.bind('<Down>',sacar4)
root.after(30,task)
root.mainloop()
