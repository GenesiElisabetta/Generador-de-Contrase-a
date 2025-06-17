import tkinter as tk
from tkinter import messagebox
import random
import string
# Base de datos simulada
base_datos = {}
# Lista de palabras comunes
palabras_comunes = ["Luz", "Sol", "Gato", "Manzana", "Ferrari", "Libro", "Cielo", "Rojo", "Agua", "Tierra", "Fuego", "Azul", "Hearts", "Favorite"]
# Función: generar contraseña segura
def generar_contraseña():
    longitud = int(entry_longitud.get())
    usar_mayus = var_mayus.get()
    usar_minus = var_minus.get()
    usar_nums = var_nums.get()
    usar_simbolos = var_simbolos.get()
    caracteres = ''
    if usar_mayus:
        caracteres += string.ascii_uppercase
    if usar_minus:
        caracteres += string.ascii_lowercase
    if usar_nums:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation
    if not caracteres:
        messagebox.showerror("Error", "Selecciona al menos un tipo de carácter.")
        return
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    resultado.set(contraseña)
# Función: generar frase secreta
def generar_frase():
    num_palabras = int(entry_palabras.get())
    frase = '-'.join(random.choice(palabras_comunes) for _ in range(num_palabras))
    resultado.set(frase)
# Guardar contraseña
def guardar_contraseña():
    servicio = entry_servicio.get()
    clave = resultado.get()
    if servicio and clave:
        base_datos[servicio] = clave
        messagebox.showinfo("Guardado", f"Contraseña guardada para '{servicio}'.")
    else:
        messagebox.showerror("Error", "Faltan datos.")
# Ver contraseñas guardadas
def ver_guardadas():
    if not base_datos:
        messagebox.showinfo("Sin contraseñas", "No hay contraseñas guardadas.")
    else:
        texto = "\n".join(f"{serv}: {clave}" for serv, clave in base_datos.items())
        messagebox.showinfo("Contraseñas guardadas", texto)
# ---------------- UI ----------------
ventana = tk.Tk()
ventana.title("Gestor de Contraseñas")
ventana.geometry("500x500")
resultado = tk.StringVar()
tk.Label(ventana, text="Generador de Contraseñas", font=("Helvetica", 14, "bold")).pack(pady=10)
# Parámetros
frame = tk.Frame(ventana)
frame.pack(pady=5)
tk.Label(frame, text="Longitud:").grid(row=0, column=0)
entry_longitud = tk.Entry(frame)
entry_longitud.insert(0, "12")
entry_longitud.grid(row=0, column=1)
var_mayus = tk.BooleanVar(value=True)
var_minus = tk.BooleanVar(value=True)
var_nums = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=False)
tk.Checkbutton(frame, text="Mayúsculas", variable=var_mayus).grid(row=1, column=0, sticky="w")
tk.Checkbutton(frame, text="Minúsculas", variable=var_minus).grid(row=1, column=1, sticky="w")
tk.Checkbutton(frame, text="Números", variable=var_nums).grid(row=2, column=0, sticky="w")
tk.Checkbutton(frame, text="Símbolos", variable=var_simbolos).grid(row=2, column=1, sticky="w")
# Botones
tk.Button(ventana, text="Generar Contraseña", command=generar_contraseña, bg="#ccc").pack(pady=5)
tk.Label(ventana, text="Numero de Palabras:").pack()
entry_palabras = tk.Entry(ventana)
entry_palabras.insert(0, "4")
entry_palabras.pack()
tk.Button(ventana, text="Generar Frase Secreta", command=generar_frase, bg="#cfc").pack(pady=5)
tk.Label(ventana, text="Resultado generado:").pack()
tk.Entry(ventana, textvariable=resultado, width=40, font=("Courier", 12)).pack(pady=5)
# Guardar
tk.Label(ventana, text="Nombre de la Plataforma:").pack()
entry_servicio = tk.Entry(ventana)
entry_servicio.pack()
tk.Button(ventana, text="Guardar Contraseña", command=guardar_contraseña, bg="#cfc").pack(pady=5)
tk.Button(ventana, text="Ver Contraseñas Guardadas", command=ver_guardadas, bg="#cff").pack(pady=5)
tk.Button(ventana, text="Salir", command=ventana.destroy, bg="#f88").pack(pady=10)
ventana.mainloop()