from fastapi_mail import FastMail, MessageSchema
from fastapi import BackgroundTasks
from correos.email_config import conf
from correos.enviar_retiro_institucion.email_template import generar_html_retiro_institucion


async def enviar_email_retiro_institucion(data, background_tasks: BackgroundTasks):
    """
    Envía un correo notificando el retiro del estudiante de una institución.
    """
    cuerpo_html = generar_html_retiro_institucion(
        nombre_estudiante=data.nombre_estudiante,
        nombre_institucion=data.nombre_institucion,
        lugar=data.lugar,
        nombre_encargado=data.nombre_encargado,
        motivo_retiro=data.motivo_retiro,
        logo_url=data.logo_url
    )

    mensaje = MessageSchema(
        subject=f"📋 Notificación de Retiro — {data.nombre_institucion}",
        recipients=[data.email],
        body=cuerpo_html,
        subtype="html"
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, mensaje)
    return {"status": f"Correo de retiro enviado correctamente a {data.email}"}
