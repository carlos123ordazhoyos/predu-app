from correos.template_base import generar_template_base


def generar_html_estudiante_agregado_tutor(nombre_tutor: str, nombre_estudiante: str, grado: str, correo: str, telefono: str, logo_url: str) -> str:
    """
    Genera el cuerpo HTML para notificar al tutor cuando se agrega un estudiante a su grupo.
    """

    contenido = f"""
    <div style="text-align:center; padding:25px;">
        <img src="{logo_url}" alt="Logo PREDU" style="width:100px; border-radius:12px; margin-bottom:15px;"/>
        <h2 style="color:#06b6d4; font-size:24px;">👨‍🏫 ¡Nuevo estudiante asignado a tu grupo!</h2>

        <p style="color:#e5e7eb; font-size:16px;">
            Hola <strong style="color:#facc15;">{nombre_tutor}</strong>,<br><br>
            Te informamos que se ha agregado un nuevo estudiante a tu grupo de estudio. 
            A continuación, encontrarás los datos del alumno para tu registro:
        </p>

        <div style="background:#1f2937; border-radius:12px; padding:20px; margin-top:20px; border:1px solid #374151; text-align:left;">
            <p style="color:#facc15; font-weight:bold; font-size:17px;">📘 Datos del Estudiante</p>
            <p style="color:#e5e7eb; font-size:15px;"><strong>Nombre:</strong> {nombre_estudiante}</p>
            <p style="color:#e5e7eb; font-size:15px;"><strong>Grado:</strong> {grado}</p>
            <p style="color:#e5e7eb; font-size:15px;"><strong>Correo:</strong> {correo}</p>
            <p style="color:#e5e7eb; font-size:15px;"><strong>Teléfono:</strong> {telefono}</p>
        </div>

        <p style="color:#d1d5db; font-size:16px; margin-top:25px;">
            Te animamos a comunicarte con tu estudiante para fortalecer el vínculo académico y brindar un acompañamiento personalizado.
        </p>

        <p style="color:#9ca3af; font-size:15px; margin-top:25px;">
            Gracias por tu compromiso y dedicación en el desarrollo educativo de cada estudiante. 💙
        </p>

        <p style="color:#ccc; font-size:14px; margin-top:25px;">
            Con aprecio,<br>
            <strong>Equipo PREDU Vocacional</strong>
        </p>
    </div>
    """

    return generar_template_base(
        titulo="👨‍🏫 Nuevo estudiante asignado a tu grupo | PREDU",
        contenido_html=contenido
    )
