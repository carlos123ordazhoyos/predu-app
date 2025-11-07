from fastapi_mail import FastMail, MessageSchema
from fastapi import BackgroundTasks
from correos.email_config import conf
from correos.tutor_cuenta_rechazada.email_template import generar_html_tutor_cuenta_rechazada


async def enviar_email_tutor_cuenta_rechazada(data, background_tasks: BackgroundTasks):
    """
    Envía un correo notificando que la cuenta de tutor independiente ha sido rechazada.
    """
    cuerpo_html = generar_html_tutor_cuenta_rechazada(
        nombre_tutor=data.nombre_tutor,
        motivo_rechazo=data.motivo_rechazo,
        fecha_revision=data.fecha_revision,
        logo_url=data.logo_url
    )

    mensaje = MessageSchema(
        subject=f"⚠️ Solicitud No Aprobada — {data.nombre_tutor}",
        recipients=[data.email],
        body=cuerpo_html,
        subtype="html"
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, mensaje)
    return {"status": f"Correo de rechazo enviado correctamente a {data.email}"}
