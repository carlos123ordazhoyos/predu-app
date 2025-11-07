from fastapi_mail import FastMail, MessageSchema
from fastapi import BackgroundTasks
from correos.email_config import conf
from correos.enviar_bienvenida.email_template import generar_html_bienvenida


async def enviar_email_bienvenida(data, background_tasks: BackgroundTasks):
    """
    Envía un correo de bienvenida al nuevo usuario.
    """

    cuerpo_html = generar_html_bienvenida(nombre_estudiante=data.nombre_estudiante)

    mensaje = MessageSchema(
        subject=f"🎉 Bienvenido/a a PREDU — {data.nombre_estudiante}",
        recipients=[data.email],
        body=cuerpo_html,
        subtype="html"
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, mensaje)

    return {"status": f"Correo de bienvenida enviado correctamente a {data.email}"}
