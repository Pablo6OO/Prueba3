import Funciones as fn
IDs=['NickNames: ']
Nombres=['Nombres: ']
Puntajes=[
    ['Valorant: '],
    ['Fortnite: '],
    ['Fifa: ']
]
categorias=[
    ['Principiante: '],
    ['Avanzado: '],
    ['Experto: ']
]
Flag=True
hola='Juan'
while Flag:
    try:
        opc,Flag=fn.menu()
    except:
        print('Escribir un Número')
    if opc==1:
        IDs,Nombres,Puntajes,categorias=fn.puntaje(IDs,Nombres,Puntajes,categorias)
    elif opc==2:
        print(IDs)
        print(Nombres)
        for fila in Puntajes:
            print(fila)
        for fila in categorias:
            print(fila)
    elif opc==3:
        fn.opcion3(IDs,Nombres,Puntajes,categorias)