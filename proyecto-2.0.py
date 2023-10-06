from tkinter import *
import random
#Crea una ventana principal 
root = Tk()
#Elegimos la medida del cuadrado
root.geometry("500x300")
#Le ponemos un titulo 
root.title("Piedra Papel o Tijera")
 
#Le asigna un valor a cada numero
computer_value = {
    "0":"Piedra",
    "1":"Papel",
    "2":"Tijera"
}
 
#Esta funcion llamada "reiniciar juego" con 3 atributos,que serian los botones,le indicamos que su estado este activado y tambien le configuramos el texto
def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text = "Jugador              ")
    l3.config(text = "Maquina")
    l4.config(text = "")
 
#Esta funcion llamada "boton desactivado" con 3 botones,le indicamos que su estado este desactivado
def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"
 
#Creamos una funcion llamada "Piedra",con un atributo "computadora valor" en la que usamos STR(una cadena) donde te devuelve el resultado,RANDOM.RANDINT le pedimos que el resultado sea aleatorio y devuelva un numero entero incluido entre los valores indicados
#despues condiciones "if","elif","else" en la que el jugador elige "Piedra",el resultado daria "empate",y si elige "Tijera" el jugador "gana",o si no la "maquina gana"
#por ultimo le configuramos el texto y ejecutamos la funcion "boton desactivado"    
def isrock():
    c_v = computer_value[str(random.randint(0,2))]
    if c_v == "Piedra":
        match_result = "Empate"
    elif c_v=="Tijera":
        match_result = "Jugador gana"
    else:
        match_result = "Maquina gana"
    l4.config(text = match_result)
    l1.config(text = "Piedra            ")
    l3.config(text = c_v)
    button_disable()


def ispaper():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Papel":
        match_result = "Empate"
    elif c_v=="Tijera":
        match_result = "Maquina gana"
    else:
        match_result = "Jugador Gana"
    l4.config(text = match_result)
    l1.config(text = "Papel           ")
    l3.config(text = c_v)
    button_disable()
 

def isscissor():
    c_v = computer_value[str(random.randint(0,2))]
    if c_v == "Piedra":
        match_result = "Maquina gana"
    elif c_v == "Tijera":
        match_result = "Empate"
    else:
        match_result = "Jugador gana"
    l4.config(text = match_result)
    l1.config(text = "Tijera         ")
    l3.config(text = c_v)
    button_disable()
 
#Usamos la etiqueta de texto Label,le modificamos el tipo de fuente,color y posicionamiento que incluye a todos los elementos,y la altura
Label(root,
      text = "Piedra Papel Tijera",
      font = "normal 30 bold",
      fg = "gray").pack(pady = 50)
#Creamos un objecto frame,con la raiz root 
frame = Frame(root)
#PACK Lo que hace es organizar y ajustar automaticamnte  el tamaño de frame y su contenido de acuerdo con el contenido que contiene
frame.pack()
#Modificamos lo vendria siendo el texto,el espacio y el tamaño de la fuente
l1 = Label(frame,
           text = "     Jugador     ",
           font ="normal 30 bold")
 
l2 = Label(frame,
           text = "      VS         ",
           font = "normal 20 bold")
 
l3 = Label(frame,
           text = "     Maquina     ",
           font = "normal 30 bold")
#Al objeto le indicamos que se coloque  en el lado izquierdo del contenedor
l1.pack(side = LEFT)
l2.pack(side = LEFT)
l3.pack()
#Modificamos 
l4 = Label(root,
           text = "",
           font = "normal 40 bold",
           bg = "white",
           width = 15 ,
           borderwidth = 2,
           relief = "solid")
l4.pack(pady = 20)
 
frame1 = Frame(root)
frame1.pack()
 
b1 = Button(frame1, text = "Piedra",
            font = 10, width = 7,
            command = isrock)
 
b2 = Button(frame1, text = "Papel ",
            font = 10, width = 7,
            command = ispaper)
 
b3 = Button(frame1, text = "Tijera",
            font = 10, width = 7,
            command = isscissor)
 
b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT,padx = 10)
b3.pack(padx = 10)
 
Button(root, text = "Reiniciar Juego",
       font = 10, fg = "sky blue",
       bg = "black", command = reset_game).pack(pady = 20)
 

root.mainloop()