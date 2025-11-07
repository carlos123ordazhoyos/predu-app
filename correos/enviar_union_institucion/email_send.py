from fastapi_mail import FastMail, MessageSchema
from fastapi import BackgroundTasks
from correos.email_config import conf
from correos.enviar_union_institucion.email_template import generar_html_union_institucion


async def enviar_email_union_institucion(data, background_tasks: BackgroundTasks):
    """
    Envía un correo de bienvenida al estudiante al unirse a una institución educativa.
    """
    cuerpo_html = generar_html_union_institucion(
        nombre_estudiante=data.nombre_estudiante,
        nombre_institucion=data.nombre_institucion,
        lugar=data.lugar,
        nombre_encargado=data.nombre_encargado,
        logo_url=data.logo_url,
        mensaje_motivador=data.mensaje_motivador
    )

    mensaje = MessageSchema(
        subject=f"🎉 ¡Te uniste a {data.nombre_institucion}! — PREDU",
        recipients=[data.email],
        body=cuerpo_html,
        subtype="html"
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, mensaje)
    return {"status": f"Correo de bienvenida enviado correctamente a {data.email}"}
