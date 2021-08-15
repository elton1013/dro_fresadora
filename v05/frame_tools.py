from tkinter import ttk
from func_comum import gridIter


class FrameZeroTools(ttk.Frame):
    def __init__(self, master=None):
        super().__init__()

        self.button_x_zero = ttk.Button(self, text='X Zero', style='Tools.TButton')
        self.button_x_meio = ttk.Button(self,  text='X 1/2', style='Tools.TButton')
        self.button_x_calc = ttk.Button(self,  text='X Calc', style='Tools.TButton')
                     
        self.button_y_zero = ttk.Button(self, text='Y Zero', style='Tools.TButton')
        self.button_y_meio = ttk.Button(self,  text='Y 1/2', style='Tools.TButton')
        self.button_y_calc = ttk.Button(self,  text='Y Calc', style='Tools.TButton')

        for pos_i, i in enumerate(gridIter([*self.children.values()], 3)):
            for pos_j, j in enumerate(i):
                j.grid(column=pos_j, row=pos_i, padx=10, pady=10)



if __name__ == '__main__':
    from gui_style import GuiStyle
    root = ttk.tkinter.Tk()
    GuiStyle(root)
    f = FrameZeroTools(root)
    f.pack()
    root.mainloop()

