from correos.template_base import generar_template_base


def generar_html_reporte_psicologico(nombre_estudiante: str, facultad: str, consejo_psicologico: str):
    """
    Genera el contenido HTML del correo para enviar el reporte psicológico
    basado en el resultado del test RIASEC.
    """

    contenido_html = f"""
    <p style="font-size:16px; color:#e5e5e5;">
      ¡Hola, <strong>{nombre_estudiante}</strong>! 👋
    </p>

    <p style="font-size:14px; color:#d1d5db; line-height:1.7;">
      Hemos analizado tus respuestas del test <strong>RIASEC</strong> y, según tu perfil psicológico y vocacional, 
      te recomendamos explorar la siguiente facultad:
    </p>

    <div style="background:linear-gradient(145deg, #0f0f0f, #1a1a1a);
                padding:22px;
                border-radius:14px;
                text-align:center;
                margin:28px 0;
                box-shadow:0 0 25px rgba(250, 204, 21, 0.15), inset 0 0 10px rgba(255, 255, 255, 0.05);
                border:1px solid rgba(250,204,21,0.3);">

        <h2 style="color:#facc15; 
                   font-family:'Poppins',sans-serif;
                   font-size:22px;
                   margin-bottom:10px;
                   text-shadow:0 0 10px rgba(250,204,21,0.5);">
            {facultad}
        </h2>

        <p style="font-size:13px; color:#9ca3af; line-height:1.6; margin-top:12px;">
            Este resultado refleja tus intereses, habilidades y valores. 
            Recuerda que cada decisión que tomes es parte de tu crecimiento profesional 💫
        </p>
    </div>

    <div style="background:#111; 
                border-left:4px solid #facc15;
                padding:15px 18px; 
                border-radius:8px; 
                margin-top:20px;">
        <h3 style="color:#facc15; font-size:15px; margin:0 0 8px 0;">
            💭 Consejo Psicológico Personalizado:
        </h3>
        <p style="font-size:13px; color:#d1d5db; line-height:1.6; margin:0;">
            {consejo_psicologico}
        </p>
    </div>

    <p style="font-size:13px; color:#aaa; margin-top:30px; text-align:center;">
      Reporte generado automáticamente por <strong>PREDU</strong>.  
      <br> Desarrollado con 💛 por el equipo <strong>AD Academy</strong>.
    </p>
    """

    return generar_template_base(
        titulo="🧠 Reporte Psicológico Vocacional | PREDU",
        contenido_html=contenido_html
    )
