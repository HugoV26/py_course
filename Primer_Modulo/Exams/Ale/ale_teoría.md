1. ¿Cuáles son las diferencias entre una Lista y una Tupla?         *2 puntos*
La diferencia es que las tuplas son inmutables.	                 
	
2. ¿Cuáles son las dos formas de declarar una Lista y un Tupla?	    *1 punto*
Las listas se declaran de la siguiente manera: 	my_list = [aquí van los elementos]
						my_list = list((aquí van los elementos))
Las tuplas se declaran de la siguiente manera:	my_tuple = (aquí van los elementos)
						my_tuple = tuple((aquí van los elementos))

3. Mencione 5 operadores de asignación y su uso.                *1 punto*
Suma +=  
Resta -= 
División /=
Multiplicación *= 
Exponencial **= 



4. ¿Cuál es la diferencia entre usar coma(,) y el operador de adición(+) dentro de un print?    *2 puntos*
Se usan para concatenar; se usa coma(,) cuando los datos son de diferente tipo; cuando son del mismo se usa adición(+); si es string se concatena pero si es int o float se suman. 

5. Indica 3 formas incorrectas de declarar una variable.    *1 punto*
1. Comenzar con un número ej: 2var_var = …
2. Incluir guión medio ej. my-var = …
3. Incluir un espacio ej. my var = … 


6. ¿Cómo obtienes el residuo de una división en python?     *0 puntos | Solución: x %= 2*
my_var = input(“Ingresa el número que quieres dividir: “) 
my_var2 = my_var
my_divisor = input(“Ingresa el número entre el que quieres dividir: “) 
my_var /= my_divisor 

if type(my_var) == int:
print(“Tu residuo es 0.”)
else:
	my_var = int(my_var) 
	my_var *= my_divisor 
my_var2 -= my_var 
print(“Tu residuo es: ” + str(my_var2))

7. ¿Cuáles son los métodos que comparten las Tuplas y las Listas?  *1 punto*
.count() y .index()