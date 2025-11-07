from correos.template_base import generar_template_base


def generar_html_tutor_agregado_grupo(nombre_grupo: str, nombre_tutor: str, tipo_tutor: str, correo: str, telefono: str, logo_url: str) -> str:
    """
    Genera el cuerpo HTML para notificar que se ha agregado un tutor a un grupo educativo.
    """

    contenido = f"""
    <div style="text-align:center; padding:25px;">
        <img src="{logo_url}" alt="Logo Institución" style="width:100px; border-radius:12px; margin-bottom:15px;"/>
        <h2 style="color:#06b6d4; font-size:24px;">👩‍🏫 ¡Nuevo tutor asignado a tu grupo educativo!</h2>

        <p style="color:#e5e7eb; font-size:16px;">
            Se ha agregado un nuevo tutor al grupo <strong style="color:#facc15;">{nombre_grupo}</strong>.
            A continuación, te compartimos los datos del tutor asignado:
        </p>

        <div style="background:#1f2937; border-radius:12px; padding:20px; margin-top:20px; border:1px solid #374151; text-align:left;">
            <p style="color:#facc15; font-weight:bold; font-size:17px;">👨‍🏫 Datos del Tutor</p>
            <p style="color:#e5e7eb; font-size:15px;"><strong>Nombre:</strong> {nombre_tutor}</p>
            <p style="color:#e5e7eb; font-size:15px;"><strong>Tipo de Tutor:</strong> {tipo_tutor}</p>
            <p style="color:#e5e7eb; font-size:15px;"><strong>Correo:</strong> {correo}</p>
            <p style="color:#e5e7eb; font-size:15px;"><strong>Teléfono:</strong> {telefono}</p>
        </div>

        <p style="color:#d1d5db; font-size:16px; margin-top:25px;">
            Este tutor se encargará de brindar orientación, seguimiento y acompañamiento académico dentro del grupo.
        </p>

        <p style="color:#9ca3af; font-size:15px; margin-top:25px;">
            Gracias por formar parte del compromiso educativo y por fortalecer la comunidad de aprendizaje. 💙
        </p>

        <p style="color:#ccc; font-size:14px; margin-top:25px;">
            Con aprecio,<br>
            <strong>Equipo PREDU Vocacional</strong>
        </p>
    </div>
    """

    return generar_template_base(
        titulo="👩‍🏫 Nuevo tutor agregado al grupo educativo | PREDU",
        contenido_html=contenido
    )
