import tkinter as tk

def abrir_ventana():
     root = tk.Tk()
     root.title("Convertir .csv de direcciones de Thunderbird a Outlook")
     root.geometry("400x300")
     etiqueta = tk.Label(root, text="Seleccione el archivo .csv a convertir")

