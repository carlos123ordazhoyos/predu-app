from correos.template_base import generar_template_base


def generar_html_bienvenida_tutor(nombre_tutor: str, institucion: str, logo_url: str, enlace_panel: str) -> str:
    """
    Genera el cuerpo HTML del correo de bienvenida para tutores.
    """

    contenido = f"""
    <div style="text-align:center; padding:25px;">
        <img src="{logo_url}" alt="Logo Institución" style="width:100px; border-radius:12px; margin-bottom:15px;"/>

        <h2 style="color:#06b6d4; font-size:24px;">👩‍🏫 ¡Bienvenido(a) a PREDU, {nombre_tutor}!</h2>

        <p style="color:#d1d5db; font-size:16px; margin-top:10px;">
            Es un honor contar contigo como <strong>tutor(a) vocacional</strong> en la institución 
            <strong style="color:#facc15;">{institucion}</strong>. 
        </p>

        <p style="color:#e5e7eb; font-size:16px; margin-top:15px;">
            Tu rol será fundamental para guiar a los estudiantes en su desarrollo académico, emocional 
            y vocacional, ayudándolos a descubrir sus fortalezas y tomar decisiones con propósito. 🌱
        </p>

        <div style="background:#1f2937; border-radius:12px; padding:20px; margin-top:25px; border:1px solid #374151;">
            <h3 style="color:#06b6d4; font-size:18px;">Accede a tu panel de tutor:</h3>
            <a href="{enlace_panel}" 
               style="display:inline-block; margin-top:15px; background:#06b6d4; color:white;
               padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:bold;">
                Ir al Panel del Tutor
            </a>
        </div>

        <p style="color:#9ca3af; font-size:15px; margin-top:25px;">
            En <strong>PREDU Vocacional</strong> creemos que cada tutor es una guía clave en el crecimiento de los estudiantes. 
            ¡Gracias por ser parte de esta misión educativa!
        </p>

        <p style="color:#ccc; font-size:14px; margin-top:25px;">
            Con aprecio,<br>
            <strong>El equipo de PREDU Vocacional 💙</strong>
        </p>
    </div>
    """

    return generar_template_base(
        titulo=f"👩‍🏫 Bienvenido(a) a PREDU — {institucion}",
        contenido_html=contenido
    )
