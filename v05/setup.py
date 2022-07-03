from tkinter import StringVar
from os import system
from math import sin, cos, radians
from func_comum import roundF
import json


class SetUp:
    def __init__(self):
        self.res = -.005 #negativo para inverter as reguas
        
        self.guiSetUp()
        self.frameCoordSetUp()
        self.frameToolsSetUp()
        self.frameRefSetUp()
        self.frameAoRaioSetUp()
        self.frameADiagonalSetUp()
        self.frameSistemaSetUp()
        self.tecladoSetUp()
        self.alertaSetUp()

        #setup do sensor
        self.sensorSetUP()
        self.leituraLoop()


    #self.frame_coord# {{{
    def frameCoordSetUp(self):
        self.var_x_main = 0 #variavel principal, altera a posição de todas as referencias
        self.var_y_main = 0 #variavel principal, altera a posição de todas as referencias
        self.var_x_atual = 0
        self.var_y_atual = 0
        self.var_x_atual_view = StringVar()
        self.var_y_atual_view = StringVar()
        
        self.frame_coord.label_coord_x.configure(textvariable=self.var_x_atual_view)
        self.frame_coord.label_coord_y.configure(textvariable=self.var_y_atual_view)

        #coord list display
        self.var_coord_list_view = StringVar()
        self.var_coord_list = dict()
        self.var_history_view = '*'

        self.frame_coord.listbox.configure(
                listvariable = self.var_coord_list_view,
                yscrollcommand = self.frame_coord.scrool_list.set)

        self.frame_coord.scrool_list.configure(command = self.frame_coord.listbox.yview)

        #coord set/del buttons
        self.frame_coord.button_list_del.configure(command = self.delFromCoordList)
        self.frame_coord.button_list_set.configure(command = self.setFromCoordList)
# }}}


    #self.frame_tools# {{{
    def frameToolsSetUp(self):
        self.frame_tools.button_x_zero.configure(command = self.setXAtual)
        self.frame_tools.button_x_meio.configure(command = self.setXMeio)

        self.frame_tools.button_x_calc.configure(
                command = lambda : self.callTecladoCoord(self.var_x_atual_view, self.setXAtual, 'X : '))

        self.frame_tools.button_y_zero.configure(command = self.setYAtual) 
        self.frame_tools.button_y_meio.configure(command = self.setYMeio)

        self.frame_tools.button_y_calc.configure(
                command = lambda : self.callTecladoCoord(self.var_y_atual_view, self.setYAtual, 'Y : '))
# }}}


    #self.frame_ref# {{{
    def frameRefSetUp(self):
        self.frame_ref.button_referencia.configure(command=lambda : self.addCoordList('Ref'))
        self.frame_ref.button_centro.configure(command=lambda : self.addCoordList('Centro'))
        self.frame_ref.button_x.configure(command=lambda : self.addCoordList('XX'))
        self.frame_ref.button_y.configure(command=lambda : self.addCoordList('YY'))
        self.frame_ref.button_furo.configure(command=lambda : self.addCoordList('Furo'))
        self.frame_ref.button_rosca.configure(command=lambda : self.addCoordList('Rosca'))
        self.frame_ref.button_abilongo.configure(command=lambda : self.addCoordList('Abilon'))
        self.frame_ref.button_raio.configure(command=lambda : self.addCoordList('Raio'))
        self.frame_ref.button_diagonal.configure(command=lambda : self.addCoordList('Diagnl'))
        # }}}


    #self.frame_ao_raio# {{{
    def frameAoRaioSetUp(self):
        self.var_ao_raio_select = 0
        self.var_ao_raio_list = []
        self.var_ao_raio_furos = StringVar()
        self.var_ao_raio_raio = StringVar()
        self.var_ao_raio_desloc = StringVar()
        self.var_ao_raio_identificador = StringVar()

        self.var_ao_raio_furos.set('0')
        self.var_ao_raio_raio.set('0.0')
        self.var_ao_raio_desloc.set('0.0°')
        self.var_ao_raio_identificador.set('0/0')

        self.frame_ao_raio.button_furos.configure(
                command=lambda : self.callTecladoVar(self.var_ao_raio_furos, int, '', 'Furos : '))

        self.frame_ao_raio.button_raio.configure(
                command=lambda : self.callTecladoVar(self.var_ao_raio_raio, roundF, '', 'Raio : '))

        self.frame_ao_raio.button_desloc.configure(
                command=lambda : self.callTecladoVar(self.var_ao_raio_desloc, roundF, '°', 'Desloc : '))

        self.frame_ao_raio.label_furos_value.configure(textvariable=self.var_ao_raio_furos)
        self.frame_ao_raio.label_raio_value.configure(textvariable=self.var_ao_raio_raio)
        self.frame_ao_raio.label_desloc_value.configure(textvariable=self.var_ao_raio_desloc)
        self.frame_ao_raio.label_identificador.configure(textvariable=self.var_ao_raio_identificador)

        self.frame_ao_raio.button_calc.configure(command=self.calcRaio)
        self.frame_ao_raio.button_anterior.configure(command=lambda:self.raioListProximo(-1))
        self.frame_ao_raio.button_proximo.configure(command=lambda:self.raioListProximo(1))
        # }}}


    #self.frame_a_diagonal# {{{
    def frameADiagonalSetUp(self):
        self.var_a_diagonal_select = 0
        self.var_a_diagonal_list = []
        self.var_a_diagonal_furos = StringVar()
        self.var_a_diagonal_distancia = StringVar()
        self.var_a_diagonal_angulo = StringVar()
        self.var_a_diagonal_desloc = StringVar()
        self.var_a_diagonal_identificador = StringVar()

        self.var_a_diagonal_furos.set('0')
        self.var_a_diagonal_distancia.set('0.0')
        self.var_a_diagonal_angulo.set('0.0°')
        self.var_a_diagonal_desloc.set('0.0')
        self.var_a_diagonal_identificador.set('0/0')

        self.frame_a_diagonal.button_furos.configure(
                command = lambda : self.callTecladoVar(self.var_a_diagonal_furos, int, '', 'Furos : '))

        self.frame_a_diagonal.button_distancia.configure(
                command = lambda : self.callTecladoVar(self.var_a_diagonal_distancia, float, '', 'Distan : '))

        self.frame_a_diagonal.button_angulo.configure(
                command = lambda : self.callTecladoVar(self.var_a_diagonal_angulo, roundF, '°', 'Angulo : '))

        self.frame_a_diagonal.button_desloc.configure(
                command = lambda : self.callTecladoVar(self.var_a_diagonal_desloc, roundF, '', 'Desloc : '))

        self.frame_a_diagonal.label_furos_value.configure(textvariable=self.var_a_diagonal_furos)
        self.frame_a_diagonal.label_distancia_value.configure(textvariable=self.var_a_diagonal_distancia)
        self.frame_a_diagonal.label_angulo_value.configure(textvariable=self.var_a_diagonal_angulo)
        self.frame_a_diagonal.label_desloc_value.configure(textvariable=self.var_a_diagonal_desloc)
        self.frame_a_diagonal.label_identificador.configure(textvariable=self.var_a_diagonal_identificador)

        self.frame_a_diagonal.button_calc.configure(command=self.calcDiagonal)
        self.frame_a_diagonal.button_anterior.configure(command=lambda:self.diagListProximo(-1))
        self.frame_a_diagonal.button_proximo.configure(command=lambda:self.diagListProximo(1))
# }}}


    #self.frame_sistema# {{{
    def frameSistemaSetUp(self):
        self.frame_sistema.button_limpar_historico.configure(command=self.limparCoordList)
        self.frame_sistema.button_sair.configure(command=exit)
        self.frame_sistema.button_desligar.configure(command=exit)
        #self.frame_sistema.button_desligar.configure(command=lambda : system('shutdown now'))
        self.frame_sistema.button_salvar_historico.configure(command=self.salvaCoordList)
        self.frame_sistema.button_carregar_historico.configure(command=self.loadCoordList)
        self.frame_sistema.button_zero_x_main.configure(command=self.setXMain)
        self.frame_sistema.button_zero_y_main.configure(command=self.setYMain)

        self.frame_sistema.button_calc_x_main.configure(
                command = lambda : (self.callTecladoCoordMain(self.var_x_main, self.DeslocarXMain, 'Main X : ')))

        self.frame_sistema.button_calc_y_main.configure(
                command = lambda : (self.callTecladoCoordMain(self.var_y_main, self.DeslocarYMain, 'Main Y : ')))
        # }}}


#self.frame_teclado# {{{
    def tecladoSetUp(self):
        self.frame_teclado.var_label = StringVar()
        self.frame_teclado.label_numeral.configure(textvariable=self.frame_teclado.var_label)
        self.frame_teclado.var_formula = ''

        self.frame_teclado.button_c.configure(command=lambda:self.addTecladoVar('c'))

        self.frame_teclado.button_9.configure(command=lambda:self.addTecladoVar('9'))
        self.frame_teclado.button_8.configure(command=lambda:self.addTecladoVar('8'))
        self.frame_teclado.button_7.configure(command=lambda:self.addTecladoVar('7'))
        self.frame_teclado.button_div.configure(command=lambda:self.addTecladoVar('/'))

        self.frame_teclado.button_6.configure(command=lambda:self.addTecladoVar('6'))
        self.frame_teclado.button_5.configure(command=lambda:self.addTecladoVar('5'))
        self.frame_teclado.button_4.configure(command=lambda:self.addTecladoVar('4'))
        self.frame_teclado.button_vz.configure(command=lambda:self.addTecladoVar('*'))

        self.frame_teclado.button_3.configure(command=lambda:self.addTecladoVar('3'))
        self.frame_teclado.button_2.configure(command=lambda:self.addTecladoVar('2'))
        self.frame_teclado.button_1.configure(command=lambda:self.addTecladoVar('1'))
        self.frame_teclado.button_menos.configure(command=lambda:self.addTecladoVar('-'))

        self.frame_teclado.button_0.configure(command=lambda:self.addTecladoVar('0'))
        self.frame_teclado.button_ponto.configure(command=lambda:self.addTecladoVar('.'))
        self.frame_teclado.button_mais.configure(command=lambda:self.addTecladoVar('+'))

        self.frame_teclado.button_ap.configure(command=lambda:self.addTecladoVar('('))
        self.frame_teclado.button_fp.configure(command=lambda:self.addTecladoVar(')'))
# }}}


# {{{self.frame_alerta
    def alertaSetUp(self):
        self.frame_alerta.button_ok.configure(command=self.frame_alerta.place_forget)
# }}}


#atualização continua no self.frame_coord# {{{
    def leituraLoop(self):
        self.ler()
        self.var_x_atual_view.set(
                f'{(self.leitura[0] - self.var_x_main - self.var_x_atual)*self.res: >8.3f}')

        self.var_y_atual_view.set(
                f'{(self.leitura[1] - self.var_y_main - self.var_y_atual)*self.res: >8.3f}')

        self.root.after(25, self.leituraLoop)
    # }}}


#adiciona para o dicionario de coordenadas no self.var_coord_list # {{{
    def addCoordList(self, flag):
        contagem = 0
        lista = [int(x.split('_')[1])
                for x in self.var_coord_list
                if x.startswith(flag)]
        if lista:
            contagem = max(lista)

        self.var_coord_list[f'{flag}_{contagem + 1:0>2d}'] = (
                self.leitura[0] - self.var_x_main,
                self.leitura[1] - self.var_y_main)

        self.var_coord_list_view.set([*self.var_coord_list.keys()])
# }}}


# {{{ #atualiza self.frame_coord
    #atualiza a label do frame_coord
    def setFromCoordList(self):
        select = self.frame_coord.listbox.curselection()
        if select:
            chave = [*self.var_coord_list.keys()][select[0]]

            if chave.startswith('XX'):
                self.var_x_atual = self.var_coord_list[chave][0]

            elif chave.startswith('YY'):
                self.var_y_atual = self.var_coord_list[chave][1]

            else:
                self.var_x_atual, self.var_y_atual = self.var_coord_list[chave]

            self.var_history_view = chave
            self.atualizarLabel(chave)
# }}}

 
# {{{ #deleta a referencia selecionada do self.var_coord_list
    #atualiza a label do frame_coord
    def delFromCoordList(self):
        select = self.frame_coord.listbox.curselection()
        if select:
            chave = [*self.var_coord_list.keys()][select[0]]
            self.var_coord_list.pop(chave, 0)
            self.var_coord_list_view.set([*self.var_coord_list.keys()])
            self.frame_coord.listbox.selection_clear(select)

            if chave == self.var_history_view:
                self.atualizarLabel()
# }}}


# {{{ #limpa o dicionario de coordenadas self.var_coord_list
    #atualiza a label do frame_coord
    def limparCoordList(self):
        self.var_coord_list = {}
        self.var_coord_list_view.set([])
        self.atualizarLabel()
# }}}


#salvar/carregar lista de coordenadas# {{{
    def salvaCoordList(self):
        with open('coordlist_backup.txt', 'w') as f:
            f.write(json.dumps(self.var_coord_list))


    def loadCoordList(self):
        with open('coordlist_backup.txt') as f:
            self.var_coord_list = json.loads(f.read())
            self.var_coord_list_view.set([*self.var_coord_list.keys()])
# }}}


# {{{ #atualiza a label do frame_coord
    def atualizarLabel(self, label='*'):
        self.frame_coord.frame_coord.configure(text=label)
# }}}


# {{{chamada de teclado para variaveis
    def callTecladoVar(self, stringvar, func_norm, simbolo, nome):
        self.frame_teclado.label_tag.configure(text = nome)
        n = stringvar.get().replace(simbolo, '')
        if n in ('0', '0.0'):
            n = ''
        self.frame_teclado.var_label.set(n)
        self.frame_teclado.var_formula = n
        self.frame_teclado.button_igual.configure(command = lambda:self.calcVar(stringvar, func_norm, simbolo))
        self.frame_teclado.place(x=10, y=10)
# }}}


# {{{chamada de teclado para coordenadas
    def callTecladoCoord(self, stringvar, coord_set_func, nome):
        self.frame_teclado.label_tag.configure(text = nome)
        n = stringvar.get()
        self.frame_teclado.var_label.set(n)
        self.frame_teclado.var_formula = n
        self.frame_teclado.button_igual.configure(command = lambda : self.calcCoodVar(coord_set_func))
        self.frame_teclado.place(x = 10, y = 10)
# }}}


# {{{chamada de teclado para coordenada principal
    def callTecladoCoordMain(self, coord, coord_set_func, nome):
        self.frame_teclado.label_tag.configure(text = nome)
        self.frame_teclado.var_label.set('')
        self.frame_teclado.var_formula = ''
        self.frame_teclado.button_igual.configure(command = lambda : self.calcCoodVar(coord_set_func))
        self.frame_teclado.place(x = 10, y = 10)
# }}}


# {{{configurar valor de tecla
    def addTecladoVar(self, value):
        self.frame_teclado.var_formula += value
        if value == 'c':
            self.frame_teclado.var_formula = ''
        self.frame_teclado.var_label.set(self.frame_teclado.var_formula[-10:])
# }}}


# {{{calcular variavel
    def calcVar(self, stringvar, func_norm, simbolo):
        result = '0'
        formula = self.frame_teclado.var_formula

        if formula:
            try:result = eval(formula)
            except:pass

        stringvar.set(f'{func_norm(result)}{simbolo}')
        self.frame_teclado.place_forget()
# }}}


# {{{calcular coordenada
    def calcCoodVar(self, coord_set_func):
        result = 0
        formula = self.frame_teclado.var_formula

        try:result = eval(formula)
        except:pass

        if result:
            coord_set_func(valor = round(result/self.res))
        self.frame_teclado.place_forget()
# }}}

             
# {{{ proximo passo do raio
    def raioListProximo(self, passo):
        if self.var_ao_raio_list:
            if self.var_ao_raio_select + passo < 0:
                self.var_ao_raio_select = len(self.var_ao_raio_list)-1

            elif self.var_ao_raio_select + passo >= len(self.var_ao_raio_list):
                self.var_ao_raio_select = 0

            else:
                self.var_ao_raio_select += passo

            self.var_ao_raio_identificador.set(f'{self.var_ao_raio_select + 1}/{len(self.var_ao_raio_list)}')
            self.var_x_atual, self.var_y_atual = self.var_ao_raio_list[self.var_ao_raio_select]
            self.atualizarLabel(f'Raio furo {self.var_ao_raio_select + 1:0>2d}')
# }}}


# {{{ proximo passo da diagonal
    def diagListProximo(self, passo):
        if self.var_a_diagonal_list:
            if self.var_a_diagonal_select + passo < 0:
                self.var_a_diagonal_select = len(self.var_a_diagonal_list)-1

            elif self.var_a_diagonal_select + passo >= len(self.var_a_diagonal_list):
                self.var_a_diagonal_select = 0

            else:
                self.var_a_diagonal_select += passo

            self.var_a_diagonal_identificador.set(f'{self.var_a_diagonal_select + 1}/{len(self.var_a_diagonal_list)}')
            self.var_x_atual, self.var_y_atual = self.var_a_diagonal_list[self.var_a_diagonal_select]
            self.atualizarLabel(f'Diag furo {self.var_a_diagonal_select + 1:0>2d}')
# }}}


# {{{ calcular raio
    def calcRaio(self):
        self.var_ao_raio_select = 0
        furos = int(self.var_ao_raio_furos.get())
        raio = float(self.var_ao_raio_raio.get())
        desloc = float(self.var_ao_raio_desloc.get().replace('°',''))
        ang = 360 / furos if furos else 0

        self.var_ao_raio_list = [
                (round(cos(radians(ang*i+desloc))*raio/self.res+(self.leitura[0]-self.var_x_main)),
                 round(sin(radians(ang*i+desloc))*raio/self.res+(self.leitura[1]-self.var_y_main)))
                 for i in range(furos)]

        if self.var_ao_raio_list:
            self.var_ao_raio_identificador.set(f'1/{len(self.var_ao_raio_list)}')
            self.var_x_atual, self.var_y_atual = self.var_ao_raio_list[self.var_ao_raio_select]
            self.atualizarLabel('Raio furo 01')
# }}}


# {{{calcular diagonal
    def calcDiagonal(self):
        self.var_a_diagonal_select = 0
        furos = int(self.var_a_diagonal_furos.get())
        distancia = float(self.var_a_diagonal_distancia.get())
        angulo = float(self.var_a_diagonal_angulo.get().replace('°',''))
        desloc = float(self.var_a_diagonal_desloc.get())

        self.var_a_diagonal_list = [
                (round(cos(radians(angulo))*(distancia*i+desloc) / self.res+(self.leitura[0]-self.var_x_main)),
                 round(sin(radians(angulo))*(distancia*i+desloc) / self.res+(self.leitura[1]-self.var_y_main)))
                 for i in range(furos)]

        if self.var_a_diagonal_list:
            self.var_a_diagonal_identificador.set(f'1/{len(self.var_a_diagonal_list)}')
            self.var_x_atual, self.var_y_atual = self.var_a_diagonal_list[self.var_a_diagonal_select]
            self.atualizarLabel('Diag furo 01')
# }}}


# {{{funções basicas para zerar
    def setXAtual(self, valor = 0):
        self.var_x_atual = self.leitura[0] - self.var_x_main - valor
        self.atualizarLabel()


    def setYAtual(self, valor = 0):
        self.var_y_atual = self.leitura[1] - self.var_y_main - valor
        self.atualizarLabel()


    def setXMain(self):
        self.var_x_main = self.leitura[0]


    def setYMain(self):
        self.var_y_main = self.leitura[1]


    def DeslocarXMain(self, valor = 0):
        self.var_x_main -= valor


    def DeslocarYMain(self, valor = 0):
        self.var_y_main -= valor


    def setXMeio(self):
        self.var_x_atual = (self.leitura[0] + self.var_x_atual - self.var_x_main) // 2
        self.atualizarLabel()


    def setYMeio(self):
        self.var_y_atual = (self.leitura[1] + self.var_y_atual - self.var_y_main) // 2
        self.atualizarLabel()
 # }}}


# {{{ chamada do frame alerta
    def callAlerta(self, msg='Alerta!'):
        self.frame_alerta.place(relx=0.5, rely=0.5, anchor='center')
        self.frame_alerta.label_alerta.configure(text=msg)
# }}}

