from tkinter import ttk
from func_comum import gridIter


class FrameTeclado(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master, padding='100 4 140 10')
        self.frame_numeral = ttk.Frame(self)
        self.label_tag = ttk.Label(self.frame_numeral, style='TecladoTag.TLabel')
        self.label_numeral = ttk.Label(self.frame_numeral, style='Teclado.TLabel')
        self.button_c = ttk.Button(self.frame_numeral, text='C', style='Teclado.TButton')

        self.frame_techado = ttk.Frame(self)
        self.button_9 = ttk.Button(self.frame_techado, text='9')
        self.button_8 = ttk.Button(self.frame_techado, text='8')
        self.button_7 = ttk.Button(self.frame_techado, text='7')
        self.button_div = ttk.Button(self.frame_techado, text='/')

        self.button_6 = ttk.Button(self.frame_techado, text='6')
        self.button_5 = ttk.Button(self.frame_techado, text='5')
        self.button_4 = ttk.Button(self.frame_techado, text='4')
        self.button_vz = ttk.Button(self.frame_techado, text='*')

        self.button_3 = ttk.Button(self.frame_techado, text='3')
        self.button_2 = ttk.Button(self.frame_techado, text='2')
        self.button_1 = ttk.Button(self.frame_techado, text='1')
        self.button_menos = ttk.Button(self.frame_techado, text='-')

        self.button_0 = ttk.Button(self.frame_techado, text='0')
        self.button_ponto = ttk.Button(self.frame_techado, text='.')
        self.button_igual = ttk.Button(self.frame_techado, text='=')
        self.button_mais = ttk.Button(self.frame_techado, text='+')

        self.button_ap = ttk.Button(self.frame_techado, text='(')
        self.button_fp = ttk.Button(self.frame_techado, text=')')


        self.frame_numeral.pack()
        self.frame_techado.pack()

        self.label_tag.pack(side='left', pady=10)
        self.label_numeral.pack(side='left', pady=10)
        self.button_c.pack(side='right', padx=6, pady=10)

        for pos_i, i in enumerate(gridIter([*self.frame_techado.children.values()], 4)):
            for pos_j, j in enumerate(i):
                j.grid(column=pos_j, row=pos_i, padx=6, pady=6)
                j.configure(style='Teclado.TButton')


if __name__ == '__main__':
    from gui_style import GuiStyle
    root = ttk.tkinter.Tk()
    root.geometry('640x480')
    f = FrameTeclado(root)
    f.pack()
    GuiStyle(root)
    root.mainloop()

