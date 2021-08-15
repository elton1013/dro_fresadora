from tkinter import ttk
from func_comum import gridIter


class FrameAoRaio(ttk.Frame):
    def __init__(self, master=None, *args):
        super().__init__()
        self.label_furos = ttk.Label(self, text='Furos : ', style='DiagRaio.TLabel')
        self.label_raio = ttk.Label(self, text='Raio : ', style='DiagRaio.TLabel')
        self.label_desloc = ttk.Label(self, text='Desloc : ', style='DiagRaio.TLabel')
        self.label_furos_value = ttk.Label(self, text='0', style='DiagRaioValue.TLabel')
        self.label_raio_value = ttk.Label(self, text='0', style='DiagRaioValue.TLabel')
        self.label_desloc_value = ttk.Label(self, text='0.0°', style='DiagRaioValue.TLabel')
        self.button_furos = ttk.Button(self, text='<', style='DiagRaio.TButton')
        self.button_raio = ttk.Button(self, text='<', style='DiagRaio.TButton')
        self.button_desloc = ttk.Button(self, text='<', style='DiagRaio.TButton')

        self.button_calc = ttk.Button(self, text='Calcular', style='DiagRaioCalc.TButton')

        self.button_anterior = ttk.Button(self, text='<<', style='DiagRaioCommand.TButton')
        self.button_proximo = ttk.Button(self, text='>>', style='DiagRaioCommand.TButton')
        self.label_identificador = ttk.Label(self, text='0/0', style='DiagRaioCommand.TLabel')

        self.label_furos.grid(row=0, column=0, pady=16)
        self.label_raio.grid(row=1, column=0, pady=16)
        self.label_desloc.grid(row=2, column=0, pady=16)
        self.label_furos_value.grid(row=0, column=1)
        self.label_raio_value.grid(row=1, column=1)
        self.label_desloc_value.grid(row=2, column=1)
        self.button_furos.grid(row=0, column=2)
        self.button_raio.grid(row=1, column=2)
        self.button_desloc.grid(row=2, column=2)

        self.button_calc.grid(row=3, column=0, columnspan=4, padx=100, pady=30)

        self.button_anterior.grid(row=4, column=0, pady=20)
        self.button_proximo.grid(row=4, column=2)
        self.label_identificador.grid(row=4, column=1)


if __name__ == '__main__':
    from gui_style import GuiStyle
    root = ttk.tkinter.Tk()
    f = FrameAoRaio(root)
    f.pack()
    GuiStyle(root)
    root.mainloop()

