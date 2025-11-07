from correos.template_base import generar_template_base


def generar_html_reporte_academico(nombre_estudiante: str, carrera: str, recomendacion_academica: str):
    """
    Genera el contenido HTML del correo para enviar el reporte académico
    basado en el resultado del modelo académico (GraphSAGE).
    """

    contenido_html = f"""
    <p style="font-size:16px; color:#e5e5e5;">
      ¡Hola, <strong>{nombre_estudiante}</strong>! 👋
    </p>

    <p style="font-size:14px; color:#d1d5db; line-height:1.7;">
      Hemos analizado tus calificaciones y habilidades en las diferentes áreas académicas evaluadas. 
      Según el modelo de análisis de <strong>PREDU Vocacional</strong>, tu perfil se alinea con la siguiente carrera:
    </p>

    <div style="background:linear-gradient(145deg, #111, #1c1c1c);
                padding:24px;
                border-radius:14px;
                text-align:center;
                margin:28px 0;
                box-shadow:0 0 25px rgba(250, 204, 21, 0.15), inset 0 0 10px rgba(255, 255, 255, 0.05);
                border:1px solid rgba(250,204,21,0.3);">

        <h2 style="color:#facc15; 
                   font-family:'Press Start 2P', cursive;
                   font-size:20px;
                   margin-bottom:10px;
                   text-shadow:0 0 12px rgba(250,204,21,0.6);">
            {carrera}
        </h2>

        <p style="font-size:13px; color:#9ca3af; line-height:1.6; margin-top:12px;">
            Este resultado refleja tu desempeño y afinidad con las competencias académicas que caracterizan a esta carrera. 
            ¡Sigue potenciando tus talentos! 🚀
        </p>
    </div>

    <div style="background:#111; 
                border-left:4px solid #3b82f6;
                padding:15px 18px; 
                border-radius:8px; 
                margin-top:20px;">
        <h3 style="color:#3b82f6; font-size:15px; margin:0 0 8px 0;">
            📘 Recomendación Académica:
        </h3>
        <p style="font-size:13px; color:#d1d5db; line-height:1.6; margin:0;">
            {recomendacion_academica}
        </p>
    </div>

    <p style="font-size:13px; color:#aaa; margin-top:30px; text-align:center;">
      Reporte generado automáticamente por <strong>PREDU</strong>.<br>
      Desarrollado con 💛 por el equipo <strong>AD Academy</strong>.
    </p>
    """

    return generar_template_base(
        titulo="📘 Reporte Académico Vocacional | PREDU",
        contenido_html=contenido_html
    )
