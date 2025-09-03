base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
Lado = float(input("Ingrese el lado del cuadrado"))

Area_Triangulo = (base * altura)/2
Area_Cuadrado = Lado * Lado
Area_Total = Area_Triangulo + Area_Cuadrado 

Precio_metro_cuadrado = 440000
Precio_total_terreno = Area_Total * Precio_metro_cuadrado
print ("El area total del terreno ea :", (Area_Total), "metros cuadrados ")
print ("El precio to del terreno es de :", (Precio_total_terreno, "Pesos"))