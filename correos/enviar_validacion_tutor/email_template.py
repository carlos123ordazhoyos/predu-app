from correos.template_base import generar_template_base


def generar_html_validacion_tutor(nombre_estudiante: str, nombre_tutor: str, consejo_tutor: str) -> str:
    """
    Genera el cuerpo HTML del correo que notifica al estudiante
    la validación de sus reportes por parte de su tutor.
    """

    contenido = f"""
    <div style="text-align:center; padding:20px;">
        <h2 style="color:#22c55e; font-size:22px;">📋 Validación completada</h2>
        <p style="color:#d1d5db; font-size:16px; margin-top:10px;">
            Hola <strong>{nombre_estudiante}</strong>, tu tutor <strong>{nombre_tutor}</strong> ha revisado y validado tus reportes académicos y psicológicos. 🎓
        </p>

        <div style="background:#1a1a1a; border-radius:12px; padding:20px; margin-top:20px; border:1px solid #2d2d2d;">
            <h3 style="color:#facc15; font-size:18px; margin-bottom:10px;">💬 Consejo del Tutor</h3>
            <p style="color:#d1d5db; font-size:15px; line-height:1.7; font-style:italic;">
                “{consejo_tutor}”
            </p>
        </div>

        <p style="color:#a5b4fc; font-size:15px; margin-top:25px;">
            Este consejo se basa en la interpretación de tus resultados y busca acompañarte 
            en tu desarrollo académico y personal dentro de <strong>PREDU Vocacional</strong>.
        </p>

        <a href="https://predu.app/reportes" 
           style="display:inline-block; margin-top:20px; background:#3b82f6; color:white; 
           padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:bold;">
            Ver mis reportes validados
        </a>

        <p style="color:#ccc; font-size:14px; margin-top:25px;">
            Con aprecio,<br>
            <strong>El equipo de PREDU Vocacional 💙</strong>
        </p>
    </div>
    """

    return generar_template_base(
        titulo="✅ Validación de Reportes — Tutor PREDU",
        contenido_html=contenido
    )
