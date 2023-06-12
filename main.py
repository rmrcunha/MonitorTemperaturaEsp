import network
import time
import machine
from machine import Pin
import firebase
import AMG8833

""""
função para definir pino como alimentação
"""
def E(pino):
    v = machine.Pin(pino, machine.Pin.OUT)
    v.value(1)

E(18)
print('3v3 ligado')

"""
    azul = sda
    proto 14
"""
sda_pin = machine.Pin(21)
"""
    amarelo = scl
    proto 17
"""
scl_pin = machine.Pin(22)

i2c = machine.I2C(scl = scl_pin,sda = sda_pin)
print('i2c feito')

#Verifica se há dispositivos i2c
devices = i2c.scan()
if len(devices) > 0:
    print("Dispositivos I2C encontrados:")
    for device in devices:
        print(hex(device))
else:
    print("Nenhum dispositivo I2C encontrado.")

#inicializa o AMG8833
amg = AMG8833.AMG8833(i2c, addr = 0x69)


timeout = 0

#horaAtual = time.localtime(time.time() + ajustaHora)




wlan = network.WLAN(network.STA_IF)

#Restart wlan
wlan.active(False)
time.sleep(0.5)
wlan.active(True)
nomeRede ='Cunha Oi Fibra'
senhaRede = '26160903'
wlan.connect(nomeRede,senhaRede)

if not wlan.isconnected():
    print('connecting...')
    while (not wlan.isconnected() and timeout < 5):
        print(5-timeout)
        timeout = timeout + 1
        time.sleep(1)

if wlan.isconnected():
    print('Connected in' + str(wlan.ifconfig()) + ' at ' + str(time.localtime()))
    URL = 'monitordetemperatura-ab3b0-default-rtdb/Paciente'
    
    while True:
        # Leitura dos valores da matriz 8x8
        data8x8 = amg.pixel()
        firebase.push(URL, str(data8x8))
        print('Envaido temp')
        time.sleep(120)
    
else:
    print('Time out')
    print('reiniciando')
    machine.reset()






