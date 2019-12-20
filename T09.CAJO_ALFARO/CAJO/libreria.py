def pedir(x):
    numero_incorrecto=(x.isdigit()==False)
    while numero_incorrecto:
        x=input("Ingresar numero:")
        numero_incorrecto=(x.isdigit()==False)
    return int(x)


def area_del_triangulo(base,altura):
    base=pedir(base)
    altura=pedir(altura)
    area=(base*altura)/2
    return area


def mayor(n1,n2):
    if (n1 > n2):
        return n1
    else:
        return n2

def sumar(a,b):
    a=pedir(a)
    b=pedir(b)
    suma=a+b
    return suma

def area_de_un_trapecio(bmenor,bmayor,altura):
    bmenor=pedir(bmenor)
    bmayor=pedir(bmayor)
    altura=pedir(altura)
    area=((bmayor+bmenor)*altura)/2
    return area

def area_de_un_circulo(pi,radio):
    pi=3.14
    radio=pedir(radio)
    area=pi*(radio**2)
    return area

def maximo_entero(y):
    y=pedir(y)

def raiz_cuadrada(x):
    x=pedir(x)
    return x**1/2

def raiz_cubica(y):
    y=pedir(y)
    return y**1/3

def elevar_cuadrado(s):
    s=pedir(s)
    return s**2

def raiz_n(y,n):
    y=pedir(y)
    n=pedir(n)
    return y**1/n

def elevar_a_la_n(x,n):
    x=pedir(x)
    n=pedir(n)
    return x**n

def repetir_n_veces(cad,n):
    return cad*int(n)

def promedio(nota1,nota2):
    nota1=pedir(nota1)
    nota2=pedir(nota2)
    resultado=(nota1+nota2)/2
    return resultado

def condicion_alumno(nota1,nota2):
    a=promedio(nota1,nota2)
    if a>=10.5 and a<=20:
        return "Aprobado"
    else:
        return "Desaprobado"

def rango(x,y,numero):
    x=pedir(x)
    y=pedir(y)
    numero=pedir(numero)
    ran=(numero>x and numero<y)
    return ran

def numero_telefono(telefono):
    telefono=pedir(telefono)
    if len(str(telefono))==9:
        return True
    else:
        return False

def numero_de_letras(palabra):
    a=0
    for x in palabra:
        a+=1
    return a

def numero_vocales(palabra):
    a=0
    for x in palabra:
        if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
            a+=1
    return a

def temperatura(r1,r2,tem):
    rango(r1,r2,tem)
    fiebre=(tem>r1 and tem<r2)
    if fiebre:
        return "tiene fiebre"
    else:
        return "temperatura normal"

def vuelto(p1,p2,dinero):
    p1=pedir(p1)
    p2=pedir(p2)
    vue=float(dinero)-p1-p2
    return vue

def volumen_cubo(lado):
    lado=pedir(lado)
    return lado**3

def area_cuadrado(lado):
    lado=pedir(lado)
    return lado**2

def area_triangulo(base,altura):
    base=pedir(base)
    altura=pedir(altura)
    return base*altura/2

def area_rectangulo(base,altura):
    base=pedir(base)
    altura=pedir(altura)
    return base*altura

