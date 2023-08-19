# pci_ad23
Repo para almacenar los ejercicios y ejemplos de clase de "Pensamiento Computacional para Ingeniería". Semestre AD23

# TC1028.411 Proyecto de Juan Pablo R.

Conforme la construcción de este proyecto, se aplicara el estilo del standard y convención PEP8, y de las buenas prácticas de industria vistos a lo largo del curso.

En los comentarios dentro de cada función, entre parentesis, vienen las subcompetencias que demuestra esa función o ese conjunto de funciones.

¡Espero te sea de ayuda! :D

# [](https://github.com/JuanPablo0947/pci_ad23#diario-nutricional)[](https://github.com/JuanPablo0947/pci_ad23#diario-nutricional)Diario Nutricional

### [](https://github.com/JuanPablo0947/pci_ad23#contexto)[](https://github.com/JuanPablo0947/pci_ad23#contexto)Contexto

Este programa es para llevar un seguimiento de lo solicitado en la actividad LiFE Nutrición y bienestar en la vida profesional con código KWEL3012. Para complementar, el diario nutricional, tiene por objetivo evaluar cómo las emociones afectan la nutrición integral (i.e., dormir, higiene, alimentación, salud mental, etc.) del escritor por medio de la recaudación de la información siguiente:

-   Emociones o sentimientos
-   alimentos ingeridos
-   horas de sueño
-   información libre (¡la que tú quieras agregar!)

Poco a poco te iras dando cuenta que hay patrones entre lo que comes y como te nutres.

Te recomendamos que cuando te pregunten tus emociones, no pongas bien o mal, en cambio escribe emociones reales como felicidad, entusiasmo, euforia, estrés, etc.

Adicionalmente, a parte que el programa corre en terminal con Python 3, el código del programa tendrá comentarios de cómo funciona cada parte e inclusive linea del programa.

El programa presenta una serie de preguntas y lo termina almacenando en variables temporales para después comparar cada entrada con lo esperado para la toma de decisión de saber a donde canalizar el programa; en otras palabras, para ciertas preguntas, lo que escribas va afectar lo que te pregunten después. Al final, te generara un análisis de la información recabada y recomendaciones al respecto. De igual manera, le permite al usuario archivar todo lo ingresado mediante el programa generando un archivo de texto para que lo puedas imprimir y anexar en tus notas para discutirlo con tus compañeros y maestra el siguiente día de clase.

Sin nada mas, espero que lo disfrutes profesor y quizás te sea de utilidad.

### [](https://github.com/JuanPablo0947/pci_ad23#instrucciones)[](https://github.com/JuanPablo0947/pci_ad23#instrucciones)Instrucciones

Descargar el archivo y correr en terminal con:

```
python diario.py

```

o abrir en tu IDE y dale el boton de play.

Responder a las preguntas que aparecen, el programa tiene instrucciones y no usa bibliotecas no standard.

### [](https://github.com/JuanPablo0947/pci_ad23#instrucciones)[](https://github.com/JuanPablo0947/pci_ad23#pseudocódigo)Pseudicódigo

**Entrada**

**Proceso**

 1. Crear función "largest width" con un parametro de tipo arreglo con la siguiente acción:
 1.1 Identifica y almacena en una variable llamada Respuesta la palabra con más caracteres en el arreglo
 1.2 Devolver Respuesta
 
 2. Crear función "generate spaces" con un parametro entero con la siguiente acción:
	 2.1 Asignar un string vacio a la variable String
	 2.1 Repetir de cero hasta parametro + 1 la concatenación de un espacio a String.
	 
 3. A la variable "printable file" asignar un objecto archivo de texto con modo de escritura/write.
 4. Pedir al usuario la fecha de hoy y asignarlo a la variable de texto "fecha".
 5. Escribir en la variable "printable file" el valor de la variable "fecha".
 6. Pedir al usuario el día de hoy y asignarlo a la variable de texto "dia".
 7. Escribir en la variable "printable file" el valor de la variable "dia".
 8. Pedir al usuario la hora de hoy y asignarlo a la variable de texto "hora".
 9. Escribir en la variable "printable file" el valor de la variable "hora".
 10. Pedir al usuario que diga si desayuno o no y asignarlo en la variable "temp"  
 11. Si el valor de la variable "temp" es igual a "Si", "si", "SI", o "sI", entonces: 
 11.1 Pedir al usuario que diga qué fue lo que desayuno y asignarlo a la variable "descripción desayuno"  
 11.2 Escribir en la variable "printable file" el valor de la variable "descripción desayuno" con saltos de línea antes y después del valor de "descripción desayuno"
 12. Pedir al usuario que diga si comió o no y asignarlo en la variable "temp"  
 13. Si el valor de la variable "temp" es igual a "Si", "si", "SI", o "sI", entonces: 
 13.1 Pedir al usuario que diga qué fue lo que comió y asignarlo a la variable "descripción comi"  
 13.2 Escribir en la variable "printable file" el valor de la variable "descripción comi" con saltos de línea antes y después del valor de "descripción comi"
 14. Pedir al usuario que diga si ceno o no y asignarlo en la variable "temp"  
 15. Si el valor de la variable "temp" es igual a "Si", "si", "SI", o "sI", entonces: 
 15.1 Pedir al usuario que diga qué fue lo que ceno y asignarlo a la variable "descripción cena"  
 15.2 Escribir en la variable "printable file" el valor de la variable "descripción cena" con saltos de línea antes y después del valor de "descripción cena"
 16. Pedir al usuario que escriba la cantidad de snacks que tuvo, poniendo cero si no aplica, y asignar lo pedido a la variable "temp".
 17. Si el valor de la variable "temp" es mayor a cero, entonces:
 17.1 Crear la variable "snacks" y asignar un arreglo vació al mismo.
 17.2 Repetir de uno hasta "temp" + 1 el pedir lo que ceno el usuario en el snack correspondiente y agregar hasta el final de la lista "snacks" su entrada/input.
 17.3 Escribir en la variable "printable file" el valor recientemente agregado a la lista de "snacks" con saltos de línea antes y después del valor de "snacks"
 
 18. Crear la variable "emociones" y asignar un arreglo vació al mismo.
 19. Escribir en pantalla las indicaciones de como ingresar las emociones. 
 20. Pedir al usuario que solo escriba una emoción y después de un enter, para asignarlo a la variable "temp".
 21. Mientras el usuario no ingrese nada mas que un enter, entonces:
 21.1 Agregar hasta el final de la lista "emociones" el valor de la variable "temp".
 21.2 Pedir al usuario que solo escriba una emoción y después de un enter, para asignarlo a la variable "temp".
 
 22. Ciclar por cada elemento del arreglo "emociones" y remplazar el valor de cada elemento por un arreglo que tiene como primer elemento la emoción/valor del elemento a remplazar y un segundo elemento que es el input del usuario describiendo la razón de por qué se siente así. 





**Salida**
