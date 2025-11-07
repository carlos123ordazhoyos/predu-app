from fastapi_mail import FastMail, MessageSchema
from fastapi import BackgroundTasks
from correos.email_config import conf
from correos.enviar_subida_plan.email_template import generar_html_subida_plan


async def enviar_email_subida_plan(data, background_tasks: BackgroundTasks):
    """
    Envía un correo notificando la subida de plan del usuario.
    """
    cuerpo_html = generar_html_subida_plan(
        nombre_estudiante=data.nombre_estudiante,
        nuevo_plan=data.nuevo_plan
    )

    mensaje = MessageSchema(
        subject=f"🚀 ¡Tu plan PREDU ahora es {data.nuevo_plan}!",
        recipients=[data.email],
        body=cuerpo_html,
        subtype="html"
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, mensaje)
    return {"status": f"Correo de confirmación de plan enviado correctamente a {data.email}"}
