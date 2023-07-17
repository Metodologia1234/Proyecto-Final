#Importancion de librerias
from grovepi import *
from grove_rgb_lcd import *
from time import sleep
from math import isnan
import datetime
import time
import grovepi
import csv

#Puertos de conexiones
dht_sensor_port = 3 #D3
dht_sensor_type = 0 
light_sensor = 0 #A0
potentiometer = 1 #A1

grovepi.pinMode(light_sensor,"INPUT") #Lectura del sensor de luz
grovepi.pinMode(potentiometer,"INPUT") #Lectura de la resistencia del potencion metro


setRGB(0,255,0)



def escribir_matriz_en_csv(tabla, nombre_archivo):
            with open(nombre_archivo, 'w', newline='') as archivo_csv:
                escritor_csv = csv.writer(archivo_csv)
                escritor_csv.writerow(archivo_csv)
    
            print("Datos escritos en", nombre_archivo)
    
while True:
    try:            
        tiempo_actual=datetime.datetime.now().now()
        
        nombre_archivo_csv = 'datos.csv'
    
        a=1
    
        sensor_value_potencion = grovepi.analogRead(potentiometer)
    
        sensor_value = grovepi.analogRead(light_sensor)

        resistance = (float)(1023 - sensor_value) * 68 / sensor_value
    
        intensidad = ((253-resistance)/23)*10
    
        [temp,hum,] = dht(dht_sensor_port,dht_sensor_type)
        
        if isnan(temp) is True or isnan(hum) is True:
            raise TypeError('nan error')
        
        if (1023>sensor_value_potencion) and (sensor_value_potencion>818.4):
            a=1
        elif (818.4>sensor_value_potencion) and (sensor_value_potencion>613.8):
            a=2
        elif (613.8>sensor_value_potencion) and (sensor_value_potencion>409.2):
            a=3
        elif (409.2>sensor_value_potencion) and (sensor_value_potencion>204.6):
            a=4
        elif (204.6>sensor_value_potencion):
            a=5

        t = str(temp)
        h = str(hum)
        i = str(intensidad)
        ts= str(a)
        hora=str(tiempo_actual)

        setText_norefresh("T:" + t + "% " + "t:" + ts + "s" + "\n" + "H:" + h + "% " + "L:" + i + "%")
        
        tabla=[
            [hora, t, h, i]
            ]
        
        vector=[]
        
        for i in range(5):
            vector.append(tabla)
            
        print("Matriz:")
        
        for fila in tabla:
            print(fila)
    
    except (IOError, TypeError) as e:
        print(str(e))
        setText("")

    except KeyboardInterrupt as e:
        print(str(e))
        setText("")
        break
    sleep(a)