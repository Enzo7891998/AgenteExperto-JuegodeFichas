from tkinter import Tk, Label, Entry, Button, messagebox, IntVar, Frame
from tkinter.ttk import Separator
from tablero import Tablero
from metodo import resolver_problema
import time

class JuegoFichas:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de las Fichas")

        # Título del juego
        self.titulo = Label(self.root, text="Juego de las Fichas", font=("Helvetica", 16, "bold"), bg="lightblue", fg="black", pady=10)
        self.titulo.grid(row=0, column=0, columnspan=2, sticky="ew")

        # Subtítulo con autores
        self.subtitulo = Label(self.root, text="Creado por Canepa y Zalazar   :O ", font=("Helvetica", 12, "italic"), bg="lightblue", fg="black")
        self.subtitulo.grid(row=1, column=0, columnspan=2, sticky="ew")

        # Separador
        Separator(self.root, orient="horizontal").grid(row=2, column=0, columnspan=2, sticky="ew", pady=5)

        # Instrucciones del juego
        self.instrucciones = Label(self.root, text="Bienvenido al juego de las fichas, el objetivo de este juego es que la ficha roja encuentre el camino más óptimo para llegar a la salida.", font=("Helvetica", 10), bg="grey10", fg="white", wraplength=580, justify="left", pady=10)
        self.instrucciones.grid(row=3, column=0, columnspan=2, sticky="ew")

        self.filas_var = IntVar(value=3)
        self.columnas_var = IntVar(value=4)
        self.ficha_roja_fila_var = IntVar(value=3)
        self.ficha_roja_columna_var = IntVar(value=1)
        self.ficha_amarilla_fila_var = IntVar(value=1)
        self.ficha_amarilla_columna_var = IntVar(value=3)
        self.salida_fila_var = IntVar(value=1)
        self.salida_columna_var = IntVar(value=4)
        self.limite_movimientos_var = IntVar(value=20)

        self.crear_interfaz()

    def crear_interfaz(self):
        self.config_frame = Frame(self.root, bd=2, relief="solid", padx=10, pady=10, bg="lightgray")
        self.config_frame.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

        Label(self.config_frame, text="Número de filas", font=("Times New Roman", 10), borderwidth=0.2, bg="lightgray", fg="black").grid(row=0, column=0, sticky="w")
        Entry(self.config_frame, textvariable=self.filas_var, highlightthickness=1, bd=0, bg="gray98", fg="black", highlightbackground="black").grid(row=0, column=1, sticky="ew")

        Label(self.config_frame, text="Número de columnas", font=("Times New Roman", 10), borderwidth=0.2, bg="lightgray", fg="black").grid(row=1, column=0, sticky="w")
        Entry(self.config_frame, textvariable=self.columnas_var, highlightthickness=1, bd=0, bg="gray98", fg="black", highlightbackground="black").grid(row=1, column=1, sticky="ew")

        Button(self.config_frame, text="Configurar Tablero", command=self.configurar_tablero, font=("Verdana", 8), bg="green").grid(row=2, column=0, columnspan=2, pady=5)

        Label(self.config_frame, text="Ficha Roja -Fila", font=("Times New Roman", 10), borderwidth=0.2, bg="lightgray", fg="black").grid(row=3, column=0, sticky="w")
        Entry(self.config_frame, textvariable=self.ficha_roja_fila_var, highlightthickness=1, bd=0, bg="gray98", fg="black", highlightbackground="black").grid(row=3, column=1, sticky="ew")

        Label(self.config_frame, text="Ficha Roja -Columna", font=("Times New Roman", 10), borderwidth=0.2, bg="lightgray", fg="black").grid(row=4, column=0, sticky="w")
        Entry(self.config_frame, textvariable=self.ficha_roja_columna_var, highlightthickness=1, bd=0, bg="gray98", fg="black", highlightbackground="black").grid(row=4, column=1, sticky="ew")

        Label(self.config_frame, text="Ficha Amarilla -Fila", font=("Times New Roman", 10), borderwidth=0.2, bg="lightgray", fg="black").grid(row=5, column=0, sticky="w")
        Entry(self.config_frame, textvariable=self.ficha_amarilla_fila_var, highlightthickness=1, bd=0, bg="gray98", fg="black", highlightbackground="black").grid(row=5, column=1, sticky="ew")

        Label(self.config_frame, text="Ficha Amarilla -Columna", font=("Times New Roman", 10), borderwidth=0.2, bg="lightgray", fg="black").grid(row=6, column=0, sticky="w")
        Entry(self.config_frame, textvariable=self.ficha_amarilla_columna_var, highlightthickness=1, bd=0, bg="gray98", fg="black", highlightbackground="black").grid(row=6, column=1, sticky="ew")

        Label(self.config_frame, text="Casilla de Salida -Fila", font=("Times New Roman", 10), borderwidth=0.2, bg="lightgray", fg="black").grid(row=7, column=0, sticky="w")
        Entry(self.config_frame, textvariable=self.salida_fila_var, highlightthickness=1, bd=0, bg="gray98", fg="black", highlightbackground="black").grid(row=7, column=1, sticky="ew")

        Label(self.config_frame, text="Casilla de Salida - Columna", font=("Times New Roman", 10), borderwidth=0.2, bg="lightgray", fg="black").grid(row=8, column=0, sticky="w")
        Entry(self.config_frame, textvariable=self.salida_columna_var, highlightthickness=1, bd=0, bg="gray98", fg="black", highlightbackground="black").grid(row=8, column=1, sticky="ew")

        Label(self.config_frame, text="Límite de Movimientos", font=("Times New Roman", 10), borderwidth=0.2, bg="lightgray", fg="black").grid(row=9, column=0, sticky="w")
        Entry(self.config_frame, textvariable=self.limite_movimientos_var, highlightthickness=1, bd=0, bg="gray98", fg="black", highlightbackground="black").grid(row=9, column=1, sticky="ew")

        Button(self.config_frame, text="Iniciar Juego", command=self.iniciar_juego, highlightthickness=1, font=("Verdana", 10), bd=0.2, bg="green", fg="black", highlightbackground="black").grid(row=10, column=0, columnspan=2, pady=5)

    def configurar_tablero(self):
        filas = self.filas_var.get()
        columnas = self.columnas_var.get()

        if hasattr(self, 'tablero_frame'):
            self.tablero_frame.destroy()

        self.tablero_frame = Frame(self.root, bd=2, relief="sunken", padx=10, pady=10, bg="black")
        self.tablero_frame.grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

    def iniciar_juego(self):
        try:
            self.tablero = Tablero(self.filas_var.get(), self.columnas_var.get())
            self.tablero.configurar_ficha_roja(self.ficha_roja_fila_var.get() - 1, self.ficha_roja_columna_var.get() - 1)
            self.tablero.configurar_ficha_amarilla(self.ficha_amarilla_fila_var.get() - 1, self.ficha_amarilla_columna_var.get() - 1)
            self.tablero.configurar_salida(self.salida_fila_var.get() - 1, self.salida_columna_var.get() - 1)
            self.limite_movimientos = self.limite_movimientos_var.get()

            self.mostrar_tablero()
            resultado = resolver_problema(self.tablero, self.limite_movimientos, self)

            if resultado is not None:
                messagebox.showinfo("Fin del juego", "¡Problema resuelto!\nCamino Óptimo de la ficha roja encontrado: " + str(resultado))
            else:
                messagebox.showinfo("Fin del juego", "No se pudo resolver el problema o se alcanzó el límite de movimientos")

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def mostrar_tablero(self):
        for widget in self.tablero_frame.winfo_children():
            widget.destroy()

        filas = self.filas_var.get()
        columnas = self.columnas_var.get()

        for i in range(filas):
            self.tablero_frame.grid_rowconfigure(i, weight=1)
            for j in range(columnas):
                self.tablero_frame.grid_columnconfigure(j, weight=1)
                if (i, j) == self.tablero.ficha_roja:
                    Label(self.tablero_frame, text="R", width=3, height=2, bg="red", relief="raised").grid(row=i, column=j, sticky="nsew", padx=1, pady=1)
                elif (i, j) == self.tablero.ficha_amarilla:
                    Label(self.tablero_frame, text="A", width=3, height=2, bg="yellow", relief="raised").grid(row=i, column=j, sticky="nsew", padx=1, pady=1)
                elif (i, j) == self.tablero.salida:
                    Label(self.tablero_frame, text="S", width=3, height=2, bg="green", relief="raised").grid(row=i, column=j, sticky="nsew", padx=1, pady=1)
                else:
                    Label(self.tablero_frame, text=".", width=3, height=2, relief="raised").grid(row=i, column=j, sticky="nsew", padx=1, pady=1)
        self.root.update()

if __name__ == "__main__":
    root = Tk()
    root.geometry("600x800")
    app = JuegoFichas(root)
    root.mainloop()
