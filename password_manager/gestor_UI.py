
# TODO - PROGRAMACION DE LA INTERFAZ GRAFICA DEL GESTOR DE CONTRASEÑAS


import os
from pickle import NONE
import sys
from os import write
import conexionDB as conexion
import tkinter as tk
from tkinter import ttk, messagebox
import string
import random       


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# TODO - CLASE DE LA PRIMERA VENTANA AL EJECUTAR EL PROGRAMA
class Inicio(tk.Frame):

    def __init__(self, master, **kwargs) -> None:

        super().__init__(master, cnf={}, **kwargs)
        self.master = master
        # atributo que contiene los metodos de la clase del archivo importado conexionDB as conexion
        self.connect = conexion.Credenciales()
        self.fuente = 'verdana {} {} italic'
        self.master.title('Gestor - Pro')
        path = resource_path(r'.\locked.ico')
        self.master.iconbitmap(path)

        # CONFIGURACION DE COLUMNAS Y FILAS DEL FRAME PRINCIPAL
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(4, weight=1)

        self.opcion = tk.IntVar()
        self.opcion.set(1)

        titulo = tk.Label(self, text='GESTOR DE CONTRASEÑAS', font=self.fuente.format(
            25, 'bold'), fg='white', bg='orange', relief='ridge')

        opcion1 = tk.Radiobutton(self, text='  Crear nueva tabla de contraseñas', variable=self.opcion,
                                 value=1, anchor='w', font=self.fuente.format(15, 'normal'), command=self.frame_opcionUno)
        opcion2 = tk.Radiobutton(self, text='  Abrir tabla existente de contraseñas', variable=self.opcion,
                                 value=2, anchor='w', font=self.fuente.format(15, 'normal'), command=self.frame_opcionDos)
        separador = ttk.Separator(self, orient='horizontal')

        titulo.grid(row=0, column=0, columnspan=3, sticky='ew', pady=30)
        opcion1.grid(row=1, column=1, sticky='nsew')
        opcion2.grid(row=2, column=1, sticky='nsew', pady=10)
        separador.grid(row=3, column=0, sticky='nsew', columnspan=3, pady=20)
        self.pack(side='top', fill='both', expand=1, padx=50, pady=0)

        self.frame_opcionUno()

    # FUNCION QUE SE EJECUTA AL PRESIONAR EL RADIOBUTTON 1 DE LA VENTANA

    def frame_opcionUno(self):

        var = tk.StringVar()

        frame = tk.Frame(self, bg='white', relief='ridge', bd=7)
        label = tk.Label(frame, text='Nombre de la nueva tabla',
                         font=self.fuente.format(18, 'normal'), bg='orange')
        entry = tk.Entry(frame, textvariable=var, highlightthickness=2,
                         highlightbackground='gray', highlightcolor='orange', width=20, font='Verdana 10 bold italic')
        boton_crear = tk.Button(frame, text='Crear Tabla', font=self.fuente.format(
            18, 'normal'), command=lambda: self.showTabla(var.get().strip(), frame, error, 'write'), bg='lime', fg='white', activebackground='lime', activeforeground='white')
        error = tk.Label(frame, bg='white', justify='center')

        label.pack(side='top', pady=40, padx=5)
        entry.pack(side='top')
        boton_crear.pack(side='top', pady=50)
        error.pack(side='top')

        frame.grid(row=4, column=0, columnspan=3,
                   sticky='nsew', pady=30, padx=200)

        boton_crear.bind('<Enter>', lambda x: boton_crear.config(bg='red'))
        boton_crear.bind('<Leave>', lambda x: boton_crear.config(bg='lime'))
    # FUNCION QUE SE EJECUTA AL PRESIONAR EL RADIOBUTTON 2 DE LA VENTANA

    def frame_opcionDos(self):

        var = tk.StringVar()

        frame = tk.Frame(self, bg='white', relief='ridge', bd=7)
        label = tk.Label(frame, text='Seleccionar Tabla',
                         font=self.fuente.format(18, 'normal'), bg='orange')

        self.tablas = ttk.Combobox(
            frame, height=8, state='readonly', font=self.fuente.format(10, 'normal'))
        self.tablas['values'] = self.connect.tablas
        self.tablas.set('Seleccionar')
        boton_abrir = tk.Button(frame, text='Abrir Tabla', font=self.fuente.format(
            18, 'normal'), command=lambda: self.showTabla(self.tablas.get().strip(), frame, error, 'read'), bg='lime', fg='white', activebackground='lime', activeforeground='white')
        error = tk.Label(frame, bg='white', justify='center')

        label.pack(side='top', pady=40, padx=5)
        self.tablas.pack(side='top')
        boton_abrir.pack(side='top', pady=50)
        error.pack(side='top')

        frame.grid(row=4, column=0, columnspan=3,
                   sticky='nsew', pady=30, padx=200)

    # METODO QUE SE EJECUTA DESPUES DE COMPLETAR EL FRAME 1 O 2 CORRECTAMENTE

    def showTabla(self, nameTabla, frame, variable, accion='write'):

        llave = False
        if accion == 'write':
            verificar = self.connect.crear(nameTabla)

            if not (verificar):
                llave = True
                frame.after(10, lambda: self.mensaje_error(
                    'Ya existe una tabla\nCon ese nombre', 0, bg='red', frame=frame, fg='white', variable=variable))

            elif nameTabla.isspace() or len(nameTabla) == 0:
                llave = True
                frame.after(10, lambda: self.mensaje_error(
                    'Escoge un nombre\nPara la tabla', 0, bg='red', frame=frame, fg='white', variable=variable))

        else:
            if nameTabla == 'Seleccionar':
                llave = True
                frame.after(10, lambda: self.mensaje_error(
                    'Escoge\nUna tabla', 0, bg='red', frame=frame, fg='white', variable=variable))

        # SI NO OCURRE NINGUN ERROR TANTO EN EL FRAME DE CREAR NUEVA TABLA
        # COMO EN EL DE ABRIR UNA SE EJECUTA LA SEGUNDA VENTANA <CLASE TABLA>.
        geometry = (self.master.winfo_geometry())
        if not (llave):
            segundaVentana(self.master, nameTabla, self.connect, geometry)

    # METODO PARA MOSTRAR UN MENSAJE DE ERROR DURANTE 2 SEGUNDOS

    def mensaje_error(self, m=None, count=0, **kwargs):

        if count <= 2:
            kwargs['variable'].config(
                bg=kwargs['bg'], text=m, fg=kwargs['fg'], justify='center')
            kwargs['frame'].after(
                1000, lambda: self.mensaje_error(m, count + 1, **kwargs))

        else:
            kwargs['variable'].config(bg='white', text='')


# TODO- CLASE DE LA SEGUNDA VENTANA DONDE SE MOSTRARA LA TABLA SELECCIONADA O CREADA DESDE LA PRIMERA VENTANA,  RELLENADA CON SUS DATOS .
class Tabla:

    def __init__(self, master, nameTabla, db) -> None:

        self.master = master
        self.db = db  # ATRIBUTO PASADO DESDE LA PRIMERA VENTANA QUE SERVIRA PARA LEER-ACTUALIZAR-ELIMINAR REGISTRO DE LA TABLA ABIERTA O CREADA DESDE LA PRIMERA VENTANA
        self.lista_selects = []
        path1 = resource_path(r'.\img.png')
        path2 = resource_path(r'.\logo.png')
        path3 = resource_path(r'.\password.png')
        self.imagen = tk.PhotoImage(file=path1)
        self.logo = tk.PhotoImage(file=path2)
        self.logo2 = tk.PhotoImage(file=path3)

        self.labelframe = tk.LabelFrame(self.master, font=(
            'Courier', 25, 'bold', 'italic'), relief='ridge', bd=5, fg='orange')  # CONTENEDOR LABELFRAME DE TODO EL CONTENIDO DE LA SEGUNDA VENTANA

        self.desplegar_tablas = ttk.Combobox(
            self.labelframe, state='readonly', font='Verdana 25 normal italic', height=4)
        self.desplegar_tablas['values'] = self.db.tablas
        self.desplegar_tablas.set(f'{nameTabla}')
        self.desplegar_tablas.bind('<<ComboboxSelected>>', lambda x: self.rellenar_datos(
            self.desplegar_tablas.get(), self.db))
        self.desplegar_tablas.grid(row=0, column=1, sticky='nsew', pady=30)

        # CONFIGURACION DE COLUMNAS Y FILAS DEL LABELFRAME
        self.labelframe.columnconfigure(0, weight=1)
        self.labelframe.columnconfigure(1, weight=1)
        self.labelframe.columnconfigure(2, weight=1)
        self.labelframe.columnconfigure(3, weight=3)
        self.labelframe.columnconfigure(4, weight=1)
        self.labelframe.columnconfigure(5, weight=1)
        self.labelframe.rowconfigure(1, weight=1)
        self.labelframe.rowconfigure(2, weight=1)
        self.labelframe.rowconfigure(3, weight=1)

        # APLICAR ESTILOS-COLORES A WIDGETS TEMATICOS COMO TREEVIEW-SCROLLBAR-COMBOBOX
        estilo_tabla = ttk.Style()
        estilo_tabla.theme_use('alt')
        estilo_tabla.configure("Treeview", font=(
            'Cascadia Code PL', 12, 'normal', 'italic'), foreground='black', rowheight=35)
        estilo_tabla.map('Treeview', background=[
                         ('selected', 'blue')], foreground=[('selected', 'white')])
        estilo_tabla.configure('Heading', background='white',
                               foreground='red1', padding=3, font=('Courier', 14, 'bold'))
        estilo_tabla.configure('TScrollbar', arrowcolor='green',
                               bordercolor='blue', troughcolor='orange1', background='orange')
        estilo_tabla.map('TScrollbar', background=[('active', 'orange')])
        estilo_tabla.configure(
            'TCombobox', foreground='black', selectforeground='red', selctbackground='transparent')

        # FRAME QUE CONTIENE EL TREWIEW CON LOS SCROLLBAR
        self.frame_tabla = tk.Frame(
            self.labelframe, bd=3, relief='ridge', bg='skyblue')

        self.tabla_credenciales = ttk.Treeview(
            self.frame_tabla, show='headings')  # TABLA DE DATOS
        self.scroll_y = ttk.Scrollbar(
            self.frame_tabla, orient='vertical', command=self.tabla_credenciales.yview)
        self.scroll_x = ttk.Scrollbar(
            self.frame_tabla, orient='horizontal', command=self.tabla_credenciales.xview)

        self.tabla_credenciales.tag_configure('gray', background='gray')
        self.tabla_credenciales.tag_configure('skyblue', background='skyblue')

        self.tabla_credenciales.config(
            yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set)

        self.tabla_credenciales['columns'] = (
            'NOMBRE', 'CORREO O NUMERO', 'CONTRASEÑA')
        self.tabla_credenciales.column('NOMBRE', minwidth=350, anchor='w')
        self.tabla_credenciales.column(
            'CORREO O NUMERO', minwidth=380, anchor='w')
        self.tabla_credenciales.column('CONTRASEÑA', minwidth=350, anchor='w')

        self.tabla_credenciales.heading('NOMBRE', text='NOMBRE')
        self.tabla_credenciales.heading(
            'CORREO O NUMERO', text='CORREO O NUMERO')
        self.tabla_credenciales.heading('CONTRASEÑA', text='CONTRASEÑA')

        # CONFIGURACION DEL FRAME TABLA PARA DARLES PESO A SUS COLUMNAS O FILAS
        self.frame_tabla.columnconfigure(0, weight=1)
        self.frame_tabla.columnconfigure(1, weight=1)
        self.frame_tabla.rowconfigure(0, weight=1)

        self.tabla_credenciales.grid(
            row=0, column=0, sticky='nsew', columnspan=2)
        self.scroll_y.grid(row=0, column=2, sticky='nsew')
        self.scroll_x.grid(row=1, column=0, sticky='nsew', columnspan=2)

        # BOTON QUE RETORNA A LA PRIMERA VENTANA
        self.btn_return = tk.Button(self.labelframe, text='HOME', font='verdana 15 bold italic', command=lambda: [
                                    self.master.destroy(), self.master.quit(), main()], anchor='e')
        self.btnDeleteTabla = tk.Button(self.labelframe, text='ELIMINAR TABLA', font='verdana 15 normal italic', fg='red',
                                        activeforeground='red', command=lambda: self.answer_delete(self.desplegar_tablas.get())
                                        )

        # FRAME QUE CONTINE DOS BOTONES UNO PARA AGREGAR UNA CREDENCIAL Y OTRO PARA ELIMINAR CREDENCIAL
        self.frame_botones = tk.Frame(
            self.labelframe, bg='skyblue', relief='ridge', bd=3)
        self.btn_del = tk.Button(self.frame_botones, text='-', relief='ridge', bd=1, width=8,
                                 font='none 14 bold italic', state='disabled', command=lambda: self.eliminarFila(self.desplegar_tablas.get()))
        self.btn_add = tk.Button(self.frame_botones, text='+', relief='ridge', bd=1, width=8, font='none 14 bold italic', command=lambda: self.add_update('NUEVA', 'AGREGAR', lambda: self.insertOrUpdateCredencial(self.desplegar_tablas.get()))
                                 )
        self.btn_update = tk.Button(self.frame_botones, text='ACTUALIZAR', relief='ridge', bd=1, width=8, font='courier 10 bold italic', command=lambda: self.add_update(
            'ACTUALIZA\nCREDENCIAL', 'ACTUALIZAR', lambda: self.insertOrUpdateCredencial(self.desplegar_tablas.get(), 'U'), nameTabla), state='disabled')
        self.btn_del.pack(side='left')
        self.btn_add.pack(side='right')
        self.btn_update.pack(side='right', expand=1, fill='both')

        # UBICACION EN EL FRAME PRINCIPAL SELF
        self.btn_return.grid(row=0, column=3, sticky='ne', pady=20)
        self.btnDeleteTabla.grid(
            row=0, column=4, columnspan=2, sticky='ns', pady=20)
        self.frame_tabla.grid(row=1, column=0, columnspan=4,
                              sticky='nsew', rowspan=3, padx=5)
        self.frame_botones.grid(row=4, column=3, sticky='nsew', padx=5)

        # FRAME EDIT DE LA TABLA DE CREDENCIALES
        self.frame_edit = tk.Frame(
            self.labelframe, relief='ridge', bd=3, bg='skyblue')
        self.frame_edit.grid(row=1, column=4, rowspan=4,
                             sticky='nsew', columnspan=2)
        # ----
        self.logo_password = tk.Frame(self.frame_edit)
        self.logo_password.pack(side='top', fill='both',
                                expand=1, padx=5, pady=2)
        label_password = tk.Label(self.logo_password, image=self.logo2)
        label_password.pack(side='top', fill='both', expand=1)
        # ................
        self.logo_create = tk.Frame(self.frame_edit)
        self.logo_create.pack(side='bottom', fill='both',
                              expand=1, padx=5, pady=2)
        label_create = tk.Label(self.logo_create, image=self.logo)
        label_create.pack(side='bottom', fill='both', expand=1)
        # -------------------------------------------------------------------
        # LLAMADA AL METODO RELLENAR DATOS
        self.rellenar_datos(nameTabla, self.db)

        # eventos
        self.labelframe.bind(
            '<Button-1>', lambda x: self.tabla_credenciales.selection_remove(self.tabla_credenciales.selection()))
        self.tabla_credenciales.bind(
            '<<TreeviewSelect>>', lambda x: self.activar_botones(self.desplegar_tablas.get()))
        self.master.bind(
            '<Control-a>', lambda x: self.event_Add(self.desplegar_tablas.get()))
        self.master.bind(
            '<Control-u>', lambda x: self.event_Update(self.desplegar_tablas.get()))
        self.master.bind(
            '<Control-d>', lambda x: self.event_Delete(self.desplegar_tablas.get()))
        self.popup()
        self.tabla_credenciales.tag_bind(
            'click', '<Button-3>', lambda x: self.abrir_menu(x))

        # self.tabla_credenciales.event_add('<<Button-1>>', '<Button-3>')
        # self.tabla_credenciales.bind('<<TreviewSelect>>', lambda x: print('Seleccionado'))
        # self.master.bind('<Configure>')
        # UBICACION DEL LABELFRAME PRINCIPAL EN EL MASTER
        self.labelframe.pack(side='top', expand=1, fill='both', padx=4, pady=5)

    def mover_datos(self, nameTablaActual, nameTablaDestino) :

        seleccion = self.tabla_credenciales.selection()
        filas = []

        for id in seleccion :
            fila = self.db.read(
                F'SELECT * FROM {nameTablaActual!r} WHERE ID={id}')
            filas.extend(fila)

        self.db.delete(seleccion, nameTablaActual)
        self.tabla_credenciales.delete(*seleccion)
        
        for row in filas :
            last_id = self.db.ultimo_id(nameTablaDestino)
            row = list(row)
            row[0] = last_id
            self.db.write(nameTablaDestino, row)
        
        self.rellenar_datos(nameTablaActual, self.db)


    # METODO QUE CREARA LA VENTANA DE OPCIONES PARA ESCOGER DONDE MOVER LOS DATOS

    def select_tabla(self):

        ventana = tk.Toplevel(self.master, highlightthickness=5, highlightbackground='DarkOrchid1',
                              highlightcolor='DarkOrchid1', relief='ridge', bd=5)
        ventana.overrideredirect(1)
        ventana.focus_set()

        var_tabla = tk.StringVar()

        ancho, alto = self.master.winfo_width(), self.master.winfo_height()
        posx, posy = self.master.winfo_x(), self.master.winfo_y()
        x, y = posx + 15 + (ancho - 350) // 2, (posy + (alto - 200) // 2)
        ventana.geometry(f'350x200+{x}+{y - 40}')

        
        label = tk.Label(ventana, text= 'Seleciona La Tabla Destino', fg='blue', bg='white',
                      relief='ridge', bd=2, font=('courier', 12, 'bold', 'italic'))
        label.pack(pady=20)

        tablas = ttk.Combobox(ventana, textvariable= var_tabla)
        tablas['values'] = self.db.tablas
        tablas.set(self.db.tablas[0])
        tablas.pack(pady=20, padx=20)
        tablas.focus_set()

        boton_realizar_fitro = tk.Button(ventana, highlightthickness=3, highlightcolor='yellow', text='MOVER', fg='white', bg='limegreen',
                                      command=ventana.destroy, activebackground='lime', activeforeground='white', font=('courier', 12, 'bold', 'italic'))
        boton_realizar_fitro.pack(side='right', padx=30)

        tablas.bind('<Return>', lambda e: ventana.destroy())

        # ventana.transient(self.tabla_uno)
        ventana.grab_set()

        self.master.wait_window(ventana)

        self.mover_datos(self.desplegar_tablas.get(), var_tabla.get())

    # METODO QUE CREARA EL MENU CONTEXTUAL

    def popup(self):
        self.popup_menu = tk.Menu(self.master,
                                  tearoff=0)

        self.popup_menu.add_command(label="Mover A Tabla",
                                    command=self.select_tabla, foreground='blue', font='"Cascadia Code PL" 13 normal')
        self.popup_menu.add_separator()
        self.popup_menu.add_separator()

        self.popup_menu.add_command(label="Eliminar",
                                    command= lambda : [ print('Se Ejecuto La Funcion'), self.eliminarFila(self.desplegar_tablas.get())], foreground='blue', font='"Cascadia Code PL" 13 normal')
        self.popup_menu.add_separator()
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label="Duplicar Y Modificar",
                                                    command=lambda: self.duplicar_modificar(), foreground='blue', font='"Cascadia Code PL" 13 normal', state='disabled')



    def do_popup(self, event):
        try:

            if len(self.tabla_credenciales.selection()) == 1:
                self.popup_menu.entryconfig(6, state='normal')
                
            else :
                self.popup_menu.entryconfig(6, state='disabled')

            self.popup_menu.tk_popup(event.x_root,
                                     event.y_root)
        finally:
            self.popup_menu.grab_release()

    # METODO QUE SE ENCARGAR DE DUPLICAR UNA CREDENCIAL PERMITIENDO AGREGARLA MODIFICANDO ALGUN DATO

    def duplicar_modificar(self):

        self.add_update('Nueva', 'AGREGAR', lambda: self.insertOrUpdateCredencial(
            self.desplegar_tablas.get()), nameTabla=self.desplegar_tablas.get(), modificar=True)

    # METODO PARA ABRIR EL MENU CONTEXTUAL AL DAR CLICK DERECHO SOBRE ITEMS DE LA VISTA DE ARBOL

    def abrir_menu(self, event):

        # print(dir(event))
        print(self.tabla_credenciales.selection())
        print('==========================')
        self.do_popup(event)

    # METODO QUE PREGUNTARA AL USUARIO SI DESEA REALMENTE ELIMINAR LA TABLA

    def answer_delete(self, nameTabla):

        if messagebox.askyesno(message=f'Esta seguro que deseas eliminar La Tabla {nameTabla!r}'):

            self.db.deleteTabla(self.desplegar_tablas.get())
            self.master.destroy()
            self.master.quit()
            main()

    # METODO QUE CREA EL FRAME DE INSERTAR NUEVA CREDENCIAL O ACTUALIZAR UNA CREDENCIAL

    def add_update(self, titulo, boton, commando=None, nameTabla=None, modificar=False):

        try:
            self.frame_add_credencial.pack_forget()
        except:
            pass

        self.logo_password.pack_forget()

        self.var_btn_key = tk.StringVar()
        self.varName = tk.StringVar()
        self.varCorreo = tk.StringVar()
        self.var_error1 = tk.StringVar()
        self.var_error2 = tk.StringVar()
        self.var_error3 = tk.StringVar()

        if boton == 'ACTUALIZAR' or modificar:
            id = self.tabla_credenciales.selection()
            fila = self.db.read(
                F'SELECT * FROM {nameTabla} WHERE ID="{id[0]}"')
            self.varName.set(fila[0][1])
            self.varCorreo.set(fila[0][2])
            self.var_btn_key.set(fila[0][3])

        self.frame_add_credencial = tk.Frame(
            self.frame_edit, bg='skyblue', bd=3, relief='ridge')
        # ||||
        self.frame_add_credencial.columnconfigure(0, weight=1)
        self.frame_add_credencial.columnconfigure(1, weight=1)
        self.frame_add_credencial.columnconfigure(2, weight=1)
        self.frame_add_credencial.columnconfigure(4, weight=1)
        # ||||
        self.new = tk.Label(self.frame_add_credencial, text=titulo, font='verdana 12 bold',
                            fg='blue', bg='skyblue', bd=3, relief='ridge', justify='center')
        self.label1 = tk.Label(self.frame_add_credencial, text='NOMBRE',
                               fg='blue', font='verdana 10 bold', bg='skyblue')
        self.nombre_credencial = tk.Entry(
            self.frame_add_credencial, textvariable=self.varName, font='verdana 11 normal italic')
        self.error1 = tk.Label(self.frame_add_credencial, font='verdana 6 normal italic',
                               bg='skyblue', fg='red', textvariable=self.var_error1)
        self.label2 = tk.Label(self.frame_add_credencial, text='CORREO O NUMERO',
                               fg='blue', font='verdana 10 bold', bg='skyblue')
        self.correo_credencial = tk.Entry(
            self.frame_add_credencial, textvariable=self.varCorreo, font='verdana 11 normal italic')
        self.error2 = tk.Label(self.frame_add_credencial, font='verdana 6 normal italic',
                               bg='skyblue', fg='red', textvariable=self.var_error2)
        self.label3 = tk.Label(self.frame_add_credencial, text='CONTRASEÑA',
                               fg='blue', font='verdana 10 bold', bg='skyblue')
        self.key_credencial = tk.Entry(
            self.frame_add_credencial, textvariable=self.var_btn_key, font='verdana 11 normal italic')
        self.img_crear_key = tk.Button(self.frame_add_credencial, image=self.imagen,
                                       anchor='w', relief='flat', bd=1, command=self.crear_contraseña, bg='limegreen', activebackground='limegreen')
        self.error3 = tk.Label(self.frame_add_credencial, font='verdana 6 normal italic',
                               bg='skyblue', fg='red', textvariable=self.var_error3)
        self.btn = tk.Button(self.frame_add_credencial,
                             text=boton, command=commando)

        self.btn_cancel = tk.Button(self.frame_add_credencial, text='Cancelar', command=lambda: [self.frame_add_credencial.pack_forget(), self.logo_password.pack(
            side='top', fill='both', expand=1, padx=5, pady=2)])

        self.new.grid(row=0, columnspan=3, column=1, pady=15,
                      sticky='nsew', padx=50, ipady=8)
        self.label1.grid(row=1, column=1, columnspan=3, sticky='nsew', pady=7)
        self.nombre_credencial.grid(
            row=2, column=1, columnspan=3, sticky='nsew', ipady=2)
        self.error1.grid(row=3, column=1, columnspan=3, sticky='ne')
        self.label2.grid(row=4, column=1, columnspan=3, sticky='nsew', pady=5)
        self.correo_credencial.grid(
            row=5, column=1, columnspan=3, sticky='nsew', ipady=2)
        self.error2.grid(row=6, column=1, columnspan=3, sticky='ne')
        self.label3.grid(row=7, column=1, columnspan=3, sticky='nsew', pady=5)
        self.key_credencial.grid(row=8, column=1, columnspan=2, sticky='nsew')
        self.img_crear_key.grid(row=8, column=3)
        self.error3.grid(row=9, column=1, columnspan=3, sticky='ne')
        self.btn.grid(row=10, column=1, columnspan=1,
                      pady=15, sticky='nsew', padx=1)
        self.btn_cancel.grid(row=10, column=2, pady=15,
                             sticky='nsew', columnspan=2, padx=1)

        # EVENTOS A LAS WIDGETS DE ENTRADA
        self.master.bind_class('Entry', '<Control-a>', lambda _: None)
        self.nombre_credencial.bind(
            '<Control-c>', lambda _: self.copiarContenido(self.nombre_credencial))
        self.correo_credencial.bind(
            '<Control-c>', lambda _: self.copiarContenido(self.correo_credencial))
        self.key_credencial.bind(
            '<Control-c>', lambda _: self.copiarContenido(self.key_credencial))

        self.frame_add_credencial.pack(
            side='top', fill='both', expand=0, padx=5)

    # METODO QUE CREA EL FRAME CON OPCIONES PARA GENERAR UNA CONTRASEÑA SEUDOALEATORIA

    def crear_contraseña(self):

        try:
            self.frame_crear_credencial.pack_forget()
        except:
            pass

        self.logo_create.pack_forget()

        # ----
        self.var_num = tk.BooleanVar()
        self.var_mayus = tk.BooleanVar(value=1)
        self.var_minus = tk.BooleanVar()
        self.var_char = tk.BooleanVar()
        self.key = tk.StringVar()
        self.frame_crear_credencial = tk.Frame(
            self.frame_edit, bg='limegreen', bd=3, relief='ridge')
        self.frame_crear_credencial.columnconfigure(0, weight=1)
        self.frame_crear_credencial.columnconfigure(1, weight=1)
        self.frame_crear_credencial.rowconfigure(5, weight=1)

        self.titulo = tk.Label(self.frame_crear_credencial, text='Selecciona los items\nque deseas que contenga\ntu contraseña',
                               justify='center', font='Courier 10 bold italic', bg='limegreen')
        self.item1 = tk.Checkbutton(self.frame_crear_credencial, anchor='w', text='  MAYUSCULAS',
                                    variable=self.var_mayus, onvalue=1, offvalue=0, bg='limegreen', font='Courier 10 normal italic')
        self.item2 = tk.Checkbutton(self.frame_crear_credencial, anchor='w', text='  minusculas',
                                    variable=self.var_minus, onvalue=1, offvalue=0, bg='limegreen', font='Courier 10 normal italic')
        self.item3 = tk.Checkbutton(self.frame_crear_credencial, anchor='w', text='  Numeros',
                                    variable=self.var_num, onvalue=1, offvalue=0, bg='limegreen', font='Courier 10 normal italic')
        self.item4 = tk.Checkbutton(self.frame_crear_credencial, anchor='w', text='  Caracteres\n  Especiales', justify='center',
                                    variable=self.var_char, onvalue=1, offvalue=0, bg='limegreen', font='Courier 10 normal italic')
        self.label_can = tk.Label(
            self.frame_crear_credencial, text='Cantidad', bg='limegreen', font='Courier 10 bold italic')
        self.cantidad = ttk.Combobox(
            self.frame_crear_credencial, height=4, state='readonly')
        self.btn_genera = tk.Button(self.frame_crear_credencial, text='Generar',
                                    font='Courier 10 bold italic', command=self.generar_contraseña)
        self.key_generada = tk.Label(
            self.frame_crear_credencial, bg='limegreen', font='Courier 10 bold italic', textvariable=self.key)
        self.btn_aplicar = tk.Button(self.frame_crear_credencial, text='APLICAR', font='Courier 10 bold italic', command=lambda: [self.var_btn_key.set(
            self.key.get()), self.frame_crear_credencial.pack_forget(), self.logo_create.pack(side='bottom', fill='both', expand=1, padx=5, pady=2)], state='disabled')

        self.cantidad['values'] = tuple(range(4, 21))
        self.cantidad.current(0)

        self.titulo.grid(row=0, column=0, columnspan=2, pady=15, sticky='nsew')
        self.item1.grid(row=1, column=0, sticky='nsew')
        self.item2.grid(row=2, column=0, sticky='nsew')
        self.item3.grid(row=3, column=0, sticky='nsew')
        self.item4.grid(row=4, column=0, sticky='nsew')
        self.label_can.grid(row=1, column=1, sticky='e', padx=10)
        self.cantidad.grid(row=2, column=1, sticky='e')
        self.btn_genera.grid(row=3, column=1, sticky='e', rowspan=2)
        self.key_generada.grid(row=5, column=0, sticky='ew', pady=5)
        self.btn_aplicar.grid(row=5, column=1, sticky='ew', pady=5, padx=10)

        self.frame_crear_credencial.pack(
            side='bottom', fill='both', expand=1, padx=5)

    # METODO QUE RELLENARA EL TREWIEW EXTRAENDO INFORMACION  DE LA BASE DE DATOS EN LA TABLA SELECCIONADA (PARAMETRO nameTabla)

    def rellenar_datos(self, nameTabla, db):

        datos = db.read(f'SELECT * FROM {nameTabla!r}')
        self.tabla_credenciales.delete(*self.tabla_credenciales.get_children())
        print(len(datos))

        for i in range(len(datos)):
            color = 'gray' if i % 2 == 0 else 'skyblue'
            self.tabla_credenciales.insert(
                '', index=0, values=datos[i][1:], tags=[color], iid=datos[i][0])

    # METODO QUE ACTIVA LOS BOTONES DEL FRAME_BOTONES DE ACTUALIZAR Y ELIMINAR CREDENCIAL Y AGREGAR ETIQUETA A ELEMENTOS

    def activar_botones(self, nameTabla):

        fila = self.tabla_credenciales.selection()

        for i in fila:
            if i not in self.lista_selects:
                self.lista_selects.append(i)

        copia = self.lista_selects.copy()

        for item in copia:

            if self.tabla_credenciales.exists(item):
                options = self.tabla_credenciales.item(item)
            else:
                self.lista_selects.remove(item)
                continue

            if 'click' not in options['tags']:
                options['tags'].append('click')

            elif item not in fila:
                self.lista_selects.remove(item)
                # if 'click' in options['tags'] :
                options['tags'].remove('click')

            self.tabla_credenciales.item(item, **options)

        if len(fila) == 1:
            self.btn_del.config(state='normal')
            self.btn_update.config(state='normal')

        elif len(fila) > 1:
            self.btn_del.config(state='normal')
            self.btn_update.config(state='disabled')

        else:
            self.btn_del.config(state='disabled')
            self.btn_update.config(state='disabled')

    # METODO QUE GENERARA LA CONTRASEÑA CON LOS ITEMS SELECCIONADO EN EL FRAME_CREAR_CREDENCIAL

    def generar_contraseña(self):

        lista_items = []
        if self.var_mayus.get():
            lista_items.append('M')
        if self.var_minus.get():
            lista_items.append('m')
        if self.var_num.get():
            lista_items.append('N')
        if self.var_char.get():
            lista_items.append('C')

        if len(lista_items) == 0:
            self.var_minus.set(1)
            lista_items.append('m')

        items = {
            i: 0 for i in lista_items
        }
        long = int(self.cantidad.get())
        shuffle = random.sample(list(items), len(items))

        index = 0
        for i in range(long):
            if index == len(items):
                index = 0
            items[shuffle[index]] += 1
            index += 1

        mayus = string.ascii_uppercase + 'Ñ'
        minus = string.ascii_lowercase + 'ñ'
        num = string.digits
        char = string.punctuation

        mayus = ''.join(random.sample(
            mayus, items['M'])) if 'M' in items else ''
        minus = ''.join(random.sample(
            minus, items['m'])) if 'm' in items else ''
        num = ''.join(random.sample(num, items['N'])) if 'N' in items else ''
        char = ''.join(random.sample(char, items['C'])) if 'C' in items else ''

        generada = list(f'{mayus}{minus}{num}{char}')
        random.shuffle(generada)
        generada = ''.join(generada)
        self.key.set(generada)
        self.btn_aplicar.config(state='normal')

    # METODO QUE INSERTA O ACTUALIZA CREDENCIAL SEGUN EL PARAMETRO MODE I=INSERTAR Y U=ACTUALIZAR
    def insertOrUpdateCredencial(self, nameTabla, mode='I'):

        id = self.db.ultimo_id(nameTabla)
        llave = False

        if len(self.nombre_credencial.get().strip()) == 0 or self.nombre_credencial.get().strip().isspace():
            self.var_error1.set('Completa Este Campo')
            llave = True

        else:
            self.var_error1.set('')

        if len(self.correo_credencial.get().strip()) == 0 or self.correo_credencial.get().strip().isspace():
            self.var_error2.set('Completa Este Campo')
            llave = True

        else:
            self.var_error2.set('')

        if len(self.key_credencial.get().strip()) == 0 or self.key_credencial.get().strip().isspace():
            self.var_error3.set('Completa Este Campo')
            llave = True

        else:
            self.var_error3.set('')

        if not (llave):
            VALUES = [id, self.nombre_credencial.get(
            ), self.correo_credencial.get(), self.key_credencial.get()]
            if mode == 'I':
                self.db.write(nameTabla, VALUES)

            else:
                try:
                    id = self.tabla_credenciales.selection()
                    self.db.update(
                        f'UPDATE {nameTabla} SET TITULO=?, CORREO_O_NUMERO=?, PASSWORD=? WHERE ID="{id[0]}"', VALUES[1:])
                    self.btn_update.config(state='disabled')
                    self.btn_del.config(state='disabled')
                except:
                    messagebox.showerror(
                        'ERROR AL ACTUALIZAR', 'Ha Ocurrido Un Error\nIntentalo De Nuevo')

            self.rellenar_datos(nameTabla, self.db)
            self.frame_add_credencial.pack_forget()
            self.logo_password.pack(
                side='top', fill='both', expand=1, padx=5, pady=2)

            try:
                self.btn_aplicar.config(state='disabled')
                self.btn_genera.config(state='disabled')
            except:
                pass

    # METODO QUE ELIMINA UNA CREDENCIAL TANTO DE LA TABLA COMO DE LA BASE DE DATOS
    def eliminarFila(self, nameTabla):
        print(f'{nameTabla = }')
        seleccion = self.tabla_credenciales.selection()
        self.tabla_credenciales.delete(*seleccion)
        self.db.delete(seleccion, nameTabla)
        self.btn_del.config(state='disabled')
        self.btn_update.config(state='disabled')
        self.rellenar_datos(nameTabla, self.db)

    def event_Add(self, nameTabla):

        self.add_update('NUEVA', 'AGREGAR',
                        lambda: self.insertOrUpdateCredencial(nameTabla), nameTabla)

    def event_Update(self, nameTabla):

        if self.tabla_credenciales.selection():
            self.add_update('ACTUALIZA\nCREDENCIAL', 'ACTUALIZAR',
                            lambda: self.insertOrUpdateCredencial(nameTabla, 'U'), nameTabla)

        else:
            messagebox.showerror('Error Al Actualizar',
                                 'Selecciona la fila\nQue deseas actualizar')

    def event_Delete(self, nameTabla):

        if self.tabla_credenciales.selection():
            self.eliminarFila(nameTabla)

        else:
            messagebox.showerror('Error Al Eliminar',
                                 'No has seleccionado\nNingunda fila')

    def copiarContenido(self, entry):

        if entry.select_present():
            first = entry.index(tk.SEL_FIRST)
            last = entry.index(tk.SEL_LAST)
            texto = entry.get().strip()[first:last]

        else:
            entry.select_range(0, tk.END)
            texto = entry.get().strip()

        self.master.clipboard_clear()
        self.master.clipboard_append(texto)



# EJECUTA LA PRIMERA VENTANA QUE A LA VEZ DESDE LA CLASE INICIO ABRE LA SEGUNDA VENTANA
def main():

    ventana = tk.Tk()
    ventana.config(background='white')
    ventana.geometry('1000x780+250+8')
    ventana.update()
    ventana.minsize(1000, 780)
    ventana.focus_force()
    Inicio(ventana, bg='white')
    ventana.mainloop()


# EJECUTA LA SEGUNDA VENTANA
def segundaVentana(master, nameTabla, db, geometry):

    master.destroy()
    master.quit()
    segunda_Ventana = tk.Tk()
    segunda_Ventana.geometry('1000x780+250+8')
    segunda_Ventana.state('zoomed')
    segunda_Ventana.minsize(1000, 780)
    tablas = Tabla(segunda_Ventana, nameTabla, db)
    segunda_Ventana.focus_force()
    segunda_Ventana.mainloop()


if __name__ == '__main__':

    main()
