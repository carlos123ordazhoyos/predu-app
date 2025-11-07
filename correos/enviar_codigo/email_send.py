from fastapi_mail import FastMail, MessageSchema
from correos.email_config import conf
from correos.enviar_codigo.email_template import generar_html_codigo_acceso


async def enviar_email_codigo(data, background_tasks):
    """
    Envía el correo con el código de acceso al estudiante utilizando el template formal oscuro.
    """

    # Generar el HTML del correo
    cuerpo_html = generar_html_codigo_acceso(
        nombre_estudiante=data.nombre_estudiante,
        unique_code=data.unique_code,
        institucion=data.institucion,
        region=data.region,
        director_name=data.director_name,
        teaching_modality=data.teaching_modality
    )

    # Crear el mensaje de correo
    mensaje = MessageSchema(
        subject=f"🔑 Código de Acceso — {data.nombre_estudiante}",
        recipients=[data.email],
        body=cuerpo_html,
        subtype="html"
    )

    # Configurar y enviar el correo en segundo plano
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, mensaje)

    return {
        "status": "success",
        "message": f"Código de acceso enviado correctamente a {data.email}"
    }
