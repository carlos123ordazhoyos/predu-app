from fastapi_mail import FastMail, MessageSchema
from correos.email_config import conf
from correos.enviar_reporte_academico.email_template import generar_html_reporte_academico


async def enviar_email_reporte_academico(data, background_tasks):
    """
    Envía el correo con el reporte académico generado por el modelo GraphSAGE.
    """

    # Generar contenido HTML
    cuerpo_html = generar_html_reporte_academico(
        nombre_estudiante=data.nombre_estudiante,
        carrera=data.facultad_academica,
        recomendacion_academica=data.recomendacion_academica
    )

    # Crear mensaje
    mensaje = MessageSchema(
        subject=f"📘 Reporte Académico — {data.nombre_estudiante}",
        recipients=[data.email],
        body=cuerpo_html,
        subtype="html"
    )

    # Envío asíncrono
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, mensaje)

    return {
        "status": "success",
        "message": f"Reporte académico enviado correctamente a {data.email}"
    }
