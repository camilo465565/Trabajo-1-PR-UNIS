import math
while True:
    print ("calculadora de operacions basicas")
    print ("1.Suma")
    print ("2.Resta")
    print ("3.Multiplicacion")
    print ("4.Division")
    print ("5.Potencia")
    print ("6.Raiz cuadrada")
    print ("7.Logaritmo natural")
    print ("8.Coseno")
    print ("9.Salir")
    op = int (input("Ingrese la operacion a realizar :"))
    if op == 1:
        numero1 = int (input("Ingrese su primer numero: "))
        numero2 = int (input("Ingrese su segundo numero: "))
        rta = numero1 + numero2
        print (f"La suma es {rta}")
    elif op == 2:
        numero1 = int (input("Ingrese su primer numero: "))
        numero2 = int (input("Ingrese su segundo numero: "))
        rta = numero1 - numero2
        print (f"La resta es {rta}")
    elif op == 3:
        numero1 = int (input("Ingrese su primer numero: "))
        numero2 = int (input("Ingrese su segundo numero: "))
        rta = numero1 * numero2
        print (f"La multiplicacion es {rta}")
    elif op == 4:
        numero1 = int (input("Ingrese su primer numero: "))
        numero2 = int (input("Ingrese su segundo numero: "))
        if numero2 != 0: 
            rta = numero1 / numero2
            print (f"La division es {rta}")
        else:
            print("Error: No se puede dividir por cero.")
    elif op == 5:
        numero1 = int (input("Ingrese la base: "))
        numero2 = int (input("Ingrese el exponente: "))
        rta = numero1 ** numero2
        print (f"La potencia es {rta}")
    elif op == 6:
        numero1 = int(input("Ingrese su primer numero:"))
        if numero1 >= 0:
            rta = math.sqrt(numero1)
            print (f"La raiz cuadrada es {rta}")
        else:
            print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
    elif op == 7:
        numero1 = int (input("Ingrese su primer numero: "))
        if numero1 > 0:
            rta = 10 *math.log(numero1)
            print (f"El logaritmo natural es {rta}")
        else:
            print("Error: El número debe ser mayor que 0 para calcular el logaritmo natural.")
    elif op == 8:
        numero1 = int (input("Ingrese su primer numero: "))
        rta = math.cos(math.radians(numero1))
        print (f"Ingrese el coseno es {rta}")
    elif op == 9:
        print("Saliendo de la calculadora...")
        break

    
