import threading, json, socket
servidor_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

def enviar(opcion,mensaje):
    mensajeE={str(opcion):mensaje}
    mensajeE=json.dumps(mensajeE)
    servidor_socket.sendto(mensajeE.encode(),('localhost',5000))

    data,direccion=servidor_socket.recvfrom(1024)

    mensajeRecibido=data.decode()
    print("---------------RESULTADO RECIBIDO------------------")
    mensajeDecodificado=json.loads(mensajeRecibido)
    print('Direccion servidor:',direccion)
    tipoPeticion = int(list(mensajeDecodificado.keys())[0])

    if(tipoPeticion==1):
        usuario=mensajeDecodificado['1']
        print(usuario['mensaje'])

    if(tipoPeticion==2):        
        usuario=mensajeDecodificado['2']
        print(usuario['mensaje'])


    if(tipoPeticion==3):
        usuario=mensajeDecodificado['3']
        print(usuario['mensaje'])

    if(tipoPeticion==4):
        usuario=mensajeDecodificado['4']
        print(usuario['mensaje'])

def menu():
    opcion=int(input(f'''------------------------ Sistema de trunos ------------------------
    1. Solicitar Turno
    2. Consultar último Turno
    3. Atender Siguiente Turno
    4. Consultar Turnos Pendientes
    5. Salir
    
    Selecciones una opcion: '''))
    return opcion

while True:
    opcion=menu()
    match opcion:
        case 1:
            usuario=input('ingrese el nombre: ')
            usuario.capitalize()
            if usuario.__len__()==0 or usuario=='':
                print('EL NOMBRE ES OBLIGATORIO')
                continue
            enviar(opcion,{'nombre':usuario.capitalize()})
            continue

        case 2:
            enviar(opcion,{'mensaje':'caso 2'})
            continue

        case 3:
            enviar(opcion,{'mensaje':'caso 3'})
            continue

        case 4:
            enviar(opcion,{'mensaje':'caso 4'})    
            continue

        case 5:
            print('salir')
            break
        
        case _:
            print('OPERACIÓN INVALIDA')
            continue