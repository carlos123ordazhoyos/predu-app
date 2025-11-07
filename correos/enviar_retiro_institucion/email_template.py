from correos.template_base import generar_template_base


def generar_html_retiro_institucion(nombre_estudiante: str, nombre_institucion: str, lugar: str, nombre_encargado: str, motivo_retiro: str, logo_url: str) -> str:
    """
    Genera el cuerpo HTML del correo de notificación de retiro institucional.
    """

    contenido = f"""
    <div style="text-align:center; padding:20px;">
        <img src="{logo_url}" alt="Logo de {nombre_institucion}" style="width:100px; border-radius:12px; margin-bottom:15px;"/>

        <h2 style="color:#f87171; font-size:22px;">📋 Notificación de Retiro Institucional</h2>

        <p style="color:#d1d5db; font-size:16px; margin-top:10px;">
            Estimado(a) <strong>{nombre_estudiante}</strong>,<br><br>
            Lamentamos informarte que se ha registrado tu retiro de la institución educativa
            <strong style="color:#facc15;">{nombre_institucion}</strong>, ubicada en <strong>{lugar}</strong>.
        </p>

        <div style="background:#1f2937; border-radius:12px; padding:20px; margin-top:20px; border:1px solid #374151;">
            <h3 style="color:#f87171; font-size:18px;">Motivo del retiro:</h3>
            <p style="color:#e5e7eb; font-size:15px; margin-top:8px;">
                “{motivo_retiro}”
            </p>
        </div>

        <p style="color:#d1d5db; font-size:16px; margin-top:20px;">
            Si consideras que esta decisión fue tomada por error o deseas más información, 
            puedes comunicarte con el encargado institucional:
        </p>

        <div style="background:#111827; border-radius:10px; padding:15px; margin-top:15px;">
            <p style="color:#a5b4fc; font-size:16px;">
                👩‍🏫 <strong>{nombre_encargado}</strong><br>
                <em>Encargado institucional de {nombre_institucion}</em>
            </p>
        </div>

        <p style="color:#9ca3af; font-size:15px; margin-top:25px;">
            En <strong>PREDU Vocacional</strong> valoramos tu dedicación y te animamos a seguir desarrollando tu talento. 
            Cada cierre representa también una nueva oportunidad para crecer. 🌱
        </p>

        <a href="https://predu.app/contacto" 
           style="display:inline-block; margin-top:25px; background:#06b6d4; color:white;
           padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:bold;">
            Contactar con Soporte PREDU
        </a>

        <p style="color:#ccc; font-size:14px; margin-top:25px;">
            Con respeto y aprecio,<br>
            <strong>El equipo de PREDU Vocacional 💙</strong>
        </p>
    </div>
    """

    return generar_template_base(
        titulo=f"📋 Notificación de retiro — {nombre_institucion}",
        contenido_html=contenido
    )
