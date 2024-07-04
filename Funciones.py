def menu():
    print('''===============
    eSports
===============
1. Registrar puntajes torneo
2. Listar los todos puntajes
3. Imprimir por Tipo
4. Salir del Programa''')
    opc=int(input('Ingrese N° Correspondiente -> '))
    if opc>4 or opc<1:
        print('Opción no valida')
        return opc,True
    elif opc==4:
        print('Saliendo...')
        return opc,False
    else:
        return opc,True

def puntaje(IDs,Nombres,Puntajes,categorias):
    Flag=Flag1=Flag2=True
    val=fort=fifa=False
    while Flag1:
        Nick=input('Escriba su ID de jugador -> ')
        Nombre=input('Escriba su nombre y apellido -> ')
        print('Esta segur@ de que son los nombres correctos? s/n')
        s=input('->').lower()
        if s=='s':
            Flag1=False
        elif s=='n':
            Flag1=True
    while Flag:
        try:
            Flag0=True
            print('''En qué juegos participa?
1. VALORANT
2. FORTNITE
3. FIFA''')
            opc=int(input('Ingrese el juego -> '))
            if opc==1:
                val=True
            elif opc==2:
                fort=True
            elif opc==3:
                fifa=True
            else:
                print('Opción no valida')
            if fifa or val or fort:
                while Flag0:
                    print('Quiere agregar otro juego? s/n')
                    sas=input('-> ').lower()
                    if sas=='s':
                        Flag=True
                        Flag0=False
                    elif sas=='n':
                        Flag=Flag0=False
        except:
            print('Igrese N°!!')
    while Flag2:
        if val:
            puntval=int(input('Ingrese puntuación de Valorant -> '))
        else:
            puntval=0
        if fort:
            puntfort=int(input('Ingrese puntuación de Fortnite -> '))
        else:
            puntfort=0
        if fifa:
            puntfifa=int(input('Ingrese puntuación de Fifa -> '))
        else:
            puntfifa=0
        d=input('Esta segur@ de su puntaje? s/n -> ').lower()
        if d=='s':
            Flag2=False
        elif d=='n':
            Flag2=True
    Nombres.append(Nombre)
    IDs.append(Nick)
    for fila in range (0,len(Puntajes)):
        if fila==0:
            if val:
                Puntajes[fila].append(puntval)
            else:
                Puntajes[fila].append(0)
        elif fila==1:
            if fort:
                Puntajes[fila].append(puntfort)
            else:
                Puntajes[fila].append(0)
        elif fila==2:
            if fifa:
                Puntajes[fila].append(puntfifa)
            else:
                Puntajes[fila].append(0)
    FlagFinal=True
    while FlagFinal:
        try:
            print('''¿De qué tipo te identificas?
1. Principiante
2. Avanzado
3. Experto''')
            opcion=int(input('-> '))
            if opcion>3 or opcion<1:
                print('Ingresar un número valido')
            else:
                FlagFinal=False
        except:
            print('Se espera un número como respuesta')
    for fila in range (0,len(categorias)):
        if fila==0:
            if opcion==1:
                categorias[fila].append(Nick)
        elif fila==1:
            if opcion==2:
                categorias[fila].append(Nick)
        elif fila==2:
            if opcion==3:
                categorias[fila].append(Nick)
    return IDs,Nombres,Puntajes,categorias

def opcion3(IDs,Nombres,Puntajes,categorias):
    print('''¿Qué categoría quiere guardar?
1. Principiante
2. Avanzado
3. Experto''')
    opci=int(input('-> '))
    with open ('Archivo.txt','w') as file:
        if opci==1:
            for nom in range (1,len(categorias)+1):
                for buscar in IDs:
                    if buscar==categorias[nom]:
                        encontrado=buscar
                        break
                file.write(IDs[encontrado])
                file.write(Nombres[encontrado])
                file.write(Puntajes[encontrado])