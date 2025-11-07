from correos.template_base import generar_template_base


def generar_html_tutor_cuenta_aprobada(nombre_tutor: str, fecha_aprobacion: str, logo_url: str) -> str:
    """
    Genera el cuerpo HTML del correo que notifica al tutor
    la aprobación de su cuenta independiente.
    """

    contenido = f"""
    <div style="text-align:center; padding:25px;">
        <img src="{logo_url}" alt="Logo Institución" style="width:100px; border-radius:12px; margin-bottom:20px;"/>

        <h2 style="color:#22c55e; font-size:24px;">🎉 ¡Solicitud Aprobada!</h2>
        <p style="color:#e5e7eb; font-size:17px; margin-top:10px;">
            Estimado/a <strong>{nombre_tutor}</strong>, nos complace informarte que tu solicitud
            para crear una cuenta de <strong>Tutor Independiente</strong> en <strong>PREDU Vocacional</strong>
            ha sido <span style="color:#22c55e; font-weight:bold;">aprobada con éxito</span>.
        </p>

        <div style="background:#1f2937; border-radius:12px; padding:22px; margin:25px 0; border:1px solid #374151; text-align:left;">
            <p style="color:#facc15; font-weight:bold; font-size:17px;">🧾 Detalles de Aprobación</p>
            <p style="color:#e5e7eb; font-size:15px; margin:6px 0;">
                <strong>Nombre del Tutor:</strong> {nombre_tutor}
            </p>
            <p style="color:#e5e7eb; font-size:15px; margin:6px 0;">
                <strong>Fecha de Aprobación:</strong> {fecha_aprobacion}
            </p>
            <p style="color:#e5e7eb; font-size:15px; margin:6px 0;">
                <strong>Estado de Cuenta:</strong> Activa ✅
            </p>
        </div>

        <p style="color:#d1d5db; font-size:16px;">
            A partir de este momento puedes acceder a tu cuenta, gestionar tus grupos educativos
            y comenzar a orientar a estudiantes de manera independiente.
        </p>

        <p style="color:#60a5fa; font-size:16px; margin-top:25px;">
            💡 Recuerda que en PREDU valoramos tu compromiso con la educación y el acompañamiento vocacional.
        </p>

        <p style="color:#ccc; font-size:14px; margin-top:30px;">
            Con aprecio,<br>
            <strong>Equipo PREDU Vocacional</strong>
        </p>
    </div>
    """

    return generar_template_base(
        titulo="🎓 Cuenta de Tutor Independiente Aprobada | PREDU",
        contenido_html=contenido
    )
