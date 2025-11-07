from fastapi_mail import FastMail, MessageSchema
from fastapi import BackgroundTasks
from correos.email_config import conf
from correos.tutor_cuenta_aprobada.email_template import generar_html_tutor_cuenta_aprobada


async def enviar_email_tutor_cuenta_aprobada(data, background_tasks: BackgroundTasks):
    """
    Envía un correo notificando que la cuenta de tutor independiente ha sido aprobada.
    """
    cuerpo_html = generar_html_tutor_cuenta_aprobada(
        nombre_tutor=data.nombre_tutor,
        fecha_aprobacion=data.fecha_aprobacion,
        logo_url=data.logo_url
    )

    mensaje = MessageSchema(
        subject=f"🎓 Cuenta Aprobada — Bienvenido a PREDU, {data.nombre_tutor}",
        recipients=[data.email],
        body=cuerpo_html,
        subtype="html"
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, mensaje)
    return {"status": f"Correo de aprobación enviado correctamente a {data.email}"}
