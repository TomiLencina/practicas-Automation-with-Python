import smtplib
import ssl
from email.message import EmailMessage
import imghdr

# Define email del que envia.contraseña y del que recibe
email_sender = 'mail@gmail.com'
email_password ='12contrasena2'
email_receiver = 'mail-receptor@gmail.com'

# Asunto-cuerpo del mail
asunto = 'Aunsto del correo'
cuerpo_correo = """
        ESTE ES EL CUERPO DEL CORREO
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = asunto
em.set_content(cuerpo_correo)

#adjuntar archivo
with open('foto.jpg', 'rb') as file:
    file_data = file.read()
    file_tipo = imghdr.what(file.name)
    file_nombre = file.name
em.add_attachment(file_data, filename=file_nombre, subtype=file_tipo, maintype='image')



# SSL PARA LA  SEGURIDAD
context = ssl.create_default_context()

# Logeo y enviado del mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())