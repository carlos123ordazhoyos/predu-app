from fastapi_mail import FastMail, MessageSchema
from fastapi import BackgroundTasks
from correos.email_config import conf
from correos.enviar_bienvenida_tutor.email_template import generar_html_bienvenida_tutor


async def enviar_email_bienvenida_tutor(data, background_tasks: BackgroundTasks):
    """
    Envía un correo de bienvenida al tutor que acaba de crear su cuenta.
    """
    cuerpo_html = generar_html_bienvenida_tutor(
        nombre_tutor=data.nombre_tutor,
        institucion=data.institucion,
        logo_url=data.logo_url,
        enlace_panel=data.enlace_panel
    )

    mensaje = MessageSchema(
        subject=f"👩‍🏫 Bienvenido(a) a PREDU — {data.institucion}",
        recipients=[data.email],
        body=cuerpo_html,
        subtype="html"
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, mensaje)
    return {"status": f"Correo de bienvenida enviado correctamente a {data.email}"}
