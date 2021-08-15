from tkinter.ttk import Style
from tkinter import Tk

class GuiStyle(Style):
    FONT_COORD = ('TkDefaultFont', 30)
    FONT_TAG_COORD = ('TkDefaultFont', 14)
    FONT_BUTTON = ('TkDefaultFont', 14)
    FONT_LABEL = ('TkDefaultFont', 20)

    def __init__(self, master=None):
        super().__init__()
        self.tk.call('source', '../Forest-ttk-theme-master/forest-light.tcl')
        self.theme_use('forest-light')

        self.configure('Tools.TButton', padding='0 30 0 30', width=8, font=self.FONT_BUTTON)

        self.configure('Coord.TButton', width=6, padding='10 20 10 20')
        self.configure('Coord.TLabelframe.Label', font=self.FONT_TAG_COORD)
        self.configure('Coord.TLabel', font=self.FONT_COORD, anchor='e', width=7, padding='0 6 6 6')

        self.configure('DiagRaio.TLabel', font=self.FONT_LABEL, width=7, anchor='e')
        self.configure('DiagRaioValue.TLabel', font=self.FONT_LABEL, width=8, anchor='w')
        self.configure('DiagRaio.TButton', font=self.FONT_LABEL, width=1, padding='14 6 14 6')
        self.configure('DiagRaioCommand.TButton', font=self.FONT_BUTTON, width=4, padding='30 20 30 20')
        self.configure('DiagRaioCalc.TButton', font=self.FONT_BUTTON, padding='20 10 20 10', anchor='we')
        self.configure('DiagRaioCommand.TLabel', font=self.FONT_LABEL)

        self.configure('TagCoord.TLabel', font=self.FONT_TAG_COORD, padding='6 0 0 0')

        self.configure('Teclado.TButton', padding='28 16 28 16', width=2, font=self.FONT_BUTTON)
        self.configure('Teclado.TLabel', font=self.FONT_LABEL, width=10, anchor='we', padding='0 6 0 6')
        self.configure('TecladoTag.TLabel', font=self.FONT_LABEL, width=8, anchor='we', padding='0 6 0 6')

        self.configure('Alerta.TLabel', font=self.FONT_LABEL)
        self.configure('Alerta.TButton', font=self.FONT_LABEL)
        self.configure('Alerta.TFrame', relief='solid', borderwidth=1)


if __name__ == '__main__':
    root = Tk()
    s = GuiStyle(root)
    root.mainloop()
