import machine
import onewire
import ds18x20
import time

# Configura o pino de dados do sensor
dat = machine.Pin(14)
print(1)
#sla
ow = onewire.OneWire(dat)
# Cria uma instância do barramento OneWire
ds = ds18x20.DS18X20(ow)
print(2)
# Pesquisa e obtém o endereço do sensor
roms = ds.scan()
print(3)
# Configura a resolução do sensor (9-12 bits)
#ds.resolution(roms[0], 12)
print(4)
while True:
    # Inicia a conversão de temperatura
    ds.convert_temp()

    # Aguarda a conversão (750ms para resolução de 12 bits)
    time.sleep_ms(750)

    # Lê a temperatura do sensor
    temp = ds.read_temp(roms[0])

    # Imprime a temperatura
    print("Temperatura: %.2f°C" % temp)

    # Aguarda 1 segundo antes de fazer a próxima leitura
    time.sleep(1)