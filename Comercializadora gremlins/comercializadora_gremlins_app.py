import tkinter as tk
from tkinter import font

def on_role_selected(role):
    print(f"Rol seleccionado: {role}")

def on_exit():
    root.destroy()

root = tk.Tk()
root.title("Comercializadora Gremlins")
root.geometry("600x400")

# Configuración del título principal
frame = tk.Frame(root, padx=20, pady=20, relief="solid", bd=2)
frame.pack(expand=True)

titulo_font = font.Font(family="Helvetica", size=16, weight="bold")
titulo = tk.Label(frame, text="COMERCIALIZADORA GREMLINS", font=titulo_font)
titulo.pack(pady=10)

bienvenido_font = font.Font(family="Helvetica", size=12, weight="bold")
bienvenido = tk.Label(frame, text="Bienvenidos", font=bienvenido_font)
bienvenido.pack(pady=10)

# Configuración del mensaje de selección de rol
seleccion_font = font.Font(family="Helvetica", size=10, weight="bold")
seleccion_label = tk.Label(frame, text="Seleccione su rol.", font=seleccion_font)
seleccion_label.pack(pady=10)

# Configuración de los botones de rol
roles = ["Gerente", "Administrador", "Empacador", "Transportador", "Recepción"]

button_frame = tk.Frame(frame)
button_frame.pack(pady=10)

for rol in roles:
    button = tk.Button(button_frame, text=rol, command=lambda r=rol: on_role_selected(r), padx=10, pady=5)
    button.pack(side=tk.LEFT, padx=5)

# Botón de salir
salir_button = tk.Button(frame, text="Salir", command=on_exit, padx=10, pady=5)
salir_button.pack(pady=20)

root.mainloop()