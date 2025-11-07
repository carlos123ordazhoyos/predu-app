from fastapi_mail import FastMail, MessageSchema
from fastapi import BackgroundTasks
from correos.email_config import conf
from correos.enviar_actualizacion_perfil.email_template import generar_html_actualizacion_perfil


async def enviar_email_actualizacion_perfil(data, background_tasks: BackgroundTasks):
    """
    Envía un correo al estudiante notificando los cambios realizados en su perfil.
    """
    cuerpo_html = generar_html_actualizacion_perfil(
        nombre_estudiante=data.nombre_estudiante,
        cambios_realizados=data.cambios_realizados
    )

    mensaje = MessageSchema(
        subject=f"🔄 Se actualizaron los datos de tu perfil — PREDU",
        recipients=[data.email],
        body=cuerpo_html,
        subtype="html"
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, mensaje)
    return {"status": f"Correo de actualización de perfil enviado correctamente a {data.email}"}
