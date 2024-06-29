import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import statistics
from matplotlib.figure import Figure
from tkinter import messagebox
# from tkinter import Combobox



def mostrar_analise():

    pib=[150,300,500,800,150,300,900]

    estados=['SP','RS','BA','PE','ES','MT','MS']
    

    estado_selecionada = estado_pib.get()
    if  estado_selecionada == 'SP':
        dado = pib
    elif estado_selecionada == 'RS':
        dado = pib
    elif estado_selecionada == 'BA':
        dado = pib
    elif estado_selecionada == 'PE':
        dado = pib
    elif estado_selecionada == 'ES':
        dado = pib
    elif estado_selecionada == 'MT':
        dado = pib
    elif estado_selecionada == 'MS':
        dado = pib
    else: 
         messagebox.showwarning('erro - Esse dado não existe')
         return  
    
   
    resultado_text = (f'''
                        estado: {estado_selecionada}
                        pib: {pib}
                       '''    ) 
    
    resultado_label.config(text = resultado_text )



    fig = Figure(figsize=(6,4), dpi = 100)
    ax = fig.add_subplot(111)
    ax.set_title('Estados e pibs')
    ax.set_xlabel('Estado')
    ax.set_ylabel('Pib')
    ax.plot(estados,pib)
    ax.grid(True)

    canvas =  FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()
    

root = tk.Tk()
root.title('Estados e pibs')
estado_pib = tk.StringVar(value='SP')
pibs = ['SP','RS','BA','PE','ES','MT','MS']
menu = ttk.Combobox(root, textvariable =estado_pib, values = pibs )
menu.pack()

btn = tk.Button(root, text='Analise', command=mostrar_analise)
btn.pack(pady=10)

resultado_label = tk.Label(root, text='')
resultado_label.pack(pady=10)



root.mainloop()