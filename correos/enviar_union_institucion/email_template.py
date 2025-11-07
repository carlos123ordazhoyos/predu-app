from correos.template_base import generar_template_base


def generar_html_union_institucion(nombre_estudiante: str, nombre_institucion: str, lugar: str, nombre_encargado: str, logo_url: str, mensaje_motivador: str) -> str:
    """
    Genera el cuerpo HTML del correo de bienvenida y felicitación
    al estudiante por unirse a una institución educativa.
    """

    contenido = f"""
    <div style="text-align:center; padding:20px;">
        <img src="{logo_url}" alt="Logo de {nombre_institucion}" style="width:120px; border-radius:12px; margin-bottom:15px;"/>

        <h2 style="color:#06b6d4; font-size:22px;">🎓 ¡Felicidades, {nombre_estudiante}!</h2>
        <p style="color:#d1d5db; font-size:16px; margin-top:10px;">
            Nos complace anunciarte que ahora formas parte de la institución educativa 
            <strong style="color:#facc15;">{nombre_institucion}</strong>, ubicada en 
            <strong>{lugar}</strong>.
        </p>

        <div style="background:#1a1a1a; border-radius:12px; padding:20px; margin-top:20px; border:1px solid #2d2d2d;">
            <h3 style="color:#a5b4fc; font-size:18px;">👩‍🏫 Encargado Institucional:</h3>
            <p style="color:#e5e7eb; font-size:16px; margin:8px 0 15px;">
                <strong>{nombre_encargado}</strong><br>
                Te dará la bienvenida oficial y te acompañará en este nuevo camino académico.
            </p>

            <p style="color:#9ca3af; font-size:15px; font-style:italic; margin-top:10px;">
                “{mensaje_motivador}”
            </p>
        </div>

        <p style="color:#d1d5db; font-size:16px; margin-top:25px;">
            En <strong>PREDU Vocacional</strong> celebramos contigo este nuevo paso en tu desarrollo personal y profesional.
        </p>

        <a href="https://predu.app/institucion" 
           style="display:inline-block; margin-top:20px; background:#06b6d4; color:white; 
           padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:bold;">
            Ver Detalles de la Institución
        </a>

        <p style="color:#ccc; font-size:14px; margin-top:25px;">
            Con entusiasmo,<br>
            <strong>El equipo de PREDU Vocacional 💙</strong>
        </p>
    </div>
    """

    return generar_template_base(
        titulo=f"🎓 ¡Bienvenido a {nombre_institucion}! — PREDU",
        contenido_html=contenido
    )
