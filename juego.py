from random import *
class espacio:
    x=50
    y=50
class serpiente:
    tamano=0
    direccion="derecha"
    posicion=[]
    par=[0,0]
    posicion.append(par)
    par=[0,1]
    posicion.append(par)
    par=[0,2]
    posicion.append(par)
    puntaje=0
def avanzar(a):
    g=a.posicion
    l=[1,2]
    if a.direccion=="izquierda":
        l[0]=g[len(g)-1][0]
        l[1]=g[len(g)-1][1]-1
        a.posicion.append(l)
    elif a.direccion=="derecha":
        l[0]=g[len(g)-1][0]
        l[1]=g[len(g)-1][1]+1
        print a.posicion
        a.posicion.append(l)
    elif a.direccion=="arriba":
        l[0]=g[len(g)-1][0]-1
        l[1]=g[len(g)-1][1]
        a.posicion.append(l)
    elif a.direccion=="abajo":
        l[0]=g[len(g)-1][0]+1
        l[1]=g[len(g)-1][1]
        a.posicion.append(l)
    a.posicion.pop(0);

def mov_iz(a):
    a.direccion="izquierda"
    avanzar(a)
def mov_de(a):
    a.direccion="derecha"
    avanzar(a)
def mov_ar(a):
    a.direccion="arriba"
    avanzar(a)
def mov_ab(a):
    a.direccion="abajo"
    avanzar(a)
class fruta:
    x=0
    y=10
def aparecer_fruta(a,espacio,manzana):
    x=0
    y=0
    b=True
    while(b):
        l=[x,y]
        b=False
        for i in a.posicion:
            if(l==i):b=True
        x=randrange(0,espacio.x)
        y=randrange(0,espacio.y)
    manzana.x=x
    manzana.y=y
def comer_fruta(a,espacio,manzana):
    a.puntaje+=10
    aparecer_fruta(a,espacio,manzana)
def p_comiofruta(a,espacio,manzana):
    l=[manzana.x,manzana.y]
    if(a.posicion[len(a.posicion)-1]==l):comer_fruta(a,espacio,manzana)
