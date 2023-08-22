# Chute um número até acertar!
# Objetivo: Criar um programa que faça com que lhe diga se está perto ou longe de acertar o número correto de 1 a 100
# Implementações para informar o máximo de tentativas é válido.

import random

import PySimpleGUI as sg

class ChuteUmNumero():
    #Lista de métodos
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

        # O Self serve para guardar informações dentro da classe.

    def iniciar(self):

        #layout
        layout = [
            [sg.Text('Chute um número: ', size=(20,0))],
            [sg.Input(size=(18,0), key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(20,10))]
        ]

        # janela
        self.janela = sg.Window('Chute o numero!',layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                # lendo os valores
                self.evento, self.valores = self.janela.Read()
                # funcionalidade
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo!')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais alto!')
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('PARABÉNS VOCÊ ACERTOU!!')
                            break
        except:
            print('Favor digitar apenas números!')
            self.Iniciar()
            

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio =  random.randint(self.valor_minimo,self.valor_maximo)

chute = ChuteUmNumero()
chute.Iniciar()