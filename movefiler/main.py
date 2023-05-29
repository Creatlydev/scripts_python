import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
import os

import keyboard

from compressor import move_files
from modal_set_images import Modal


downloadFolder = "C:/Users/SAMIR/Downloads"

picturesFolder = "D:/samir/Pictures"
musicFolder = "D:/samir/Music"
videoFolder = "D:/samir/Videos"
documentsFolder  = "D:/samir/Documents"


def real_path(relative_path) :
    base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class Window(tk.Frame) :

    def __init__(self, master= None, cnf= {}, **kwarg) :
        super().__init__(master, cnf, **kwarg) 

        self.root = master
        self.setting_images = {} # Ajustes para comprimir las imagenes
        # Cargar imagenes con [tkinter.PhotoImage]
        self.path_img_folder = real_path('assets\carpeta.png')
        self.path_img_setting = real_path('assets\configuraciones.png') 
        self.img_folder = PhotoImage(file= self.path_img_folder)
        self.img_setting = PhotoImage(file= self.path_img_setting)
        # Crear estilos personalizados
        self.style = ttk.Style()
        self.style.theme_use('vista')
        self.style.configure('TSeparator', relief= 'flat')
        self.style.configure('TButton', width= 4, font= ('Verdana', 9, 'bold'))
        self.style.configure('TLabel', font= ('Verdana', 15, 'bold'))

        self.frame_paths= tk.Frame(self) 
        self.frame_paths.columnconfigure(1, weight= 1)
        self.frame_paths.columnconfigure(2, weight= 1)

        self.title = ttk.Label(self.frame_paths, text= 'Configuración', foreground= 'steelblue', justify= 'center')
        self.title.grid(row= 0, column= 0, columnspan= 4, pady= 25) 

        self.label = ttk.Label(self.frame_paths, text= 'Seleccionar de:', font= ('Verdana', 8, 'normal'))
        self.label.grid(row= 1, column= 0, pady= 5) 

        self.var_dir_select_files = tk.StringVar(self.frame_paths, value= downloadFolder)

        self.dir_select_files = ttk.Entry(self.frame_paths, state= 'readonly', textvariable= self.var_dir_select_files)
        self.btn_dir_select_files = ttk.Button(self.frame_paths, image= self.img_folder, command= lambda : self.select_path(self.var_dir_select_files)) 

        self.dir_select_files.grid(row= 2, column= 0, columnspan= 4, sticky= 'ew')
        self.btn_dir_select_files.grid(row= 2, column= 4)

        ttk.Separator(self.frame_paths).grid(row= 3, column= 0, columnspan= 5, sticky= 'ew', pady= 20)

        self.var_dir_images = tk.StringVar(self.frame_paths, value= picturesFolder)
        self.var_dir_videos = tk.StringVar(self.frame_paths, value= videoFolder)
        self.var_dir_music = tk.StringVar(self.frame_paths, value= musicFolder)
        self.var_dir_documents = tk.StringVar(self.frame_paths, value= documentsFolder) 

        self.dir_images = ttk.Entry(self.frame_paths, state= 'readonly', textvariable= self.var_dir_images)
        self.dir_videos = ttk.Entry(self.frame_paths, state= 'readonly', textvariable= self.var_dir_videos)
        self.dir_music = ttk.Entry(self.frame_paths, state= 'readonly', textvariable= self.var_dir_music)
        self.dir_documents = ttk.Entry(self.frame_paths, state= 'readonly', textvariable= self.var_dir_documents)

        self.btn_dir_images = ttk.Button(self.frame_paths, image= self.img_folder, command= lambda : self.select_path(self.var_dir_images))
        self.btn_setting_images = ttk.Button(self.frame_paths, image= self.img_setting, command= lambda : self.open_modal_setting_images()) 
        self.btn_dir_videos = ttk.Button(self.frame_paths, image= self.img_folder, command= lambda : self.select_path(self.var_dir_videos))
        self.btn_dir_music = ttk.Button(self.frame_paths, image= self.img_folder, command= lambda : self.select_path(self.var_dir_music))
        self.btn_dir_documents = ttk.Button(self.frame_paths, image= self.img_folder, command= lambda : self.select_path(self.var_dir_documents))

        self.dir_images.grid(row= 4, column= 0, columnspan= 3, sticky= 'ew')
        self.btn_dir_images.grid(row= 4, column= 3) 
        self.btn_setting_images.grid(row= 4, column= 4) 

        ttk.Separator(self.frame_paths).grid(row= 5, column= 0, columnspan= 5, sticky= 'ew', pady= 10)

        self.dir_videos.grid(row= 6, column= 0, columnspan= 4, sticky= 'ew')
        self.btn_dir_videos.grid(row= 6, column= 4)

        ttk.Separator(self.frame_paths).grid(row= 7, column= 0, columnspan= 5, sticky= 'ew', pady= 10)

        self.dir_music.grid(row= 8, column= 0, columnspan= 4, sticky= 'ew')
        self.btn_dir_music.grid(row= 8, column= 4)

        ttk.Separator(self.frame_paths).grid(row= 9, column= 0, columnspan= 5, sticky= 'ew', pady= 10)

        self.dir_documents.grid(row= 10, column= 0, columnspan= 4, sticky= 'ew')
        self.btn_dir_documents.grid(row= 10, column= 4)



        self.frame_buttons= tk.Frame(self, height= 70)
        self.frame_buttons.propagate(False) 

        self.btn_iniciar = ttk.Button(self.frame_buttons, text= 'INICIAR', command= self.move_files, width= 10) 
        self.btn_iniciar.pack(side= tk.RIGHT, padx= 5)

        self.frame_paths.pack(expand= True, fill= tk.BOTH, padx= 10, pady= 10)
        self.frame_buttons.pack(fill= tk.BOTH)
        self.pack(expand= True, fill= tk.BOTH) 

    
    def select_path(self, var: tk.StringVar) :
        path_dir = filedialog.askdirectory() 
        if path_dir : var.set(path_dir)

    
    def open_modal_setting_images(self) :
        Modal(self)


    def move_files(self) :
        move_files(
            self.var_dir_select_files.get() + '/',
            self.var_dir_images.get() + '/',
            self.var_dir_music.get() + '/',
            self.var_dir_videos.get() + '/',
            self.var_dir_documents.get() + '/',
            **self.setting_images
        )
        messagebox.showinfo(
            'Exito',
            'Realizado exitosamente'
        )




def on_hotkey() :
    root= tk.Tk() 
    root.wm_attributes('-topmost', True) 
    root.iconbitmap(real_path('assets\icon.ico'))
    # Obtener el ancho y alto de la pantalla
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    # Calcular las coordenadas x e y para centrar la ventana en la pantalla
    x = (width // 2) - (400 // 2)
    y = (height // 2) - (450 // 2)

    root.minsize(width= 400, height= 450) 
    root.maxsize(width= 400, height= 450)
    root.geometry(f'400x450+{x}+{y}')
    root.focus_force()
    root.transient()
    root.resizable(False, False)
    root.title('MoveFiler') 
    Window(root)

    root.mainloop()


if __name__ == '__main__' :

    keyboard.add_hotkey('ctrl+alt+m', on_hotkey)
    keyboard.wait()
