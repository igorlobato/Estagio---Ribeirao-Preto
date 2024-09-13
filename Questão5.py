'''5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. 
Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. 
Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas
das lâmpadas, qual interruptor controla cada lâmpada?  '''

'''
Primeiro se deve ligar o primeiro interruptor e deixar a lâmpada esquentar, depois se liga o segundo e visita uma das salas, podendo
ocorrer os seguintes cenários
    1° A lâmpada da sala visitada está ligada
    2° Desligada e fria
    3° Desligada e quente

Caso a lâmpada esteja ligada, então já se sabe que o primeiro interruptor liga a lâmpada da sala selecionada, e basta visitar qualquer
outra sala para verificar se o segundo interruptor ligou a lâmpada dela ou não, matando assim a charada.

Apenas o segundo cenário se utiliza o mesmo jogo com os interruptores, pois já se sabe que o interruptor escolhido não liga a lâmpada
da sala escolhida, dessa forma, se repete o exato mesmo teste com as salas restantes.
'''