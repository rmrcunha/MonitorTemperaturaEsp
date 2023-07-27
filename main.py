import AMG8833
import firebase
import machine
from machine import Pin
import network
import onewire
import time
import utime

def pegaTemp(timer):
    data8x8 = amg.pixel()
    print(str(data8x8))
    firebase.push(URL,str(data8x8))
    print('Enviando temp')
    gc.collect()
    

def dsx(pino):
    dat = machine.Pin(pino)
    ow = onewire.OneWire(dat)
    global ds
    ds = ds18x20.DS18X20(ow)
    global roms
    roms = ds.scan()

def prova():
    return ds.read_temp(roms[0])

timer = machine.Timer(0)

def E(pino):
    v = machine.Pin(pino, machine.Pin.OUT)
    v.value(1)
    print('Pino {pino} utilizado como alimentação!');

E(18)

sda_pin = machine.Pin(21)
scl_pin = machine.Pin(22)

i2c = machine.I2C(scl = scl_pin,sda = sda_pin)

devices = i2c.scan()
if len(devices) > 0:
    print("Dispositivos I2C encontrados:")
    for device in devices:
        print(hex(device))
else:
    print("Nenhum dispositivo I2C encontrado.")

amg = AMG8833.AMG8833(i2c, addr = 0x69)

timeout = 0

wlan = network.WLAN(network.STA_IF)

def restartWlan():
    wlan.active(False)
    time.sleep(0.5)
    wlan.active(True)

restartWlan()
nomeRede =''
senhaRede = ''
wlan.connect(nomeRede,senhaRede)
URL = 'monitordetemperatura-ab3b0-default-rtdb/Paciente'

if not wlan.isconnected():
    print('conectando...')
    while (not wlan.isconnected() and timeout < 5):
        print(5-timeout)
        timeout = timeout + 1
        time.sleep(1)
    

if wlan.isconnected():
    print('Conectado em' + str(wlan.ifconfig()) + ' às ' + str(time.localtime()))

    timer.init(period=10000, mode=machine.Timer.PERIODIC, callback=pegaTemp)
    timer.init(period=10000, mode=machine.Timer.PERIODIC, callback=prova)
    
else:
    print('Time out')
    print('reiniciando')
    machine.reset()

