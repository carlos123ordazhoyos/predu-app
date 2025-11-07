from correos.template_base import generar_template_base


def generar_html_subida_plan(nombre_estudiante: str, nuevo_plan: str) -> str:
    """
    Genera el cuerpo HTML del correo que notifica la subida de plan.
    """

    contenido = f"""
    <div style="text-align:center; padding:20px;">
        <h2 style="color:#22c55e; font-size:24px;">🌟 ¡Felicidades, {nombre_estudiante}!</h2>
        <p style="color:#d1d5db; font-size:16px; margin-top:10px;">
            Has mejorado tu experiencia con <strong>PREDU</strong> al subir al plan <strong>{nuevo_plan}</strong>. 🚀
        </p>

        <div style="background:#1a1a1a; border-radius:10px; padding:20px; margin-top:20px;">
            <p style="color:#9ca3af; font-size:15px; line-height:1.6;">
                Ahora tendrás acceso a nuevas funcionalidades exclusivas que te ayudarán a 
                descubrir tu vocación y potenciar tu desarrollo académico:
            </p>
            <ul style="color:#9ca3af; text-align:left; display:inline-block; margin-top:15px;">
                <li>🎯 Evaluaciones vocacionales avanzadas</li>
                <li>📊 Reportes personalizados y detallados</li>
                <li>🧠 Análisis RIASEC con orientación profesional</li>
                <li>💼 Seguimiento académico con inteligencia artificial</li>
            </ul>
        </div>

        <p style="color:#a5b4fc; font-size:15px; margin-top:25px;">
            ¡Tu crecimiento está en marcha! Aprovecha al máximo las nuevas herramientas de PREDU.
        </p>

        <a href="https://predu.app/dashboard" 
           style="display:inline-block; margin-top:20px; background:#3b82f6; color:white; 
           padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:bold;">
            Ir a mi cuenta
        </a>

        <p style="color:#ccc; font-size:14px; margin-top:25px;">
            Con gratitud,<br>
            <strong>El equipo de PREDU Vocacional 💙</strong>
        </p>
    </div>
    """

    return generar_template_base(
        titulo="🚀 Tu plan PREDU ha sido actualizado",
        contenido_html=contenido
    )
