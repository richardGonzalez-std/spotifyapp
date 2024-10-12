import tkinter as tk
root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

'''root.title("Tutorial")

root.geometry(f'{width}x{height}')

#Widgets

label = tk.Label(root,text="Hola Mundo!", font=("Arial",19))

button = tk.Button(root,text="Presionar")

entry = tk.Entry(root)


#Colocar widgets

label.pack(pady=10)
button.pack(pady=10)
entry.pack(pady=10)'''

#root.title("Usando Grid")
root.geometry(f"300x300")

#grid
'''tk.Label(root,text="Usuario: ").grid(row=0, column=0)
tk.Entry(root).grid(row=0, column=1)

tk.Label(root, text="Contraseña: ").grid(row=1,column=0)
tk.Entry(root).grid(row=1,column=1)

tk.Label(root, text="Correo Electrónico: ").grid(row=2,column=0)
tk.Entry(root).grid(row=2,column=1)

tk.Canvas(root,background="#fff",cursor="yes").grid(row=4,column=1)

tk.Button(root, text="Login").grid(rowspan=3, columnspan=3)
'''
'''root.title("Comandos")
def Saludo():
    tk.Label(root,text="Hola Amigo",fg="#3f001a").pack(pady=20)

button = tk.Button(root,text="Saludar",command=Saludo)
button.pack(pady=20)'''

'''root.title("App Bonita")
root.configure(bg="#3498db")


label = tk.Label(root, text="¡Bienvenido!", font=('Helvetica',24),bg="#3498db", fg="white")
label.pack(pady=20)

button = tk.Button(root, text="Continuar", bg="white", fg="#3498db", font=('Helvetica',16))

button.pack(pady=20)'''

'''root.title("Diseño responsivo")
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

label = tk.Label(root, text="Texto que se expande",bg="lightgray")
button = tk.Button(root, text="Boton que se expande",bg="#9a1eda")

label.grid(sticky="nsew")
button.grid(sticky="nsew")'''
def convertir():
    valor = float(entry.get())
    if  opcion_seleccionada.get() == "Metros a Pies":
        pies = valor * 3.28084
        resultado_label.config(text=f'{pies:.2f} pies')
    elif opcion_seleccionada.get() == "Pies a Metros":
        metros = valor / 3.28084
        resultado_label.config(text=f"{metros:.2f} metros")


root.title("Convertirdor de Metros a Pies y Pies a Metros")
opciones = ["Metros a Pies","Pies a Metros"]
opcion_seleccionada = tk.StringVar()
opcion_seleccionada.set(opciones[0])

option_menu = tk.OptionMenu(root, opcion_seleccionada,*opciones)
option_menu.configure()
option_menu.pack(pady=20)
tk.Label(root, text=f"Introduce el valor: ").pack(pady=20)

entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Convertir", command=convertir).pack(pady=10)

resultado_label = tk.Label(root, text="")
resultado_label.pack(pady=5)
root.mainloop()