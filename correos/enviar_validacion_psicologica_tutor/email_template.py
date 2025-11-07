from correos.template_base import generar_template_base


def generar_html_validacion_psicologica_tutor(nombre_estudiante: str, nombre_tutor: str, consejo_tutor: str) -> str:
    """
    Genera el cuerpo HTML del correo que notifica al estudiante
    la validación del reporte psicológico por parte de su tutor.
    """

    contenido = f"""
    <div style="text-align:center; padding:20px;">
        <h2 style="color:#06b6d4; font-size:22px;">🧠 Validación de Reporte Psicológico</h2>

        <p style="color:#d1d5db; font-size:16px; margin-top:10px;">
            Hola <strong>{nombre_estudiante}</strong>, tu tutor <strong>{nombre_tutor}</strong> ha revisado 
            tu <strong>Reporte Psicológico Vocacional</strong> y ha completado su validación 🧩.
        </p>

        <div style="background:#1a1a1a; border-radius:12px; padding:20px; margin-top:20px; border:1px solid #2d2d2d;">
            <h3 style="color:#facc15; font-size:18px; margin-bottom:10px;">💬 Consejo del Tutor</h3>
            <p style="color:#d1d5db; font-size:15px; line-height:1.7; font-style:italic;">
                “{consejo_tutor}”
            </p>
        </div>

        <p style="color:#a5b4fc; font-size:15px; margin-top:25px;">
            Esta retroalimentación te ayudará a comprender mejor tus fortalezas personales, 
            tus motivaciones y cómo se relacionan con tu perfil vocacional. 
        </p>

        <a href="https://predu.app/reporte-psicologico" 
           style="display:inline-block; margin-top:20px; background:#06b6d4; color:white; 
           padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:bold;">
            Ver Reporte Psicológico Validado
        </a>

        <p style="color:#ccc; font-size:14px; margin-top:25px;">
            Con aprecio,<br>
            <strong>El equipo de PREDU Vocacional 💙</strong>
        </p>
    </div>
    """

    return generar_template_base(
        titulo="🧠 Validación del Reporte Psicológico — Tutor PREDU",
        contenido_html=contenido
    )
