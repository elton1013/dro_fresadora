from tkinter import ttk
from func_comum import gridIter


class FrameSistema(ttk.Frame):
    def __init__(self, master=None):
        super().__init__()

        self.button_sair = ttk.Button(self, text='Sair',                   style='Tools.TButton')
        self.button_desligar = ttk.Button(self, text='Desligar',           style='Tools.TButton')
        self.button_limpar_historico = ttk.Button(self, text='Limpar',     style='Tools.TButton')

        self.button_zero_x_main = ttk.Button(self, text='Z Main X',        style='Tools.TButton')
        self.button_calc_x_main = ttk.Button(self, text='Deslc X',         style='Tools.TButton')
        self.button_salvar_historico = ttk.Button(self, text='Salvar',     style='Tools.TButton')

        self.button_zero_y_main = ttk.Button(self, text='Z Main Y',        style='Tools.TButton')
        self.button_calc_y_main = ttk.Button(self, text='Deslc Y',         style='Tools.TButton')
        self.button_carregar_historico = ttk.Button(self, text='Carregar', style='Tools.TButton')

        for pos_i, i in enumerate(gridIter([*self.children.values()], 3)):
            for pos_j, j in enumerate(i):
                j.grid(column=pos_j, row=pos_i, padx=10, pady=10)


if __name__ == '__main__':
    from gui_style import GuiStyle
    root = ttk.tkinter.Tk()
    root.geometry('680x460+100-100')
    GuiStyle(root)
    f = FrameSistema(root)
    f.pack()
    root.mainloop()

