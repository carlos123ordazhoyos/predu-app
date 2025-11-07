from fastapi_mail import FastMail, MessageSchema
from correos.email_config import conf
from correos.enviar_resultados.email_template import generar_html_resultado


async def enviar_email_resultado(data, background_tasks):
    """
    Envía el correo con el resultado integral vocacional,
    combinando los análisis psicológico y académico.
    """

    # Generar el contenido HTML con el template base
    cuerpo_html = generar_html_resultado(
        facultad_academica=data.facultad_academica,
        facultad_psicologica=data.facultad_psicologica
    )

    # Crear el mensaje de correo
    mensaje = MessageSchema(
        subject=f"🎓 Reporte Integral Vocacional — {data.nombre_estudiante}",
        recipients=[data.email],
        body=cuerpo_html,
        subtype="html"
    )

    # Enviar de forma asíncrona
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, mensaje)

    return {
        "status": "success",
        "message": f"Reporte integral vocacional enviado correctamente a {data.email}"
    }
