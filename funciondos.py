import ramdom

# Realiazar funciones probabilidad

def probabilidad(num_lanzamientos,num_caras) :

    #Simular los lanzamientos de la moneda
    resultados=[ramdom.choice([0,1])] for _ in range(num_lanzamientos)

    #Calcular la probalidad de obtener el numero caras
    prob=resultados.count(1)/num_lanzamientos
    return prob

#Ejemplos de uso ( Declarcion de objetos)
num_lanzamientos=10
num_caras=6

prob=probabilidad(num_lanzamientos,num_caras)
print(f"La probabilidad de obtener{num_caras} caras en {num_lanzamientos} es {prob:.4f}")
