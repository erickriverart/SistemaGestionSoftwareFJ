import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva

clientes = []
reservas = []


# Registrar cliente
def registrar_cliente():

    try:

        nombre = entry_nombre.get()
        correo = entry_correo.get()
        telefono = entry_telefono.get()

        cliente = Cliente(nombre, correo, telefono)

        clientes.append(cliente)

        lista_clientes.insert(tk.END, cliente.obtener_nombre())

        combo_clientes["values"] = [c.obtener_nombre() for c in clientes]

        messagebox.showinfo("Registro exitoso", "Cliente registrado correctamente.")

        limpiar_cliente()

    except Exception as error:

        messagebox.showerror("Error", str(error))


# Crear reserva
def crear_reserva():

    try:

        nombre_cliente = combo_clientes.get()

        if nombre_cliente == "":

            raise ValueError("Debes seleccionar un cliente.")

        cliente = None

        for c in clientes:

            if c.obtener_nombre() == nombre_cliente:
                cliente = c

        tipo_servicio = variable_servicio.get()

        costo = float(entry_costo.get())

        cantidad = int(entry_cantidad.get())

        fecha = entry_fecha.get()

        if not fecha.strip():

            raise ValueError("Debes ingresar una fecha.")

        # Crear servicio
        if tipo_servicio == "Reserva Sala":

            servicio = ReservaSala("Reserva Sala", costo, cantidad)

        elif tipo_servicio == "Alquiler Equipo":

            servicio = AlquilerEquipo("Alquiler Equipo", costo, cantidad)

        else:

            servicio = AsesoriaEspecializada("Asesoría", costo, "Avanzado")

        reserva = Reserva(cliente, servicio, cantidad, fecha)

        reserva.confirmar_reserva()

        reservas.append(reserva)

        actualizar_reservas()

        messagebox.showinfo("Reserva creada", "Reserva registrada correctamente.")

        limpiar_reserva()

    except Exception as error:

        messagebox.showerror("Error", str(error))


# Mostrar reservas
def actualizar_reservas():

    lista_reservas.delete(0, tk.END)

    for reserva in reservas:

        texto = (
            f"{reserva._cliente.obtener_nombre()} | "
            f"{reserva._servicio._nombre} | "
            f"{reserva._fecha} | "
            f"${reserva._servicio.calcular_costo():,.0f} | "
            f"{reserva.obtener_estado()}"
        )

        lista_reservas.insert(tk.END, texto)


# Cancelar reserva
def cancelar_reserva():

    try:

        seleccion = lista_reservas.curselection()

        if not seleccion:

            raise ValueError("Selecciona una reserva.")

        reserva = reservas[seleccion[0]]

        reserva.cancelar_reserva()

        actualizar_reservas()

        messagebox.showinfo("Reserva cancelada", "La reserva fue cancelada.")

    except Exception as error:

        messagebox.showerror("Error", str(error))


# Limpiar cliente
def limpiar_cliente():

    entry_nombre.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)


# Limpiar reserva
def limpiar_reserva():

    entry_costo.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    entry_fecha.delete(0, tk.END)


# =====================================
# Ventana principal
# =====================================

ventana = tk.Tk()

ventana.title("Sistema Integral Software FJ")

ventana.geometry("850x650")


# =====================================
# Título principal
# =====================================

titulo = tk.Label(
    ventana, text="Sistema Integral de Clientes y Reservas", font=("Arial", 18, "bold")
)

titulo.pack(pady=10)


mensaje = tk.Label(
    ventana,
    text="Primero registra un cliente para poder crear una reserva.",
    fg="goldenrod",
)

mensaje.pack()


# =====================================
# Sistema de pestañas
# =====================================

notebook = ttk.Notebook(ventana)

notebook.pack(expand=True, fill="both", padx=10, pady=10)


# =====================================
# Pestaña clientes
# =====================================

tab_clientes = tk.Frame(notebook)

notebook.add(tab_clientes, text="Clientes")


frame_cliente = tk.LabelFrame(
    tab_clientes, text="Registro de clientes", padx=10, pady=10
)

frame_cliente.pack(padx=10, pady=10, fill="x")


tk.Label(frame_cliente, text="Nombre").pack()

entry_nombre = tk.Entry(frame_cliente, width=40)

entry_nombre.pack()


tk.Label(frame_cliente, text="Correo").pack()

entry_correo = tk.Entry(frame_cliente, width=40)

entry_correo.pack()


tk.Label(frame_cliente, text="Teléfono").pack()

entry_telefono = tk.Entry(frame_cliente, width=40)

entry_telefono.pack()


boton_cliente = tk.Button(
    frame_cliente, text="Registrar cliente", command=registrar_cliente
)

boton_cliente.pack(pady=10)


frame_lista_clientes = tk.LabelFrame(
    tab_clientes, text="Clientes registrados", padx=10, pady=10
)

frame_lista_clientes.pack(padx=10, pady=10, fill="both", expand=True)


lista_clientes = tk.Listbox(frame_lista_clientes, height=10)

lista_clientes.pack(fill="both", expand=True)


# =====================================
# Pestaña reservas
# =====================================

tab_reservas = tk.Frame(notebook)

notebook.add(tab_reservas, text="Reservas")


frame_reserva = tk.LabelFrame(tab_reservas, text="Crear reserva", padx=10, pady=10)

frame_reserva.pack(padx=10, pady=10, fill="x")


tk.Label(frame_reserva, text="Seleccionar cliente").pack()

combo_clientes = ttk.Combobox(frame_reserva, state="readonly")

combo_clientes.pack()


tk.Label(frame_reserva, text="Tipo de servicio").pack()

variable_servicio = tk.StringVar()

variable_servicio.set("Reserva Sala")


menu_servicio = tk.OptionMenu(
    frame_reserva, variable_servicio, "Reserva Sala", "Alquiler Equipo", "Asesoría"
)

menu_servicio.pack()


tk.Label(frame_reserva, text="Costo base").pack()

entry_costo = tk.Entry(frame_reserva, width=40)

entry_costo.pack()


tk.Label(frame_reserva, text="Cantidad (horas/días)").pack()

entry_cantidad = tk.Entry(frame_reserva, width=40)

entry_cantidad.pack()


tk.Label(frame_reserva, text="Fecha de reserva").pack()

tk.Label(frame_reserva, text="Formato: DD/MM/AAAA", fg="gray").pack()

entry_fecha = tk.Entry(frame_reserva, width=40)

entry_fecha.pack()


boton_reserva = tk.Button(frame_reserva, text="Crear reserva", command=crear_reserva)

boton_reserva.pack(pady=10)


# =====================================
# Pestaña historial
# =====================================

tab_historial = tk.Frame(notebook)

notebook.add(tab_historial, text="Historial")


frame_historial = tk.LabelFrame(
    tab_historial, text="Reservas realizadas", padx=10, pady=10
)

frame_historial.pack(padx=10, pady=10, fill="both", expand=True)


lista_reservas = tk.Listbox(frame_historial, height=15)

lista_reservas.pack(fill="both", expand=True)


boton_cancelar = tk.Button(
    tab_historial, text="Cancelar reserva seleccionada", command=cancelar_reserva
)

boton_cancelar.pack(pady=10)


# Ejecutar ventana
ventana.mainloop()
