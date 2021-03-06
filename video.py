import cv2

def capturarVideo():

    """Se selecciona la camara a utilizar, en este caso al ser una sola, se utiliza el valor 0"""
    camara = cv2.VideoCapture(0)

    #Se Establece resolucion del video en 320x240
    camara.set(3, 320)
    camara.set(4, 240)

    if not camara.isOpened():
        print("No se puede abrir la camara")

    return camara

#-----------------------------------------OBTENER VIDEO-----------------------------

def obtenerVideo(camara):
    """Una vez obtenida la camara de donde se va a obtner el video, debemos obtener cada uno de
       los frames para dar inicio al procesamiento en tiempo real."""
    val, frame = camara.read()
    return val, frame

def mostrarVideo(nombre,frame):
    """Muestra en pantalla el video obtenido"""
    cv2.imshow(nombre, frame)