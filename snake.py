from juego import *
from Tkinter import *
import time
def sacar1(event):
    global serp
    serp.direccion="izquierda"
def sacar2(event):
    global serp
    serp.direccion="derecha"
def sacar3(event):
    global serp
    serp.direccion="arriba"
def sacar4(event):
    global serp
    serp.direccion="abajo"
def task():
    sleep(0.3)
    global serp
    global space
    global pera
    pedir_tecla(serp,space,pera)
    root.after(60,task)
serp=serpiente()
space=espacio()
pera=fruta()
y=0
if y==0:
    y+=1
    aparecer_fruta(serp,space,pera)
    dibujar(serp,space,pera)
space.x=10
space.y=10
root=Tk()
root.bind('<Left>',sacar1)
root.bind('<Right>',sacar2)
root.bind('<Up>',sacar3)
root.bind('<Down>',sacar4)
root.after(30,task)
root.mainloop()
