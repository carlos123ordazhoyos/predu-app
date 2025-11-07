from fastapi_mail import FastMail, MessageSchema
from fastapi import BackgroundTasks
from correos.email_config import conf
from correos.enviar_estudiante_agregado_tutor.email_template import generar_html_estudiante_agregado_tutor


async def enviar_email_estudiante_agregado_tutor(data, background_tasks: BackgroundTasks):
    """
    Envía un correo al tutor notificando que se ha agregado un estudiante a su grupo de estudio.
    """
    cuerpo_html = generar_html_estudiante_agregado_tutor(
        nombre_tutor=data.nombre_tutor,
        nombre_estudiante=data.nombre_estudiante,
        grado=data.grado,
        correo=data.correo,
        telefono=data.telefono,
        logo_url=data.logo_url
    )

    mensaje = MessageSchema(
        subject=f"👨‍🏫 Nuevo estudiante asignado a tu grupo — {data.nombre_estudiante}",
        recipients=[data.email_tutor],
        body=cuerpo_html,
        subtype="html"
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, mensaje)
    return {"status": f"Correo enviado correctamente a {data.email_tutor}"}
