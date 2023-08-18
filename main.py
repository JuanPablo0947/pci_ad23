print("Tecnológico de Monterrey\n")
print("Bienvenido al curso de Pensamiento Computacional para Ingeniería\n")
print("\tAtemtamemte: Los Profesores")
print(
    "Tecnológico de Monterrey\n\nBienvenido al curso de Pensamiento Computacional para Ingeniería\n\n\tAtemtamemte: Los Profesores"
)

print("Bye")

#Funciones auxiliares
def largest_width(array):
    largest = -1
    for i in array:
        if (len(i) > largest):
            largest = len(i)
            answer = i
    return len(answer)


def generate_spaces(num):
    string = ""
    for i in range(num + 1):
        string = string + " "
    return string


printable_file = open("Diario.txt", "w")

fecha = input("Fecha: ")
printable_file.write(fecha + ",")

dia = input("Día: ")
printable_file.write(" " + dia + ",")

hora = input("Hora: ")
printable_file.write(" " + hora + ".\n\n\n")

temp = input("¿Desayunaste? ")
if (temp == "Si" or temp == "si" or temp == "SI" or temp == "sI"):
    descripcion_desa = input("¿Qué desayunaste? ")
    printable_file.write("Desayuno:\n" + descripcion_desa + "\n\n\n")
temp = input("¿Comiste? ")
if (temp == "Si" or temp == "si" or temp == "SI" or temp == "sI"):
    descripcion_comi = input("¿Qué comiste? ")
    printable_file.write("Comida:\n" + descripcion_comi + "\n\n\n")
temp = input("¿Cenaste? ")
if (temp == "Si" or temp == "si" or temp == "SI" or temp == "sI"):
    descripcion_cena = input("¿Qué cenaste? ")
    printable_file.write("Cena:\n" + descripcion_cena + "\n\n\n")

temp = int(input("¿Cuántos snacks tuviste? Pon cero si no tuviste ninguno: "))
if (temp > 0):
    snacks = []
    for i in range(1, temp + 1):
        snacks.append(input(f"¿Qué cenaste en el snack {i}? "))
        printable_file.write(f"Snack {i}:\n" + snacks[i - 1] + "\n\n\n")

emociones = []
print(
    "Enlista las emociones o sentimientos que tuviste el día de hoy. Por cada emoción o sentimiento escrito da un enter. Al finalizar, solo da un enter final sin escribir nada más. ")
temp = input("Guarda tu emoción o sentimiento: ")
while (temp != ""):
    emociones.append(temp)
    temp = input("Guarda tu emoción o sentimiento: ")
for i in emociones:
    emociones[emociones.index(i)] = [i, input(f"¿Por qué te sentiste {i}? ")]
emociones.insert(0, ["Emociones", "Razón"])

first_column = []
for i in range(0, len(emociones)):
    first_column.append(emociones[i][0])
largest_width = largest_width(first_column)

string = ""
for i in range(largest_width):
    string = string + " "

for row in range(len(emociones)):
    if (len(emociones[row][0]) == largest_width):
        printable_file.write(' '.join([str(a) for a in emociones[row]]) + '\n')
    elif (len(emociones[row][0]) < largest_width):
        printable_file.write(
            generate_spaces(largest_width - len(emociones[row][0])).join([str(a) for a in emociones[row]]) + '\n')
printable_file.write("\n\n")

final_description = input("Sientete libre de escribir lo que quieras (recomendado para desahogarte): ")
final_des = [(final_description[i:i + 54]) for i in range(0, len(final_description), 54)]
printable_file.write("Descripción:\n")
for i in final_des:
    printable_file.write(i + "\n")

printable_file.close()
