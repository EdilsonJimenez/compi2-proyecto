from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog as FiledDialog
from tkinter import ttk
from io import open

#Parte de Importaciones para el analisis etc
import interprete as Inter
import Ast2 as ast

# ------------------------------------------- VENTANA PRINCIPAL ------------------------------------------------------ #
class Aplicacion:

# ruta del fichero
    ruta = ""
# ----------------------------------------- FUNCIONES MENU ARCHIVO --------------------------------------------------- #
    def nuevo(self):
        global ruta
        ruta = ""
        # Borra desde el primer caracter hasta el final del texto.
        self.entrada.delete(1.0, "end")
        self.miVentana.title("TytusDB G16")

    def abrir(self):
        global ruta
        ruta = FiledDialog.askopenfilename(initialdir='.', filetype=(("Archivos SQL", "*.sql"),), title="Abrir")
        if ruta != "":
            fichero = open(ruta, 'r')
            contenido = fichero.read()
            self.entrada.delete(1.0, "end")
            self.entrada.insert('insert', contenido)
            fichero.close()
            self.miVentana.title(ruta + " - TytusDB G16")

    def guardar(self):
        # Si tiene una ruta
        if ruta != "":
            contenido = self.entrada.get(1.0, "end")
            fichero = open(ruta, 'w+')
            fichero.write(contenido)
            fichero.close()
            # Mensaje de que se guardo el archivo.
        # Si no tiene una ruta
        else:
            self.guardarComo()

    def guardarComo(self):
        global ruta
        fichero = FiledDialog.asksaveasfile(title="Guardar archivo", mode="w", defaultextension=".sql")
        if fichero is not None:  # Si no se cancela
            ruta = fichero.name  # guardamos ruta accediendo con name
            contenido = self.entrada.get(1.0, "end-1c")  # se lee sin el ultimo caracter
            fichero = open(ruta, 'w+')
            fichero.write(contenido)
            fichero.close()
        else:
            ruta = ""



    def enviarDatos(self):
        contenido = self.entrada.get(1.0, "end-1c")
        self.consola.insert('insert', contenido)
        Inter.inicializarEjecucionAscendente(contenido)



    def Seleccionar(self):
        cadena=""
        cadena2=""

        try:
            cadena = self.entrada.get(SEL_FIRST, SEL_LAST)
            Inter.inicializarEjecucionAscendente(cadena)
            self.consola.insert('insert', cadena)
            print("Estoy Ejecutando valor Selecccionado")

        except:
            cadena2 = self.entrada.get(1.0, "end-1c")
            Inter.inicializarEjecucionAscendente(cadena2)
            self.consola.insert('insert', cadena2)
            print("Estoy Ejecutando  los datos encontrados")





    def GraficarArbol(self):
        ast.Graficar()
        self.consola.insert('insert', "Exito Al Graficar")






    def __init__(self):
        self.miVentana = Tk()
        self.miVentana.title("TytusDB G16")
        self.miVentana.config(bd=3)
        self.miVentana.state('zoomed')

        # Menu
        self.barraMenu = Menu(self.miVentana)

        self.menuArchivo = Menu(self.barraMenu, tearoff=0)
        self.menuArchivo.add_command(label="Nuevo", command=self.nuevo)
        self.menuArchivo.add_command(label="Abrir", command=self.abrir)
        self.menuArchivo.add_command(label="Guardar", command=self.guardar)
        self.menuArchivo.add_command(label="Guardar Como", command=self.guardarComo)
        self.menuArchivo.add_separator()
        self.menuArchivo.add_command(label="Salir de TytusDB", command=self.miVentana.quit())

        self.menuAnalizar = Menu(self.barraMenu, tearoff=0)
        #self.menuAnalizar.add_command(label="Run", command=self.enviarDatos)
        self.menuAnalizar.add_command(label="Ejecucion", command=self.Seleccionar)
        self.menuAnalizar.add_command(label="Graficar Arbol" ,command=self.GraficarArbol)

        self.barraMenu.add_cascade(menu=self.menuArchivo, label="Archivo")
        self.barraMenu.add_cascade(menu=self.menuAnalizar, label="Run")

        # Area de texto
        self.entrada = scrolledtext.ScrolledText(self.miVentana)

        # fill desde la raiz y se expande = True/1
        self.entrada.pack(fill="both", expand=1)
        # Borde de 0px, padding X = 10px, padding Y = 5 y fuente
        self.entrada.config(bd=0, padx=10, pady=5, font=("Consolas", 11))

        self.sepa = ttk.Separator(self.miVentana, orient=HORIZONTAL)
        self.sepa.pack(fill="x", expand=1)

        # Consola salida
        mensaje = StringVar()
        mensaje.set("Consola: ")
        self.labelConsola = Label(self.miVentana, textvar=mensaje, justify='left')
        self.labelConsola.pack(side="left")
        self.consola = scrolledtext.ScrolledText(self.miVentana, width=50, height=10)
        self.consola.pack(fill="both", expand=0)

        # Loop ventana
        self.miVentana.config(menu=self.barraMenu)
        self.miVentana.mainloop()

principal = Aplicacion()
