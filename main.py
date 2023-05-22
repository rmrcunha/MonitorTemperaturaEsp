import network
import time
import machine
from machine import Pin
import firebase


timeout = 0

#horaAtual = time.localtime(time.time() + ajustaHora)




wlan = network.WLAN(network.STA_IF)

#Restart wlan
wlan.active(False)
time.sleep(0.5)
wlan.active(True)
nomeRede ='iPhone'
senhaRede = '10flecas'
wlan.connect(nomeRede,senhaRede)

if not wlan.isconnected():
    print('connecting...')
    while (not wlan.isconnected() and timeout < 5):
        print(5-timeout)
        timeout = timeout + 1
        time.sleep(1)

if wlan.isconnected():
    print('Connected in' + str(wlan.ifconfig()) + ' at ' + str(time.localtime()))
    led = machine.Pin(25,Pin.OUT)
    led.value(1)
    URL = 'monitordetemperatura-ab3b0-default-rtdb/Paciente'
    
else:
    print('Time out')
    print('reiniciando')
    machine.reset()






