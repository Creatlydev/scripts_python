import tkinter as tk
from tkinter import ttk


class Modal(tk.Toplevel):
    def __init__(self, parent= None):
        super().__init__(parent, padx= 15, pady= 15)
        self.title('Ajustes de compression avanzados')
        self.parent = parent

        self.center() # Centra la ventana Modal
        self.widgets()

        # Evento <Return> al modal para guardar los cambios al presionar ENTER
        self.bind('<Return>', lambda x: self.save())

        self.transient(parent)
        self.focus_force() 
        # Hacer que la ventana modal sea la única activa
        self.grab_set()
        parent.wait_window(self)
    
    def widgets(self) :
        self.lbframe_to_jpg = ttk.LabelFrame(self, text= 'PNG a JPG')
        self.var_check_to_jpg = tk.BooleanVar(value= False)
        self.check_to_jpg = ttk.Checkbutton(self.lbframe_to_jpg, text= ' Convertir archivos PNG a JPG ', variable= self.var_check_to_jpg)

        self.lbframe_to_jpg.pack(expand= True, fill= tk.BOTH)
        self.check_to_jpg.pack(expand= True, fill= tk.X)
        # -----------------------------------------------------------------------
        self.lbframe_quality = ttk.LabelFrame(self, text= ' Calidad de la imagen ')
        self.var_num_quality = tk.IntVar(value= 90)
        self.num_quality = tk.Scale(self.lbframe_quality, from_= 1, to= 100, variable= self.var_num_quality, showvalue= True, orient= tk.HORIZONTAL)        

        self.lbframe_quality.pack(expand= True, fill= tk.BOTH)
        self.num_quality.pack(expand= True, fill= tk.X)
        # -----------------------------------------------------------------------
        self.lbframe_resize_ratio = ttk.LabelFrame(self, text= ' Redimensionar imagen x su radio ')
        self.var_num_resize_ratio = tk.DoubleVar(value= 1.0)
        self.num_resize_ratio = tk.Scale(self.lbframe_resize_ratio, from_= 0.1, to= 1.0, variable= self.var_num_resize_ratio, showvalue= True, orient= tk.HORIZONTAL, resolution= 0.1)  

        self.lbframe_resize_ratio.pack(expand= True, fill= tk.BOTH)
        self.num_resize_ratio.pack(expand= True, fill= tk.X)
        # -----------------------------------------------------------------------
        self.lbframe_manual_resize = ttk.LabelFrame(self, text= ' Redimensionar a un tamaño fijado ')
        self.frame_width = ttk.Frame(self.lbframe_manual_resize)
        self.frame_height = ttk.Frame(self.lbframe_manual_resize)
        self.var_entry_width = tk.StringVar()
        self.lb_width = ttk.Label(self.frame_width, text= 'Ancho nuevo', justify= tk.CENTER, font= ('Verdana', 8, 'normal'))
        self.entry_width = ttk.Entry(self.frame_width, textvariable= self.var_entry_width) 
        self.var_entry_height = tk.StringVar()
        self.lb_height = ttk.Label(self.frame_height, text= 'Alto nuevo', justify= tk.CENTER, font= ('Verdana', 8, 'normal'))
        self.entry_height = ttk.Entry(self.frame_height, textvariable= self.var_entry_height)

        self.lbframe_manual_resize.pack(expand= True, fill= tk.BOTH)
        self.frame_width.pack(expand= True, fill= tk.BOTH, side= tk.LEFT, padx= 10)
        self.frame_height.pack(expand= True, fill= tk.BOTH, side= tk.RIGHT, padx= 10)
        self.lb_width.pack(pady= 10)
        self.entry_width.pack(expand= True, fill= tk.X)
        self.lb_height.pack(pady= 10)
        self.entry_height.pack(expand= True, fill= tk.X)

        # ------------------------------------------------------------------
        # Boton para salvar las configuraciones modificadas
        self.btn_save = ttk.Button(self, text= 'GUARDAR', command= self.save)
        self.btn_save.pack(expand= True, fill= tk.X, padx= 30, pady= 10)


    def center(self) :
        # Obtener el ancho y alto de la pantalla
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        x = (width // 2) - (150)
        y = (height // 2) - (175)
        self.geometry(f'300x350+{x}+{y}')

    def save(self):
        self.destroy()
        self.parent.setting_images =  {
            'to_jpg': self.var_check_to_jpg.get(),
            'quality': self.var_num_quality.get(),
            'new_size_ratio': self.var_num_resize_ratio.get(), 
            'width': self.var_entry_width.get(),
            'height': self.var_entry_height.get()
        }
