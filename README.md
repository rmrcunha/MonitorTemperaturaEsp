# MonitorTemperaturaEsp

1,8: importação de módulos

10,13: Criação da função pegaTemp():
        11: A função começa declarando a variavel data8x8 recebendo como valor amg.pixel()
            amg.pixel():
                Lê os dados enviados pelo sensor amg8833 começando no endereço 0x80(h). Retorna matriz 8x8 de números inteiros (dados em fahrenheit).
        12: Envio dos dados da matriz para a firebase utilizando o método firebase.push(URL,str(data8x8)).
        13: Confirmação.

15, 21: Criação da função dsx(pino):
                16:Variável dat: Recebe como valor machine.Pin(pino);
                17: Variável ow: Recebe como valor onewire.OneWire(dat):
                        onewire: Declara um barramento de fio único. Utilizado unicamente em dispositivos de baixo consumo energético.
                18:Variável global ds;
                19: Valor atribuído a ds: ds18x20.DS18X20(ow).
                20: Variável global roms;
                21: roms recebe como valor ds.scan()
                        ds.scan(): Retorna o dispositivo ds em um valor decimal começando por 0.

23,24: Criação da função prova():
                24: Retorna a medição do sensor(ds.read_temp(rom[0]))

26: Setando timer para 0.

28,31: Criação da função E(pino):
            Função para setar nível lógico alto em um de escolha livre tornando-o alimentação de qualquer componente.
            29: Variável v recebe machine.Pin(pino, machine.Pin.OUT).
            30: Setando o nível lógico alto no pino escolhido.
            31: Confirmação da escolha do pino e do funcionamento da função.

33: Chamando função E(pino)

35: Criação da variável sda_pin (Pino de dados).

36: Criação da variável scl_pin (Pino de clock).

38: Criação da variável i2c:
        Recebe como valor atribuído machine.I2C(scl = scl_pin, sda = sda_pin).

        "Explicação do que é i2c em: https://learn.sparkfun.com/tutorials/i2c/all#:~:text=Each%20I2C%20bus,Clock)%20is%20the%20clock%20signal. "

40: Cria variável devices:
        Recebe como parâmetro i2c.scan()
            i2c.scan():
                Método que retorna um array com os dispositivos I2C encontrados.

41,44: Condicional:
        Se a tamanho do array retornado por devices, for maior que zero - ou seja - caso existam dispositivos I2C conectados, entramos na condicional.
            30: Confirmação de que dispositivos I2C foram encontrados.
            31,32: Para cada dispositivo retornado pelo array devices, um id será atribuído (id hexadecimal).

45,46: Caso nenhum dispositivo I2C seja encontrado, uma mensagem informando o ocorrido será enviada.

48: Inicializa o sensor amg8833 com a variável amg.

50: Variável timeout criada com o valor 0.

52: Variável wlan criada:
    Valor atribuído: network.WLAN(network.STA_IF)-> STA_IF: Permite conectar a uma rede.

54,57:Função restartWlan:
        Reinicia o dispositivo de conexão para, se assegurando de configurá-lo de forma correta.(Não há problema utilizar o time.sleep pois o programa não pode continuar sem esta configuração).

59: Chamada da função restartWlan.

60: Variável nomeRede: recebe o ssid da rede.

61: Variável senhaRede: recebe a senha da rede.

62: wlan.connect(nomeRede,senhaRede): Conecta na rede. O método connect recebe como parâmetro nomeRede e senhaRede.

63: Interrupção: A cada 20 segundos a função pegaTemp() é chamada.

64: Interrupção: A cada 10 segundo a função prova() é chamada.

65, 73: Condicional: caso o dispositivo não esteja conectado a rede entraremos em um loop:
        55: loop que ocorre durante 5 segundos enquanto o dispositivo não está conectado a rede.
        61: Reinicia o dispositivo caso a conexão não tenha sido estabelecida, deste modo o código será executado novamente.

76, 78: Condicional: caso esteja conectado a rede, o dispositivo mostrará os detalhes da rede onde está conectado.
        78: Variável URL declarada: recebe o caminho do banco de dados para a postagem das medições.