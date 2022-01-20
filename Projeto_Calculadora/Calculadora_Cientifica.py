'''Mini Cauculadora com layout'''

import PySimpleGUI as sg

# Declarando Layout Da Janela

class TelaPython:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Primeiro Valor:'),sg.Input(size=(10,1),key='n1')],
            [sg.Text('Segundo valor:'),sg.Input(size=(10,1),key='n2')],
            [sg.Slider(range=(0,20),default_value=0,key='slider',orientation='h',size=(20,20))],
            [sg.Button('Somar',key='Somar'), sg.Button('Subtrair',key='Subtrair'), sg.Button('Multiplicar',key='Multiplicar'), sg.Button('Dividir',key='Divisao')],
            [sg.Output(size=(30,6),key='saida')],
            [sg.Button('Sair',key='Sair')]
        ]
        
        #Definindo Janela
        
        self.janela = sg.Window("Trabalhando Com Numeros").layout(layout)
    
    def Iniciar(self):
        while True:
            
            #Extraindo dados
            
            self.button, self.values = self.janela.Read()
            
            #Tratando erros
            
            try:
                n1 = float(self.values['n1'])
                n2 = float(self.values['n2'])
            except:
                print('VALOR DIGITADO INVALIDO! ')
            else:
                
                #Verificando botao clicado
                
                if self.button == 'Somar':
                    self.soma = float(self.values['n1']) + float(self.values['n2'])
                    print(f'{self.values["n1"]} + {self.values["n2"]} = {round(self.soma, int(self.values["slider"]))}')

                elif self.button == 'Subtrair':
                    self.subtracao = float(self.values['n1']) - float(self.values['n2'])
                    print(f'{self.values["n1"]} - {self.values["n2"]} = {round(self.subtracao, int(self.values["slider"]))}')

                elif self.button == 'Multiplicar':
                    self.multiplicacao = float(self.values['n1']) * float(self.values['n2'])
                    print(f'{self.values["n1"]} X {self.values["n2"]} = {round(self.multiplicacao, int(self.values["slider"]))}')

                elif self.button == 'Divisao':
                    self.divisao = float(self.values['n1']) / float(self.values['n2'])
                    print(f'{self.values["n1"]} / {self.values["n2"]} = {round(self.divisao, int(self.values["slider"]))}')

            if self.button == 'Sair':
                break
            if self.button == None:
                break

#Declarando instancia da classe

tela = TelaPython()

#iniciando a tela

tela.Iniciar()