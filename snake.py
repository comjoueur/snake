from juego import *
from Tkinter import *
def sacar1(event):
    global serp
    global space
    global pera
    lado="a"
    pedir_tecla(serp,space,lado,pera)
def sacar2(event):
    global serp
    global space
    global pera
    lado="d"
    pedir_tecla(serp,space,lado,pera)
def sacar3(event):
    global serp
    global space
    global pera
    lado="w"
    pedir_tecla(serp,space,lado,pera)
def sacar4(event):
    global serp
    global space
    global pera
    lado="s"
    pedir_tecla(serp,space,lado,pera)
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
root.mainloop()
