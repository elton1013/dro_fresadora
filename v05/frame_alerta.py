from tkinter import ttk

class FrameAlerta(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master, width=400, height=150, style='Alerta.TFrame')
        self.label_alerta = ttk.Label(self,
                text='Possivel falha do sensor!\nConfira o ponto de origem.',
                style='Alerta.TLabel')
                
        self.button_ok = ttk.Button(self, text='Ok', style='Alerta.TButton')

        self.label_alerta.place(relx=0.5, rely=0.3, ancho='center')
        self.button_ok.place(relx=0.5, rely=0.75, ancho='center')


if __name__ == '__main__':
    from gui_style import GuiStyle
    root = ttk.tkinter.Tk()
    f = FrameAlerta(root)
    f.pack()
    GuiStyle(root)
    root.mainloop()
