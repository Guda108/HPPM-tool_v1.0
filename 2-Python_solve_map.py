import os
import matplotlib.pyplot as plt

# Ruta del archivo .exe a ejecutar
ruta_exe = "p_trayectoria.exe"

# Ruta del archivo de datos generado por el .exe
ruta_datos = "tray.txt"

# Ruta del archivo de obstáculos
ruta_obstaculos = "obstaculos1.txt"

# Número de veces que se ejecutará el archivo .exe
num_ejecuciones = 1

# Lista para almacenar los datos del archivo de texto
homotopy_path = []

# Lista para almacenar los obstáculos
obstaculos = []

for _ in range(num_ejecuciones):
    os.system(ruta_exe)

    # Leer el archivo de datos generado
    with open(ruta_datos, 'r') as archivo:
        lineas = archivo.readlines()
        
        # Extraer los datos de cada línea y almacenarlos en la lista
        for linea in lineas:
            elementos = linea.strip().split('\t')
            x = float(elementos[0])
            y = float(elementos[1])
            homotopy_path.append((x, y))

    # Leer el archivo de obstáculos
    with open(ruta_obstaculos, 'r') as archivo_obstaculos:
        lineas_obstaculos = archivo_obstaculos.readlines()
        
        # Extraer los datos de cada línea y almacenarlos en la lista de obstáculos
        for linea_obstaculo in lineas_obstaculos:
            elementos_obstaculo = linea_obstaculo.strip().split('\t')
            x_obstaculo = float(elementos_obstaculo[0])
            y_obstaculo = float(elementos_obstaculo[1])
            radio_obstaculo = float(elementos_obstaculo[2])
            obstaculos.append((x_obstaculo, y_obstaculo, radio_obstaculo))

# Graficar los datos y obstáculos
x_vals = [dato[0] for dato in homotopy_path]
y_vals = [dato[1] for dato in homotopy_path]

plt.scatter(x_vals, y_vals, color='blue', label='homotopy_path')

for obstaculo in obstaculos:
    x_obstaculo, y_obstaculo, radio_obstaculo = obstaculo
    circulo = plt.Circle((x_obstaculo, y_obstaculo), radio_obstaculo, color='red', fill=False)
    plt.gca().add_patch(circulo)


fig_image = plt.imread("Lab_5.jpg")
alto_px, ancho_px, _ = fig_image.shape
print("tamano=", alto_px, ancho_px)
plt.imshow(fig_image, extent=[0, ancho_px, 0, alto_px], aspect='auto', origin='lower')



plt.xlabel('X')
plt.ylabel('Y')
plt.title('Homotopy path')
plt.legend()
plt.show()


