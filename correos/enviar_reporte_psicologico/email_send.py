from fastapi_mail import FastMail, MessageSchema
from correos.email_config import conf
from correos.enviar_reporte_psicologico.email_template import generar_html_reporte_psicologico


async def enviar_email_reporte_psicologico(data, background_tasks):
    """
    Envía el correo con el reporte psicológico generado por el test RIASEC.
    """

    # Generar contenido HTML personalizado
    cuerpo_html = generar_html_reporte_psicologico(
        nombre_estudiante=data.nombre_estudiante,
        facultad=data.facultad_psicologica,
        consejo_psicologico=data.consejo_psicologico
    )

    # Crear mensaje de correo
    mensaje = MessageSchema(
        subject=f"🧠 Reporte Psicológico — {data.nombre_estudiante}",
        recipients=[data.email],
        body=cuerpo_html,
        subtype="html"
    )

    # Envío del mensaje de forma asíncrona
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, mensaje)

    return {
        "status": "success",
        "message": f"Reporte psicológico enviado correctamente a {data.email}"
    }
