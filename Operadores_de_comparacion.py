#OPERADORES DE COMPARACION              (==,1=,<,>,>=,<=)
num1 = 5
num2 = 4
print(num1 == num2)

#ejemplo con cadenas 

cad = "hola"
cad1 = "hola"

print (cad == cad1)
 #CUANDO LAS VARIABLES UTILIZANDO ESTE OPERADOR "==" SON IGUALES TE MANDA UN TRUE 
 #PERO SI LOS VALORES DE LAS VARIABLES SON DIFERENTES TE MANDA DE RETORNO UN "FALSE"

if (cad == "hola"):
    print("dijo hola")
#-------------------------------------------------------------------------------------------------------------------------
#OPERADOR "DISTINTO DE:"

# ESTE OPERADOR FUNCIONA AL CONTRARIO DEL ANTERIOR, ESTE ANALIZA SI LAS VARIABLES EN COMPRACION SON DIFERENTES Y SI LAS SON, ENTONCES ES CORRECTO    
# SI LOS VALORES SON IGUALES TE MANDARA UN "FALSE"        
# #SI LOS OPERADORES SON DISTINTOS TE MANDARA UN "TRUE"

print("LOS VALORES SON DISTINTOS: " , (num1 != num2) )
print ("LOS VALORS SON IGUALES: "+cad != cad1)
#-------------------------------------------------------------------------------------------------------------------------

#OPERADORES MAYOR Y MENOR
#COMPARACION DE 2 NUMEROS UTILIZANDO LOS OPERADORES             "MAYOR QUE" Y "MENOR QUE" 
print("El numero 2 es menor que numero 1:" , (num2 < num1))
print("El numero 1 es menor que numero 2:" , (num1 < num2))

print("El numero 2 es mayor que numero 1:" , (num2 > num1))
print("El numero 1 es mayor que numero 2:" , (num1 > num2))

#-------------------------------------------------------------------------------------------------------------------------

#OPERADORES "MAYOR O IGUAL QUE :" Y "MENOR O IGUAL QUE: "

#SI ES MENOR O IGUAL EL RESULTADO SERA TRUE 
#SI ES MAYOR EL RESULTADO ES "FALSE"

print("El numero 2 es MENOR O IGUAL que numero 1:" , (num2 <= num1))
print("El numero 1 es MENOR O IGUAL que numero2 :" , (num1 <= num2))

print("El numero 2 es MAYOR O IGUAL que numero 1:" , (num2 >= num1))
print("El numero 1 es MAYOR O IGUAL que numero 2:" , (num1 >= num2))

