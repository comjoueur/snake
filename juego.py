from random import *
from os import *
from time import *
class espacio:
    x=10
    y=10
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
def condicion(a,r):
    return a>=r or a<0
def limite(a,space):
    t=len(a.posicion)-1
    o=a.posicion
    return condicion(o[t][0],space.y) or condicion(o[t][1],space.x) 
def pedir_tecla(a,space,manzana):
    x=True
    print space.x,space.y
    r=[1,2]
    r=a.posicion[0]
    avanzar(a)
    for i in range(len(a.posicion)-1):
        if(a.posicion[i]==a.posicion[len(a.posicion)-1]):x=False
    p_comiofruta(a,space,manzana,r)
    x=x and not limite(a,space)
    if x :dibujar(a,space,manzana)
    return x
class fruta:
    x=0
    y=10
def aparecer_fruta(a,space,manzana):
    x=0
    y=0
    b=True
    while(b):
        y=randrange(0,space.x)
        x=randrange(0,space.y)
        l=[x,y]
        b=False
        for i in a.posicion:
            if(i==l):b=True
    manzana.x=x
    manzana.y=y
def comer_fruta(a,space,manzana):
    a.puntaje+=10
    aparecer_fruta(a,space,manzana)
def p_comiofruta(a,space,manzana,r):
    l=[manzana.x,manzana.y]
    if(a.posicion[len(a.posicion)-1]==l):
        a.posicion.insert(0,r)
        comer_fruta(a,space,manzana)
        return True
    return False
def dibujar(a,space,manzana):
    system("clear")
    print space.x,space.y
    l=[]
    u=[]
    for i in range(space.y):
        for i in range(space.x):
            u.append('.')
        l.append(u)
        u=[]
    for i in range(len(a.posicion)):
        l[a.posicion[i][0]][a.posicion[i][1]]="*"
    l[manzana.x][manzana.y]="o"
    for i in range(len(l)):
        for j in range(len(l[i])):
            print l[i][j],
        print ""
