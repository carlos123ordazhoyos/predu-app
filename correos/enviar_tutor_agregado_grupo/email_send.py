from fastapi_mail import FastMail, MessageSchema
from fastapi import BackgroundTasks
from correos.email_config import conf
from correos.enviar_tutor_agregado_grupo.email_template import generar_html_tutor_agregado_grupo


async def enviar_email_tutor_agregado_grupo(data, background_tasks: BackgroundTasks):
    """
    Envía un correo notificando que se ha agregado un tutor a un grupo educativo.
    """
    cuerpo_html = generar_html_tutor_agregado_grupo(
        nombre_grupo=data.nombre_grupo,
        nombre_tutor=data.nombre_tutor,
        tipo_tutor=data.tipo_tutor,
        correo=data.correo,
        telefono=data.telefono,
        logo_url=data.logo_url
    )

    mensaje = MessageSchema(
        subject=f"👩‍🏫 Tutor asignado al grupo {data.nombre_grupo}",
        recipients=[data.email_destino],
        body=cuerpo_html,
        subtype="html"
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, mensaje)
    return {"status": f"Correo enviado correctamente a {data.email_destino}"}
