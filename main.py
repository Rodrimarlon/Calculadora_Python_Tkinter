from tkinter import *

window = Tk()
window.title('Calculadora')

i = 0

# Entrada
e_texto = Entry(window, font=('Calibri 20'))
e_texto.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Funciones


def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1


def borrar():
    e_texto.delete(0, END)
    i = 0


def operacion():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i = 0


# Botones
boton1 = Button(window, text='1', width='5', height='2',
                command=lambda: click_boton(1))
boton2 = Button(window, text='2', width='5', height='2',
                command=lambda: click_boton(2))
boton3 = Button(window, text='3', width='5', height='2',
                command=lambda: click_boton(3))
boton4 = Button(window, text='4', width='5', height='2',
                command=lambda: click_boton(4))
boton5 = Button(window, text='5', width='5', height='2',
                command=lambda: click_boton(5))
boton6 = Button(window, text='6', width='5', height='2',
                command=lambda: click_boton(6))
boton7 = Button(window, text='7', width='5', height='2',
                command=lambda: click_boton(7))
boton8 = Button(window, text='8', width='5', height='2',
                command=lambda: click_boton(8))
boton9 = Button(window, text='9', width='5', height='2',
                command=lambda: click_boton(9))
boton0 = Button(window, text='0', width='13', height='2',
                command=lambda: click_boton(0))


boton_borrar = Button(window, text='AC', width='5',
                      height='2', command=lambda: borrar())
boton_parentesis1 = Button(window, text='(', width='5', height='2',
                           command=lambda: click_boton('('))
boton_parentesis2 = Button(window, text=')', width='5',
                           height='2', command=lambda: click_boton(')'))
boton_punto = Button(window, text='.', width='5',
                     height='2', command=lambda: click_boton('.'))


boton_sum = Button(window, text='+', width='5', height='2',
                   command=lambda: click_boton('+'))
boton_rest = Button(window, text='-', width='5',
                    height='2', command=lambda: click_boton('-'))
boton_mult = Button(window, text='x', width='5',
                    height='2', command=lambda: click_boton('*'))
boton_div = Button(window, text='/', width='5', height='2',
                   command=lambda: click_boton('/'))
boton_igual = Button(window, text='=', width='5',
                     height='2', command=lambda: operacion())

# Agregar botones en pantalla
boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_parentesis1.grid(row=1, column=1, padx=5, pady=5)
boton_parentesis2.grid(row=1, column=2, padx=5, pady=5)
boton_div.grid(row=1, column=3, padx=5, pady=5)

boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_mult.grid(row=2, column=3, padx=5, pady=5)

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_sum.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_rest.grid(row=4, column=3, padx=5, pady=5)

boton0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
boton_punto.grid(row=5, column=2, padx=5, pady=5)
boton_igual.grid(row=5, column=3, padx=5, pady=5)


window.mainloop()
