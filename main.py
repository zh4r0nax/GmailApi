import quickstart
from FuncionesCorreo import Correo

service = quickstart.main()

sender='juan.galvez.qwe@gmail.com'
to='juan.galvez@telectronic.com'
subject = 'mensaje prueba 2'
message_text ='mensaje numero 1 de python'

correo = Correo(service)
mensajeB64 = correo.Create_Message(sender, to, subject, message_text)

# #para crear un borrador
# respuesta = correo.Create_Draft(mensajeB64)

#TODO: sin soporte buscar alternativas
# respuestaDraft = correo.Get_Draft_All('r7667771443788871170')
#enviar mensaje

respeusta = correo.send_message(mensajeB64)
