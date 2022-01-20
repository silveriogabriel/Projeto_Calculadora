'''
    Calculadora Python By: GABRIEL SILVÉRIO
'''

import PySimpleGUI as sg
import re

#Definindo classe 
class Calculadora:
    def __init__(self):
        #layout
        layout = [
            [sg.Output(size=(29,1))],
            [sg.Button('C', size=(12,2), key=('apaga')), sg.Button('%', size=(5,2)), sg.Button('/',size=(5,2))],
            [sg.Button('7', size=(5,2)), sg.Button('8', size=(5,2)), sg.Button('9',size=(5,2)), sg.Button('*', size=(5,2))],
            [sg.Button('4', size=(5,2)), sg.Button('5', size=(5,2)), sg.Button('6',size=(5,2)), sg.Button('-', size=(5,2))],
            [sg.Button('1', size=(5,2)), sg.Button('2', size=(5,2)), sg.Button('3',size=(5,2)), sg.Button('+', size=(5,2))],
            [sg.Button('0', size=(12,2)), sg.Button('.', size=(5,2)), sg.Button('=',size=(5,2))]
      ]
        self.numeros = []
        self.valor = 0
        self.numero = ''
        #Definindo Janela 
        self.janela = sg.Window('Calculadora').layout(layout)
    def iniciar(self):
        while True:
            self.Button, self.values = self.janela.Read()
            if self.Button == sg.WINDOW_CLOSED:
                break
            
            if self.Button in '0123456789':
                self.numero = self.numero + self.Button
                print(self.Button,end='')
            else:
                self.numeros.append(int(self.numero))
                self.numero = ''

            if self.Button == '+':
                if len(self.numeros) != 0 and self.numeros[-1] != '+' and self.numeros[-1] != '-' and self.numeros[-1] != '*' and self.numeros[-1] != '/' and self.numeros[-1] != '%' and self.numeros[-1] != 'apagar':
                    self.numeros.append('+')
            if self.Button == '-':
                if len(self.numeros) != 0 and self.numeros[-1] != '+' and self.numeros[-1] != '-' and self.numeros[-1] != '*' and self.numeros[-1] != '/' and self.numeros[-1] != '%' and self.numeros[-1] != 'apagar':
                    self.numeros.append('-')
            
            if self.Button == '/':
                if len(self.numeros) != 0 and self.numeros[-1] != '+' and self.numeros[-1] != '-' and self.numeros[-1] != '*' and self.numeros[-1] != '/' and self.numeros[-1] != '%' and self.numeros[-1] != 'apagar':
                    self.numeros.append('/')
            
            if self.Button == '*':
                if len(self.numeros) != 0 and self.numeros[-1] != '+' and self.numeros[-1] != '-' and self.numeros[-1] != '*' and self.numeros[-1] != '/' and self.numeros[-1] != '%' and self.numeros[-1] != 'apagar':
                    self.numeros.append('*')

            if self.Button == '%':
                if len(self.numeros) != 0 and self.numeros[-1] != '+' and self.numeros[-1] != '-' and self.numeros[-1] != '*' and self.numeros[-1] != '/' and self.numeros[-1] != '%' and self.numeros[-1] != 'apagar':
                    self.numeros.append('%')
            
            for i in self.numeros:
                print(i,end='')
            print()
            if self.Button == '=' and len(self.numeros) != 0:
                for i, v in enumerate(self.numeros):
                    if v == '+':
                        self.valor += self.numeros[i - 1] + self.numeros[i + 1]
                        self.numeros.pop()
                        self.numeros.pop()
                        self.numeros.pop()
                        print(self.valor)

            if len(self.numeros) != 0 and self.Button == 'apaga':
                self.numeros.pop()

CL = Calculadora()
CL.iniciar()