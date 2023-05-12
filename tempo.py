
import ntptime
import network
timeout = 0

led = machine.Pin(25,Pin.OUT)
led.value(1)

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
    print('Connected in' + str(wlan.ifconfig()))
    
else:
    print('Time out')
    print('reiniciando')



ajustaHora = -3 * 60 * 60
print("Local time before synchronization：%s" %str(time.localtime()))
#hora = time.localtime(time.time()+ajustaHora)
#print(hora) 
print("Local time after synchronization：%s" %str(time.localtime(time.time()+ajustaHora)))