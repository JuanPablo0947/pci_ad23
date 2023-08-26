#EJEMPLOS EN PYTHON DE LAS OPERACIONES MATEMÁTICAS QUE USARE EN MI PROGRAMA 

"""
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
""" 
Informa al usuario si la cantidad de agua que tomaste en un día es lo ideal respecto a tu peso 

La fórmula es:  
la cantidad ideal de líquido que debes de tomar por día = 30 ml * tu peso 
""" 
cantidad_vasos = int(input("Aproximadamente cuantos vasos de agua tomas al día? ")) 
cantidad_real_ml = cantidad_vasos * 200 
cantidad_ideal_de_liquido = 30 * 77 
print("Agua que deberías de consumir al día: " + str(cantidad_ideal_de_liquido)) 
print("Agua que consumes consumiste hoy: " + str(cantidad_real_ml)) 

"""
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
#Que el usuario sepa que tanta satisfacción tuvo en su día actual de alimentación 
puntaje_desayuno = float(input("Del 0 al 10, ¿cuánto disfrutaste tu desayuno? ")) 
puntaje_comida = float(input("Del 0 al 10, ¿cuánto disfrutaste tu comida? ")) 
puntaje_cena = float(input("Del 0 al 10, ¿cuánto disfrutaste tu cena? ")) 
puntaje_promedio = (puntaje_desayuno + puntaje_comida + puntaje_cena) / 3 
print("Tu promedio de disfrute es " + str(puntaje_promedio)) 
 
"""
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
""" 
Calcular tu estado de ánimo general con la fórmula NEV 

El NEV (Net Emotional Value) mide las emociones positivas y negativas para entender que es lo que impulsa la acción de preferencia en una relación de corto y largo plazo, ya que algunas emociones generan respuestas a corto y otras a largo. 

La fórmula del NEV es: 
nev = total de emociones positivas - total de emociones negativas 

Digamos que hicimos los cálculos de todas las emociones ingresadas por el usuario—por referencia ver principal.py—y obtenemos un total de 18 emociones positivas contra 7 emociones negativas: 
""" 
total_emociones_pos = 18 
total_emociones_neg = 7 
nev = total_emociones_pos - total_emociones_neg 
print("Tu valor emocional neto del dìa es: " + str(nev)) 

""" 
Informarte si las proporciones nutricionales que tuviste en el día es lo ideal:
Digamos que calculamos por una serie de procesos complejos utilizando la teoría del curso, las kilocalorías que el usuario idealmente debería consumir en un día, eso es, digamos, 2200 kilocalorías 
""" 
kilocalorias_ideales_al_dia = 2200 

# Proporciones nutricionales recomendadas 
porcentaje_carbohidratos = 0.55 
porcentaje_grasas = 0.30 
porcentaje_proteinas = 0.15 

proteinas_g = (calorias_ideales_al_dia * porcentaje_proteinas) / 4 #1 gramo de proteína = 4 kilocalorías 
carbohidratos_g = (calorias_ideales_al_dia * porcentaje_carbohidratos) / 4 #1 gramo de carbohidrato = 4 kilocalorías 
grasas_g = (calorias_ideales_al_dia *porcentaje_grasas) / 9 #1 gramo de grasa = 9 kilocalorías 

print(f"Gramos de proteínas recomendadas: {proteinas_g} g") 
print(f"Gramos de carbohidratos recomendados: {carbohidratos_g} g") 
print(f"Gramos de grasas recomendadas: {grasas_g} g") 

"""
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
#Ambición final: Al final me gustaría correlacionar con el coeficiente de correlación los cuatro cálculos de cada ejemplo de arriba mostrado y crear una gráfica en el archivo de texto o generar una imagen que muestre lo dicho. 
