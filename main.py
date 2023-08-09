import AMG8833
import firebase
import machine
from machine import Pin
import network
import onewire
import time
import ds18x20
import utime
import gc

dat = machine.Pin(16)
sda_pin = machine.Pin(21)
scl_pin = machine.Pin(22)

def E(pino):
    v = machine.Pin(pino, machine.Pin.OUT)
    v.value(1)
    print('Pino ' + str(pino) + ' utilizado como alimentação!');

E(18)

def pegaTemp():
    print('Infravermelho acionado')
    data8x8 = amg.pixel()
    print(str(data8x8))
    #firebase.push(URL + "/temp8x8" ,str(data8x8))
    print('Enviando temp')
    
def init_ds18b20():
    ow = onewire.OneWire(dat)
    ds = ds18x20.DS18X20(ow)
    roms = ds.scan()
    return ds, roms

def read_temperature(ds, rom):
    ds.convert_temp()
    time.sleep_ms(750)
    return ds.read_temp(rom)

ds, roms = init_ds18b20()

def proof():
    print('ds18b20 acionado')
    for rom in roms:     
        temperature = read_temperature(ds, rom)
        print('Temperatura:', str(temperature), 'ºC')
        #firebase.push(URL + "/prova", str(temperature))
        gc.collect()

timer = machine.Timer(0)

def callbackTemps(timer):
    pegaTemp()
    proof()

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
    print('Definindo wlan')
    wlan.active(False)
    time.sleep(0.5)
    wlan.active(True)

restartWlan()
nomeRede ='CunhaClaro'
senhaRede = '26160903'
wlan.connect(nomeRede,senhaRede)
URL = 'monitordetemperatura-ab3b0-default-rtdb/Paciente'

if not wlan.isconnected():
    print('conectando em ' + nomeRede + '...')
    while (not wlan.isconnected() and timeout < 5):
        print(5-timeout)
        timeout = timeout + 1
        time.sleep(1)
    
if wlan.isconnected():
    print('Conectado em' + str(wlan.ifconfig()) + ' às ' + str(time.localtime()))

    timer.init(period=1000, mode=machine.Timer.PERIODIC, callback=callbackTemps)
    
    while True:
        gc.collect()
        print('Lixo coletado')

else:
    print('Time out')
    print('reiniciando')
    machine.reset()
