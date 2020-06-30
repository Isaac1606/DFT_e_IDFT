# Carballo Pérez Isaac
import math
import cmath
import numpy as np
import re

# Reglas
regla1 = '1.- W**K+N) = W*K'
regla2 = '2.- W**(K+N/2) = -W**K'
regla3 = '3.- W**KN = 1'

# Funcion que construye la matriz dada una secuencia
def hacerMatriz(sec):
    longitud = len(sec)
    matriz = []
    for fila in range(longitud):
        lista = []
        for columna in range(longitud):
            if columna == 0:
                lista.append('1')
            if columna > 0:
                lista.append(f'W**({fila * columna})')
        matriz.append(lista)
    matriz[0] = ['1' for i in range(longitud)]
    return matriz

# Funcion que permite determinar de acorde al exponente que tipo
# de regla es la que se debe de ocupar recordando que:
# W^K+N = W^K 
# W^K+N/2 = -W^K
# w^KN = 1
def separarPorRegla(lensec,m):
    for i in range(1,len(m)):
        for j in range(1,len(m[0])):
            expresion = m[i][j]
            exponente = expresion[4:-1]
            exponente = int(exponente)
            cociente = exponente // lensec
            residuo = exponente % lensec
            resta = abs(lensec-exponente)
            if resta + (lensec/2) == exponente or resta == exponente:
                m[i][j] = '-' + m[i][j][:4] + str(reducir(lensec,exponente)) + ')'
                #m[i][j] = '-' + m[i][j][:4] + str(reducir2(exponente)) + ')'
            elif cociente >= 1 and residuo == 0:
                reducir(lensec,exponente)
                m[i][j] = '1'
            elif resta + lensec == exponente and resta != 0:
                m[i][j] =  m[i][j][:4] + str(reducir(lensec,exponente)) + ')'
                #m[i][j] =  m[i][j][:4] + str(reducir2(exponente)) + ')'
    return m

# Funcion de tipo recursiva que ayuda a determinar cual hasta que punto 
# un exponente puede reducirse 
def reducir(lensec,exponente):
    regla = ''
    car = ' '
    copia = exponente
    cociente = exponente // lensec
    residuo = exponente % lensec
    resta = abs(lensec-exponente)
    if resta + (N/2) == exponente or resta == exponente:
            if resta == exponente:
                exponente = 0
            else:
                exponente = resta
            car = ' -'
            regla = '(2)'
    if cociente >= 1 and residuo == 0:
        exponente = 0
        regla = '(3)'
    if resta + lensec == exponente:
        exponente = resta
        regla = '(1)'
    print(f'W**{copia} ={car}W**{exponente} por {regla}',end="\n")
    while exponente >= lensec:
        exponente = reducir(len(sec),exponente)
    return exponente

# Funcion que sustituye las W por su expresion imaginaria
# la evalua y ese resultado es el colocado
def sustituir(m):
    for i in range(1,len(m)):
        for j in range(1,len(m[i])):
            m[i][j] = m[i][j].replace('W',f'{cmath.e**complex(0,-2*cmath.pi/N)}') 
            m[i][j] = complex(eval(m[i][j]))
            if str(m[i][j].real).count('e') == 1 :
                m[i][j] = complex(0,m[i][j].imag)
            if str(m[i][j].imag).count('e') == 1 :
                m[i][j] = complex(m[i][j].real,0)
    return m

# Funcion para convertir la matriz a una matriz de numeros complejos
def convertirAComplejo(m):
    m = np.array(m)
    return m.astype(np.complex)

# Funcion que crea la lista de los conjugados de una secuencia
def crearConjugados(a):
    longitud = a.shape[0]
    mitad = longitud / 2 
    mitad2 = math.ceil(mitad)
    count = 0
    if mitad == mitad2:
        for i in range(longitud):
            if mitad - i > -1 and mitad + i < longitud and mitad - i != mitad + i:
                x1 = a[int(mitad-i)]
                x2 = a[int(mitad+i)]
                #print(f'{x1} & {x2} son complejos conjugados')
                print(f'x[{int(mitad-i)}] & x[{int(mitad+i)}]')
    else:
        a = np.insert(a,int(mitad2),0)
        for i in range(longitud+1):
            if mitad2 - i > -1 and mitad2 + i < longitud+1 and mitad2 - i != mitad2 + i:
                x1 = a[int(mitad2-i)]
                x2 = a[int(mitad2+i-1)]
                print(f'{x1} & {x2} son complejos conjugados')
                print(f'x[{int(mitad2-i)}] & x[{int(mitad2+i-1)}]')

# Funcion que dada una matriz de complejos devuelve
# el conjugado de esa matriz 
def sustituirConjugadoMatriz(m):
    return np.conj(m)

def eliminarCeros(m):
    m = m.tolist()
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j].real == 0:
                m[i][j] = str(m[i][j])
                m[i][j] = m[i][j][2:]
            elif m[i][j].imag == 0:
                m[i][j] = str(m[i][j])
                m[i][j] = m[i][j][:-2]
    m = np.array(m)
    return m.astype(np.str)


print(f'\nPrograma que dada una secuencia calcula la DFT e IDFT')
print("\tFormato de secuencia: n-1 _n n+1")
print("""\t\nNotas:  El origen se señala con prefijo '_'\n\tLos numeros se separan con espacios.""")
bandera = True
while bandera:
    sec = input("\nIngrese la secuencia x(n):\n>> ")
    if len(sec) == 0:
        bandera = False
    cop = sec.split()
    origen = [i for i,key in enumerate(cop) if cop[i].startswith('_') ][0]

    sec = sec.replace('_','').split()
    sec = [complex(eval(i)) for i in sec]
    print(f'\nLa secuencia ingresada fue: {sec}')

    N = len(sec)

    print(f'La N de la secuencia es: {N}')
    print(f'El indice del origen de la secuencia es: {origen}')

    ma = hacerMatriz(sec)
    print(f'\nForma matricial Wn:\n{np.array(ma)}')

    print(f'\nLa lista de reglas que nos ayudan a simplificar es la sig:')
    print(f'{regla1}\n{regla2}\n{regla3}')
    s = separarPorRegla(N,ma)
    print(f'\nForma matricial Wn simplificada:\n{np.array(s)}')

    r = sustituir(s)
    r = convertirAComplejo(r)
    
    print(f'\nMatriz Wn despues de evaluar:\n{r.round(decimals=3)}')

    print(f'\nMatriz Wn conjugada:\n{np.conj(r.round(decimals=3))}')

    x = np.array(sec)
    #print(x)

    xk = np.dot(x,r)
    xk = xk.round(decimals=3)
    xk = xk.astype(np.str)
    xk[origen] = '_'+ xk[origen] 
    print(f'\nSecuencia DFT Xk:\n{xk}')

    print('\nLos complejos conjugados de Xk son: ')
    crearConjugados(xk)

    cr = sustituirConjugadoMatriz(r)
    cxk = (1/N) * np.dot(x,cr)
    cxk = cxk.round(decimals=3)
    cxk = cxk.astype(np.str)
    cxk[origen] = '_'+ cxk[origen] 
    print(f'\nIDFT de la secuecnia Xk:\n{cxk}')
    