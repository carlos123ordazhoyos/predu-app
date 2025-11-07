from correos.template_base import generar_template_base


def generar_html_resultado(facultad_academica: str, facultad_psicologica: str) -> str:
    """
    Genera el cuerpo HTML del correo de resultados vocacionales
    mostrando las facultades sugeridas tanto por el test psicológico (RIASEC)
    como por el análisis académico.
    """

    contenido = f"""
    <p style="font-size:15px; color:#f3f4f6; text-align:center; margin-bottom:20px;">
      🎓 <strong>¡Felicitaciones!</strong><br>
      Has completado tu evaluación vocacional y aquí tienes tu <strong>reporte integral</strong>:
    </p>

    <div style="background-color:#0f0f0f; 
                border-radius:14px; 
                padding:22px 25px; 
                margin:25px 0; 
                border:1px solid #2d2d2d;
                box-shadow:0 0 15px rgba(250,204,21,0.2), inset 0 0 8px rgba(255,255,255,0.05);
                animation: fadeIn 2s ease-in-out;">

        <h3 style="color:#facc15; font-size:18px; margin-bottom:12px; text-align:center;">
            🔍 Análisis de Facultades Sugeridas
        </h3>

        <div style="background:#1a1a1a; padding:16px; border-radius:10px; margin-bottom:14px;">
            <p style="color:#d1d5db; margin:0;">🧠 <strong>Facultad sugerida (Test Psicológico RIASEC):</strong></p>
            <p style="color:#a78bfa; font-size:15px; font-weight:bold; margin:6px 0 0 0;">
                {facultad_psicologica}
            </p>
        </div>

        <div style="background:#1a1a1a; padding:16px; border-radius:10px;">
            <p style="color:#d1d5db; margin:0;">📘 <strong>Facultad recomendada (Análisis Académico):</strong></p>
            <p style="color:#60a5fa; font-size:15px; font-weight:bold; margin:6px 0 0 0;">
                {facultad_academica}
            </p>
        </div>
    </div>

    <p style="color:#ccc; font-size:14px; line-height:1.6;">
      💡 Este resultado combina tus fortalezas académicas y tus intereses personales,
      ofreciéndote una orientación integral para elegir tu futuro profesional.
    </p>

    <p style="color:#bbb; font-size:13px; text-align:center; margin-top:25px;">
      🌟 Confía en tus talentos, sigue tu pasión y construye tu camino con propósito.<br>
      ¡Tu futuro te está esperando! 🚀
    </p>

    <style>
      @keyframes fadeIn {{
        0% {{ opacity: 0; transform: translateY(10px); }}
        100% {{ opacity: 1; transform: translateY(0); }}
      }}
    </style>
    """

    html = generar_template_base(
        titulo="🎓 Reporte de Facultades — PREDU Vocacional",
        contenido_html=contenido
    )

    return html
