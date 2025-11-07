from fastapi_mail import FastMail, MessageSchema
from fastapi import BackgroundTasks
from correos.email_config import conf
from correos.enviar_validacion_tutor.email_template import generar_html_validacion_tutor


async def enviar_email_validacion_tutor(data, background_tasks: BackgroundTasks):
    """
    Envía un correo al estudiante notificando la validación de sus reportes
    por parte de su tutor y el consejo brindado.
    """
    cuerpo_html = generar_html_validacion_tutor(
        nombre_estudiante=data.nombre_estudiante,
        nombre_tutor=data.nombre_tutor,
        consejo_tutor=data.consejo_tutor
    )

    mensaje = MessageSchema(
        subject=f"✅ {data.nombre_tutor} ha validado tus reportes en PREDU",
        recipients=[data.email],
        body=cuerpo_html,
        subtype="html"
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, mensaje)
    return {"status": f"Correo de validación enviado correctamente a {data.email}"}
