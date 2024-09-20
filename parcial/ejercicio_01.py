""" Generar una lista por compresión que contenga la raíz cuadrada de todos los números desde 0 hasta un número limite N.
 """

x,y = 5,2
def ExVar1():
    print(x,y)

def ExVar2():
    x = 2
    def ExVar21():
        nonlocal x
        global y
        y,x = x,y
        print(x,y)
    ExVar21()

def ExVar3():
    def ExVar31():
        global x,y
        x,y = y,x
    ExVar31()
    print(y,x)

ExVar3()
ExVar2()
ExVar1()