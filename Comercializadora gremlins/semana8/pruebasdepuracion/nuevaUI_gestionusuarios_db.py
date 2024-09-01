import tkinter as tk
from tkinter import font, ttk
from database import get_users

# Funciones para abrir las ventanas de gestión
def open_user_management():
    user_window = tk.Toplevel(root)
    user_window.title("Gestión de Usuarios")
    user_window.geometry("600x400")

    title_font = font.Font(family="Helvetica", size=14, weight="bold")
    title_label = tk.Label(user_window, text="Gestión de Usuarios", font=title_font)
    title_label.pack(pady=10)

    # Crear un árbol (Treeview) para mostrar los datos
    tree = ttk.Treeview(user_window, columns=("ID", "Nombre", "Cargo"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Cargo", text="Cargo")
    tree.pack(expand=True, fill="both")

    # Obtener los datos de la base de datos
    users = get_users()
    for user in users:
        tree.insert("", tk.END, values=user)

    close_button = tk.Button(user_window, text="Cerrar", command=user_window.destroy, padx=20, pady=10)
    close_button.pack(pady=20)

def open_inventory_management():
    # Implementa la lógica para la gestión de inventarios aquí
    pass

def open_reports_management():
    # Implementa la lógica para la generación de reportes aquí
    pass

def open_packing_management():
    # Implementa la lógica para la gestión de empaques aquí
    pass

def open_transport_management():
    # Implementa la lógica para la gestión de transporte aquí
    pass

def open_reception_management():
    # Implementa la lógica para la gestión de recepción aquí
    pass

# Función para crear la ventana del módulo de administración
def open_admin_management():
    create_module_window(
        title="Módulo de Administración",
        options=["Gestión de usuarios", "Administración de inventarios", "Generación de reportes"],
        open_user_management_callback=open_user_management
    )

# Función genérica para crear una ventana de módulo
def create_module_window(title, options, open_user_management_callback=None):
    module_window = tk.Toplevel(root)
    module_window.title(title)
    module_window.geometry("600x400")

    title_font = font.Font(family="Helvetica", size=14, weight="bold")
    title_label = tk.Label(module_window, text=title, font=title_font)
    title_label.pack(pady=10)

    for option in options:
        if option == "Gestión de usuarios" and open_user_management_callback:
            button = tk.Button(module_window, text=option, padx=20, pady=10, command=open_user_management_callback)
        elif option == "Administración de inventarios":
            button = tk.Button(module_window, text=option, padx=20, pady=10, command=open_inventory_management)
        elif option == "Generación de reportes":
            button = tk.Button(module_window, text=option, padx=20, pady=10, command=open_reports_management)
        elif option == "Gestión de empaques":
            button = tk.Button(module_window, text=option, padx=20, pady=10, command=open_packing_management)
        elif option == "Gestión de transporte":
            button = tk.Button(module_window, text=option, padx=20, pady=10, command=open_transport_management)
        elif option == "Gestión de recepción":
            button = tk.Button(module_window, text=option, padx=20, pady=10, command=open_reception_management)
        else:
            button = tk.Button(module_window, text=option, padx=20, pady=10)
        button.pack(pady=10)

    close_button = tk.Button(module_window, text="Cerrar", command=module_window.destroy, padx=20, pady=10)
    close_button.pack(pady=20)

# Función para manejar la selección de roles
def on_role_selected(role):
    if role == "Gerente":
        open_admin_management()
    elif role == "Administrador":
        open_admin_management()
    elif role == "Empacador":
        open_packing_management()
    elif role == "Transportador":
        open_transport_management()
    elif role == "Recepción":
        open_reception_management()
    else:
        print("Rol desconocido")

# Función para salir de la aplicación
def on_exit():
    root.destroy()

# Configuración de la ventana principal
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

