from correos.template_base import generar_template_base


def generar_html_bienvenida(nombre_estudiante: str) -> str:
    """
    Genera el cuerpo HTML del correo de bienvenida a PREDU.
    """

    contenido = f"""
    <div style="text-align:center; padding:20px;">
        <h2 style="color:#facc15; font-size:24px;">👋 ¡Bienvenido/a a PREDU, {nombre_estudiante}!</h2>
        <p style="color:#d1d5db; font-size:16px; margin-top:10px;">
            Nos alegra mucho tenerte con nosotros. 🎓<br><br>
            PREDU es una plataforma diseñada para ayudarte a descubrir tu vocación, 
            potenciar tus habilidades y construir el futuro que mereces. 🚀
        </p>

        <div style="background:#1a1a1a; border-radius:10px; padding:20px; margin-top:20px;">
            <p style="color:#9ca3af; font-size:15px; line-height:1.6;">
                Aquí podrás acceder a herramientas de orientación vocacional, 
                análisis de perfil psicológico (RIASEC), y reportes personalizados
                para guiarte en tu camino académico y profesional.
            </p>
        </div>

        <p style="color:#a5b4fc; font-size:15px; margin-top:25px;">
            🌟 <strong>Consejo:</strong> Da el primer paso completando tu evaluación vocacional.
        </p>

        <p style="color:#ccc; font-size:14px; margin-top:25px;">
            Con cariño,<br>
            <strong>El equipo de PREDU Vocacional 💙</strong>
        </p>
    </div>
    """

    html = generar_template_base(
        titulo="🎉 Bienvenido/a a PREDU Vocacional",
        contenido_html=contenido
    )

    return html
