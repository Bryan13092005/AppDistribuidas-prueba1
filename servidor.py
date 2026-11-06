import threading, json, socket
servidor_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
servidor_socket.bind(("0.0.0.0",5000))
print('esperando conexiones')

turnos=[]

def enviarRespuesta(mensaje,codigo,addr):
    enviarDatos={codigo:mensaje}
    enviarDatos=json.dumps(enviarDatos)
    servidor_socket.sendto(enviarDatos.encode(),addr)

def caso1(data):
    if(data['nombre']=='' or data['nombre'].__len__()==0):
        print({'mensaje':f'''El nombre es obligatorio para asignar turnos'''})
    contador=0
    for turno in turnos:
        contador+=1
    turnoAsignado=contador+1
    turnos.append({'nombre':data['nombre'],
                   'turno':turnoAsignado,
                   'estado':0})

    print({'mensaje':f'''Su turno es: {turnoAsignado}'''})
    return {'mensaje':f'''Su turno es: {turnoAsignado}'''}

def caso2():
    indice=(turnos.__len__())-1

    if(indice==-1):
        return {'mensaje':'No hay Usuarios Registrados'}
    
    ultimoTurno=turnos[indice]
    print(turnos)
    return {'mensaje':f'''El último turno asignado fue {ultimoTurno['turno']}, para {ultimoTurno['nombre']}'''}

def caso3():
    encontrado=False
    indice=0

    for turno in turnos:
        if turno['estado']==0:
            encontrado=True
            print(turnos.index(turno))
            indice=turnos.index(turno)
            break
        

    if(encontrado):
        usuario=turnos[indice]
        usuario['estado']=1
        return {'mensaje':f'''El turno Atendido fue #{usuario['turno']}, del paciente {usuario['nombre']}'''}

    return {'mensaje':'No hay pacientes para atender'}


def caso4():
    contador=0

    for turno in turnos:
        if turno['estado']==0:
            contador+=1

    return {'mensaje':f'''El número de turnos por atender es: {contador}'''}

def tarea(data,direccion):
    mensaje=data
    print("---------------PETICION RECIBIDA------------------")
    mensajeDecodificado=json.loads(mensaje)
    print(mensajeDecodificado)
    print('Direccion cliente:',direccion)
    tipoPeticion = int(list(mensajeDecodificado.keys())[0])
    if(tipoPeticion==1):
        mensaje=caso1(mensajeDecodificado['1'])
        enviarRespuesta(mensaje,1,direccion)

    if(tipoPeticion==2):
        mensaje=caso2()
        enviarRespuesta(mensaje,2,direccion)

    if(tipoPeticion==3):
        mensaje=caso3()
        enviarRespuesta(mensaje,3,direccion)

    if(tipoPeticion==4):
        mensaje=caso4()
        enviarRespuesta(mensaje,4,direccion)

while True:
    data,addr=servidor_socket.recvfrom(1024)
    datos=data.decode()
    hilo=threading.Thread(target=tarea,args=(datos,addr))
    hilo.start()

