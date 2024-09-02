import tkinter as tk
from tkinter import font, ttk, messagebox
from database import get_users  # Asegúrate de que 'get_users' esté correctamente implementado

# Funciones para abrir diferentes módulos basados en el rol
def open_import_management():
    create_module_window("Gestión de Importaciones - Gerente", 
                         ["Clasificación y gestión de productos importados", 
                          "Asignación y gestión de proveedores ocultos", 
                          "Generación de informes"])

def open_admin_management():
    create_module_window("Módulo de Administración", 
                         ["Gestión de usuarios", 
                          "Administración de inventarios", 
                          "Generación de reportes"], 
                         open_user_management_callback=open_user_management)

def open_packing_management():
    create_module_window("Módulo de Empaque", 
                         ["Empaque de productos", 
                          "Revisión de productos empacados", 
                          "Actualización de inventario"])

def open_transport_management():
    create_module_window("Módulo de Transporte", 
                         ["Gestión de rutas", 
                          "Monitoreo de entregas", 
                          "Registro de transportes"])

def open_reception_management():
    create_module_window("Módulo de Recepción", 
                         ["Recepción de productos", 
                          "Clasificación inicial", 
                          "Registro de recibos"])

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
        else:
            button = tk.Button(module_window, text=option, padx=20, pady=10)
        button.pack(pady=10)

    close_button = tk.Button(module_window, text="Cerrar", command=module_window.destroy, padx=20, pady=10)
    close_button.pack(pady=20)

# Función para abrir la ventana de gestión de usuarios
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

# Selección del rol y acceso al módulo correspondiente
def on_role_selected(role):
    if role == "Gerente":
        open_import_management()
    elif role == "Administrador":
        open_admin_management()
    elif role == "Empacador":
        open_packing_management()
    elif role == "Transportador":
        open_transport_management()
    elif role == "Recepción":
        open_reception_management()
    else:
        messagebox.showinfo("Acceso Restringido", f"El rol '{role}' no tiene acceso a ningún módulo.")

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
