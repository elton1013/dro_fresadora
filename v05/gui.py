from tkinter import ttk
from frame_tools import FrameZeroTools
from frame_coord import FrameCoord
from frame_ref import FrameRef
from frame_ao_raio import FrameAoRaio
from frame_a_diagonal import FrameADiagonal
from frame_sistema import FrameSistema
from frame_teclado import FrameTeclado
from frame_alerta import FrameAlerta


class Gui:
    def guiSetUp(self):
        self.root = ttk.tkinter.Tk()
        #self.root.attributes('-fullscreen', 1)
        self.root.geometry('640x480+50-50')
        self.note_book = ttk.Notebook(self.root, width=400, height=480)
        self.frame_tools = FrameZeroTools(self.note_book)
        self.frame_ref = FrameRef(self.note_book)
        self.frame_ao_raio = FrameAoRaio(self.note_book)
        self.frame_a_diagonal = FrameADiagonal(self.note_book)
        self.frame_sistema = FrameSistema(self.note_book)
        self.frame_coord = FrameCoord(self.root)
        self.frame_teclado = FrameTeclado(self.root)
        self.frame_alerta = FrameAlerta(self.root)

        self.note_book.add(self.frame_tools, text='Zerar')
        self.note_book.add(self.frame_ref, text='Referir')
        self.note_book.add(self.frame_ao_raio, text='Ao Raio')
        self.note_book.add(self.frame_a_diagonal, text='Diagonal')
        self.note_book.add(self.frame_sistema, text='Sistema')

        self.frame_coord.pack(side='right', padx=10, pady=10)
        self.note_book.pack(side='left', padx=10, pady=10)


if __name__ == '__main__':
    from gui_style import GuiStyle
    root = Gui()
    root.guiSetUp()
    GuiStyle(root.root)
    root.root.mainloop()

