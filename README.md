Bienvenido al procesador de imágenes

Al ejecutar el procesador, primero pon el nombre de tu proyecto y la ruta de la imagen que usarás.
Una vez que lo hagas, se desplegará el menú donde podrás elegir entre 27 opciones, cada una marcada con un número entre 0 y 26.
Las opciones de 0 a 15 son acciones que podrás realizar en la imagen las cuales son:

0: Filtro negativo.

1: Filtro pixelado el cuál requiere un número entre 2 y 50.

2: Dibujar un círculo que requiere de una coordenada x, una coordenada y, el radio y el color a elegir.

3: Filtro de oscurecimiento.

4: Filtro de iluminación.

5: Filtro gris.

6: Reemplazar un color con otro de tu elección. Los colores a elegir son rojo, verde, azul, amarillo, naranja y púrpura.

7: Fusionar la imagen con otra. Se le pedirá la ruta de la segunda imagen.

8: Unir dos imágenes. Se le pedirá la ruta de la segunda imagen y la forma de la unión que puede ser right(una al lado de otra) o bottom(una debajo de la otra).

9: Resaltar un color de tu elección. Los colores a elegir son rojo, verde, azul, amarillo, naranja y púrpura.

10: Escribir texto. Se le pedirá coordenadas x e y, tamaño, color y el texto que desea escribir.

11: Dibujar una línea. Se le pedirá coordenadas tanto iniciales como finales de x e y, color y ancho.

12: Dibujar rectángulo. Se le pedirá coordenadas tanto iniciales como finales de x e y, y color.

13: Marca de agua con otra imagen. Se le pedirá la ruta de la segunda imagen.

14: Dibujar estrella. Se le pedirá coordenadas x e y, tamaño y color.

15: Fusionar la mitad de la imagen con la mitad de otra imagen. Se le pedirá la ruta de la segunda imagen.

Las opciones 16 a 25 involucran los datos del proyecto:

16: Crea un nuevo proyecto que requiere nombre de este y ruta de la imagen que desea usar.

17: Muestra el estado actual del proyecto.

18: Guarda el proyecto como imagen. Se le pedirá la ruta en donde desea guardarla.

19: Guarda el proyecto en sí con el nombre de este.

20: Carga el proyecto guardado. Se le pedirá el nombre del proyecto.

21: Deshace acciones realizadas al proyecto.

22: Perimite ver el historial.

23: Cambia de un proyecto a otro. Se le pedirá el nombre del proyecto al que desea ingresar.

24: Guarda el historial del proyecto como script en un archivo JSON.

25: Abre un script en un archivo JSON y ejecuta las acciones en el proyecto.

26: Salir del procesador

Ten en cuenta que cuando se le pida un color, el nombre de este debe ser en inglés.

También puede crear archivos en JSON a mano para poder cargarlos en el proyecto con el siguiente formato:

-El archivo debe ser una lista que empieza y termina con estos paréntesis: [].

-Dentro de la lista se definirá cada acción como un diccionario que empieza y termina con {}.

-En cada diccionario el nombre de la acción debe ser definido como '__type__', sus parámetros también deben definirse si es necesario. (Tenga en cuenta que si 'type' está en comillas, es porque tiene dos guiones bajos
por atrás y adelante. Asegúrese de que estén los guiones bajo al escribir el archivo)

-El formato para cada acción es el siguiente:

*Negativo: {'__type__':'Negative'}

*Pixelado: {'__type__':'Pixel', 'num': número entre 2 y 50}

*Circulo: {'__type__': 'Circle', 'x': coordenada x, 'y': coordenada y, 'r': número de tamaño del radio, 'color': 'nombre del color'}

*Oscurecer: {'__type__': 'Darken'}

*Iluminar: {'__type__':'Illuminate'}

*Gris: {'__type__' :'Grey'}

*Reemplazar: {'__type__': 'Replace', 'color': 'nombre de color', 'color2': 'nombre de color'}

*Fusionar: {'__type__': 'Fusion', 'filename2': 'ruta de segunda imagen'}

*Unir: {'__type__':'Union', 'filename2': 'ruta de segundo imagen', 'form': 'right o bottom'}

*Destacar: {'__type__': 'Highlight', 'color': 'nombre de color'}

*Texto: {'__type__': 'Text', 'x': coordenada x, 'y': coordenada y, 's': numero del tamaño del texto, 'color': 'nombre de color', 'st': 'texto'}

*Linea: {'__type__': 'Line', 'x': coordenada x, 'y': coordenada y, 'x2':coordenada x2, 'y2': coordenada y2, 'color': 'nombre de color', 'wdh': numero de ancho}

*Rectángulo: {'__type__': 'Rectangle', 'x': coordenada x, 'y': coordenada y, 'x2':coordenada x2, 'y2': coordenada y2, 'color': 'nombre de color'}

*Watermark: {'__type__': 'Watermark', 'filename2': 'ruta de segunda imagen'}

*Estrella: {'__type__':'Star', 'x': coordenada x, 'y': coordenada y, 'size': numero de tamaño, 'color': 'nombre de color'}

*Mitad y Mitad: {'__type__': 'CutRightLeft', 'filename2': 'ruta de segunda imagen'}

*Ejemplo de lista con diccionarios: [{'__type__': 'Watermark', 'filename2': 'ruta de segunda imagen'},
{'__type__':'Star', 'x': coordenada x, 'y': coordenada y, 'size': numero de tamaño, 'color': 'nombre de color'}]

-También se puede escribir en la lista el nombre de un archivo JSON ya existente que cumpla con el formato.

*Ejemplo: [{'__type__' :'Grey'},'nombre del archivo']

