from tkinter import ttk
from func_comum import gridIter


class FrameADiagonal(ttk.Frame):
    def __init__(self, master=None):
        super().__init__()
        self.label_furos = ttk.Label(self, text='Furos : ', style='DiagRaio.TLabel')
        self.label_distancia = ttk.Label(self, text='Distan : ', style='DiagRaio.TLabel')
        self.label_angulo = ttk.Label(self, text='Angulo : ', style='DiagRaio.TLabel')
        self.label_desloc = ttk.Label(self, text='Desloc : ', style='DiagRaio.TLabel')
        self.label_furos_value = ttk.Label(self, text='0', style='DiagRaioValue.TLabel')
        self.label_distancia_value = ttk.Label(self, text='0.0', style='DiagRaioValue.TLabel')
        self.label_angulo_value = ttk.Label(self, text='0.0°', style='DiagRaioValue.TLabel')
        self.label_desloc_value = ttk.Label(self, text='0.0', style='DiagRaioValue.TLabel')
        self.button_furos = ttk.Button(self, text='<', style='DiagRaio.TButton')
        self.button_distancia = ttk.Button(self, text='<', style='DiagRaio.TButton')
        self.button_angulo = ttk.Button(self, text='<', style='DiagRaio.TButton')
        self.button_desloc = ttk.Button(self, text='<', style='DiagRaio.TButton')

        self.button_calc = ttk.Button(self, text='Calcular', style='DiagRaioCalc.TButton')

        self.button_anterior = ttk.Button(self, text='<<', style='DiagRaioCommand.TButton')
        self.button_proximo = ttk.Button(self, text='>>', style='DiagRaioCommand.TButton')
        self.label_identificador = ttk.Label(self, text='0/0', style='DiagRaioCommand.TLabel')

        self.label_furos.grid(row=0, column=0, pady=16)
        self.label_distancia.grid(row=1, column=0, pady=16)
        self.label_angulo.grid(row=2, column=0, pady=16)
        self.label_desloc.grid(row=3, column=0, pady=16)
        self.label_furos_value.grid(row=0, column=1)
        self.label_distancia_value.grid(row=1, column=1)
        self.label_angulo_value.grid(row=2, column=1)
        self.label_desloc_value.grid(row=3, column=1)
        self.button_furos.grid(row=0, column=2)
        self.button_distancia.grid(row=1, column=2)
        self.button_angulo.grid(row=2, column=2)
        self.button_desloc.grid(row=3, column=2)

        self.button_calc.grid(row=4, column=0, columnspan=4, padx=100, pady=10)

        self.button_anterior.grid(row=5, column=0)
        self.button_proximo.grid(row=5, column=2)
        self.label_identificador.grid(row=5, column=1)


if __name__ == '__main__':
    from gui_style import GuiStyle
    root = ttk.tkinter.Tk()
    f = FrameADiagonal(root)
    f.pack()
    GuiStyle(root)
    root.mainloop()

