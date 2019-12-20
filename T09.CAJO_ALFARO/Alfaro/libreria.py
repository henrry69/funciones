def pedir_numero(num):
    numero_invalido=(num.isdigit()==False)
    while numero_invalido:
        num=input("ingrese numero:")
        numero_invalido=num.isdigit()==False
    return int(num)

def sumar(n1,n2):
    n1=pedir_numero(n1)
    n2=pedir_numero(n2)
    suma=n1+n2
    return suma

def dividir(numerador,denominador):
    numerador=pedir_numero(numerador)
    denominador=pedir_numero(denominador)
    denominador_invalido=(denominador==0)
    while denominador_invalido:
        denominador=input("Ingrese denominador(!=0):")
        denominador_invalido=(denominador==0)
    division= numerador/int(denominador)
    return division

def multiplicar(a,b):
    a=pedir_numero(a)
    b=pedir_numero(b)
    return a*b

def restar(x,y):
    x=pedir_numero(x)
    y=pedir_numero(y)
    return x-y

def valor_absoluto(j):
    for x in j:
        if x=="-":
            return -1*int(j)
        else:
            return int(j)

def raiz_cuadrada(x):
    x=pedir_numero(x)
    return x**1/2

def raiz_cubica(y):
    y=pedir_numero(y)
    return y**1/3

def elevar_cuadrado(s):
    s=pedir_numero(s)
    return s**2

def raiz_n(y,n):
    y=pedir_numero(y)
    n=pedir_numero(n)
    return y**1/n

def elevar_a_la_n(x,n):
    x=pedir_numero(x)
    n=pedir_numero(n)
    return x**n

def repetir_n_veces(cad,n):
    return cad*int(n)

def promedio(nota1,nota2):
    nota1=pedir_numero(nota1)
    nota2=pedir_numero(nota2)
    resultado=(nota1+nota2)/2
    return resultado

def condicion_alumno(nota1,nota2):
    a=promedio(nota1,nota2)
    if a>=10.5 and a<=20:
        return "Aprobado"
    else:
        return "Desaprobado"

def rango(x,y,numero):
    x=pedir_numero(x)
    y=pedir_numero(y)
    numero=pedir_numero(numero)
    ran=(numero>x and numero<y)
    return ran

def numero_telefono(telefono):
    telefono=pedir_numero(telefono)
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
    p1=pedir_numero(p1)
    p2=pedir_numero(p2)
    vue=float(dinero)-p1-p2
    return vue

def tildes(palabra):
    b=0
    for x in palabra:
        if x=="á" or x=="é" or x=="í" or x=="ó" or x=="ú":
            b+=1
        return b

def volumen_cubo(lado):
    lado=pedir_numero(lado)
    return lado**3

def area_cuadrado(lado):
    lado=pedir_numero(lado)
    return lado**2

def area_triangulo(base,altura):
    base=pedir_numero(base)
    altura=pedir_numero(altura)
    return base*altura/2

def area_rectangulo(base,altura):
    base=pedir_numero(base)
    altura=pedir_numero(altura)
    return base*altura
