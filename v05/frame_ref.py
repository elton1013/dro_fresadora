from tkinter import ttk
from func_comum import gridIter


class FrameRef(ttk.Frame):
    def __init__(self, master=None):
        super().__init__()

        self.button_referencia = ttk.Button(self, text='Ref',         style='Tools.TButton')
        self.button_centro = ttk.Button(self, text='Centro',          style='Tools.TButton')
        self.button_x = ttk.Button(self, text='XX',                   style='Tools.TButton')
        self.button_furo = ttk.Button(self, text='Furo',              style='Tools.TButton')
        self.button_rosca = ttk.Button(self, text='Rosca',            style='Tools.TButton')
        self.button_y = ttk.Button(self, text='YY',                   style='Tools.TButton')
        self.button_abilongo = ttk.Button(self, text='Abilongo',      style='Tools.TButton')
        self.button_raio = ttk.Button(self, text='Raio',              style='Tools.TButton')
        self.button_diagonal = ttk.Button(self, text='Diagonal',      style='Tools.TButton')

        for pos_i, i in enumerate(gridIter([*self.children.values()], 3)):
            for pos_j, j in enumerate(i):
                j.grid(column=pos_j, row=pos_i, padx=10, pady=10)


if __name__ == '__main__':
    from gui_style import GuiStyle
    root = ttk.tkinter.Tk()
    GuiStyle(root)
    f = FrameRef(root)
    f.pack()
    root.mainloop()

