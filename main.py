import quickstart
from FuncionesCorreo import Correo

service = quickstart.main()

sender='juan.galvez.qwe@gmail.com'
to='juan.galvez@telectronic.com'
subject = 'mensajeprueba'
message_text ='mensaje numero 1 de python'

correo = Correo(service)
mensajeB64 = correo.Create_Message(sender, to, subject, message_text)

respuesta = correo.Create_Draft('me',mensajeB64)
