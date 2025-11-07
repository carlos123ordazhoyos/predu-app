from fastapi_mail import FastMail, MessageSchema
from fastapi import BackgroundTasks
from correos.email_config import conf
from correos.enviar_validacion_academica_tutor.email_template import generar_html_validacion_academica_tutor


async def enviar_email_validacion_academica_tutor(data, background_tasks: BackgroundTasks):
    """
    Envía un correo al estudiante notificando la validación de su reporte académico
    por parte de su tutor, incluyendo el consejo o retroalimentación.
    """
    cuerpo_html = generar_html_validacion_academica_tutor(
        nombre_estudiante=data.nombre_estudiante,
        nombre_tutor=data.nombre_tutor,
        consejo_tutor=data.consejo_tutor
    )

    mensaje = MessageSchema(
        subject=f"📘 {data.nombre_tutor} validó tu reporte académico en PREDU",
        recipients=[data.email],
        body=cuerpo_html,
        subtype="html"
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, mensaje)
    return {"status": f"Correo de validación académica enviado correctamente a {data.email}"}
