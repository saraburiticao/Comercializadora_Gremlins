import tkinter as tk
from tkinter import messagebox

def create_module_window(title, options):
    # Crear ventana principal
    window = tk.Tk()
    window.title(title)

    # Crear botones para cada opción
    for option in options:
        button = tk.Button(window, text=option, command=lambda opt=option: handle_option(opt))
        button.pack(pady=10)
    
    window.mainloop()

def handle_option(option):
    if option == "Gestión de usuarios":
        open_user_management()

    # Agregar manejo para otras opciones aquí

def open_user_management():
    # Aquí irá la implementación para abrir la ventana de gestión de usuarios
    pass
