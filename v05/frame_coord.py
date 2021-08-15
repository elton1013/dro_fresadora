from tkinter import ttk
from func_comum import gridIter


class FrameCoord(ttk.Frame):
    PADY = 8
    FONT_LIST = ('TkDefaultFont', 20)


    def __init__(self, master=None):
        super().__init__(master=master)
        self.frameTopo(self)
        self.frameMeio(self)
        self.frameBaixo(self)


    def frameTopo(self, master):
        self.frame_coord = ttk.LabelFrame(self, text='*', style='Coord.TLabelframe')
        self.label_x = ttk.Label(self.frame_coord, text='x', style='TagCoord.TLabel')
        self.label_y = ttk.Label(self.frame_coord, text='y', style='TagCoord.TLabel')
        self.label_coord_x = ttk.Label(self.frame_coord, text='0.000', style='Coord.TLabel')
        self.label_coord_y = ttk.Label(self.frame_coord, text='0.000', style='Coord.TLabel')

        self.frame_coord.pack(side='top', pady=self.PADY)
        self.label_x.grid(column=0, row=0)
        self.label_y.grid(column=0, row=1)
        self.label_coord_x.grid(column=1, row=0)
        self.label_coord_y.grid(column=1, row=1)


    def frameMeio(self, master):
        self.frame_list = ttk.Frame(self)
        self.scrool_list = ttk.Scrollbar(self.frame_list, style='Coord.Vertical.TScrollbar')
        self.listbox = ttk.tkinter.Listbox(self.frame_list,
                width=8, height=5, font=self.FONT_LIST, relief='solid', bd=1)

        self.frame_list.pack(side='top', pady=self.PADY)
        self.scrool_list.pack(side='left', fill='y', padx=8)
        self.listbox.pack(side='right')


    def frameBaixo(self, master):
        self.frame_list_tools = ttk.Frame(self)
        self.button_list_set = ttk.Button(self.frame_list_tools, text='Set')
        self.button_list_del = ttk.Button(self.frame_list_tools, text='Del')
        self.button_list_set.configure(style='Coord.TButton')
        self.button_list_del.configure(style='Coord.TButton')

        self.frame_list_tools.pack(side='top', pady=self.PADY)
        for pos_i, i in enumerate(gridIter([*self.frame_list_tools.children.values()], 3)):
            for pos_j, j in enumerate(i):
                j.grid(column=pos_j, row=pos_i, padx=10, pady=2)



if __name__ == '__main__':
    from gui_style import GuiStyle
    root = ttk.tkinter.Tk()
    f = FrameCoord(root)
    f.pack()
    GuiStyle(root)
    root.mainloop()
