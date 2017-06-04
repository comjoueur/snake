from random import *
from os import *
from time import *
class espacio:
    x=10
    y=10
class serpiente:
    tamano=0
    direccion="derecha"
    posicion=[[0,0],[0,1],[0,2]]
    puntaje=0
    nivel=1
    estado="perder"
class obstaculos:
    posicion=[]
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

def limite(a,space):
    o=[]
    t=0
    t=len(a.posicion)-1
    o=a.posicion
    if o[t][0]<0:
        return 4
    elif o[t][0]>=space.y:
        return 2
    elif o[t][1]<0:
        return 1
    elif o[t][1]>=space.x:
        return 3
    return 0
def ganar(a,space,manzana,dif):
    if a.puntaje>=50 and a.nivel==1:
        u=[[space.x/2,0],[space.x/2,1],[space.x/2,2]]
        a.posicion=u
        system("clear")
        x=5
        while(x>0):
            print "nivel 2 en....",x
            sleep(1)
            system("clear")
            x-=1
        a.direccion="derecha"
        a.nivel=2
        return True
    elif a.puntaje>=100 and a.nivel==2:
        u=[[space.x/2,0],[space.x/2,1],[space.x/2,2]]
        dif.posicion=[[space.y-4,space.x-4],[space.y-5,space.x-4],[space.y-4,space.x-5],[space.y-4,3],[space.y-5,3],[space.y-4,4]]
        a.posicion=u
        system("clear")
        x=5
        while(x>0):
            print "nivel 3 en....",x
            sleep(1)
            system("clear")
            x-=1
        a.direccion="derecha"
        a.nivel=3
        return True
    elif a.puntaje>=150 and a.nivel==3:
        system("clear")
        print "usted ha ganado el juego"
        a.estado="ganar"
        return True
    return False
def movimiento(a,space,manzana,dif):
    x=True
    r=[1,2]
    r=a.posicion[0]
    avanzar(a)
    for i in range(len(a.posicion)-1):
        if(a.posicion[i]==a.posicion[len(a.posicion)-1]):x=False
    if ganar(a,space,manzana,dif):return True
    if a.nivel==3:
        for i in dif.posicion:
            if i==a.posicion[len(a.posicion)-1]:x=False
    z=limite(a,space)
    if a.nivel>=2:
        if z!=0:
            x=False
    else:
        if z!=0:
            if z==1:
                a.posicion[len(a.posicion)-1][1]=space.x-1
            elif z==2:
                a.posicion[len(a.posicion)-1][0]=0
            elif z==3:
                a.posicion[len(a.posicion)-1][1]=0
            elif z==4:
                a.posicion[len(a.posicion)-1][0]=space.y-1
    for i in range(len(a.posicion)-1):
        if(a.posicion[i]==a.posicion[len(a.posicion)-1]):x=False
    p_comiofruta(a,space,manzana,r,dif)
    if ganar(a,space,manzana,dif):return True
    if x==False:return False
    if x :dibujar(a,space,manzana,dif)
    return x
class fruta:
    x=0
    y=10
def aparecer_fruta(a,space,manzana,dif):
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
        for i in dif.posicion:
            if i==l:b=True
    manzana.x=x
    manzana.y=y
def comer_fruta(a,space,manzana,dif):
    a.puntaje+=10
    aparecer_fruta(a,space,manzana,dif)
def p_comiofruta(a,space,manzana,r,dif):
    l=[manzana.x,manzana.y]
    if(a.posicion[len(a.posicion)-1]==l):
        a.posicion.insert(0,r)
        comer_fruta(a,space,manzana,dif)
        return True
    return False
def dibujar(a,space,manzana,dif):
    system("clear")
    print a.puntaje
    l=[]
    u=[]
    for i in range(space.y):
        for i in range(space.x):
            u.append('.')
        l.append(u)
        u=[]
    for i in range(len(dif.posicion)):
        l[dif.posicion[i][0]][dif.posicion[i][1]]="p"
    for i in range(len(a.posicion)):
        l[a.posicion[i][0]][a.posicion[i][1]]="*"
    l[manzana.x][manzana.y]="o"
    for i in range(len(l)):
        for j in range(len(l[i])):
            print l[i][j],
        print ""
