from correos.template_base import generar_template_base


def generar_html_validacion_academica_tutor(nombre_estudiante: str, nombre_tutor: str, consejo_tutor: str) -> str:
    """
    Genera el cuerpo HTML del correo que notifica al estudiante
    la validación del reporte académico por parte de su tutor.
    """

    contenido = f"""
    <div style="text-align:center; padding:20px;">
        <h2 style="color:#22c55e; font-size:22px;">📘 Validación de Reporte Académico</h2>

        <p style="color:#d1d5db; font-size:16px; margin-top:10px;">
            Hola <strong>{nombre_estudiante}</strong>, tu tutor <strong>{nombre_tutor}</strong> ha revisado 
            tus respuestas en el <strong>Reporte Académico</strong> y ha completado su validación ✅.
        </p>

        <div style="background:#1a1a1a; border-radius:12px; padding:20px; margin-top:20px; border:1px solid #2d2d2d;">
            <h3 style="color:#facc15; font-size:18px; margin-bottom:10px;">🧩 Consejo del Tutor</h3>
            <p style="color:#d1d5db; font-size:15px; line-height:1.7; font-style:italic;">
                “{consejo_tutor}”
            </p>
        </div>

        <p style="color:#a5b4fc; font-size:15px; margin-top:25px;">
            Esta retroalimentación busca reforzar tu desarrollo académico, ayudándote 
            a comprender mejor tus fortalezas y áreas de mejora en el contexto de tu orientación profesional.
        </p>

        <a href="https://predu.app/reporte-academico" 
           style="display:inline-block; margin-top:20px; background:#3b82f6; color:white; 
           padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:bold;">
            Ver Reporte Académico Validado
        </a>

        <p style="color:#ccc; font-size:14px; margin-top:25px;">
            Con aprecio,<br>
            <strong>El equipo de PREDU Vocacional 💙</strong>
        </p>
    </div>
    """

    return generar_template_base(
        titulo="📘 Validación del Reporte Académico — Tutor PREDU",
        contenido_html=contenido
    )
