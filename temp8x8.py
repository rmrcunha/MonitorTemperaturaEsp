import machine
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
print('amg inciado')
while True:
    # Leitura dos valores da matriz 8x8
    data8x8 = amg.pixel()

    # Imprimir os valores
    amg.print8x8(data8x8)
    print('**************************')
    time.sleep(30)