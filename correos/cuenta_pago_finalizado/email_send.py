from fastapi_mail import FastMail, MessageSchema
from fastapi import BackgroundTasks
from correos.email_config import conf
from correos.cuenta_pago_finalizado.email_template import generar_html_pago_finalizado


async def enviar_email_pago_finalizado(data, background_tasks: BackgroundTasks):
    """
    Envía un correo notificando al estudiante que su suscripción o pago de cuenta ha finalizado.
    """
    cuerpo_html = generar_html_pago_finalizado(
        nombre_estudiante=data.nombre_estudiante,
        tipo_cuenta=data.tipo_cuenta,
        fecha_fin=data.fecha_fin,
        logo_url=data.logo_url
    )

    mensaje = MessageSchema(
        subject=f"⚠️ Fin de tu suscripción — {data.tipo_cuenta}",
        recipients=[data.email],
        body=cuerpo_html,
        subtype="html"
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, mensaje)
    return {"status": f"Correo de fin de suscripción enviado correctamente a {data.email}"}
