from correos.template_base import generar_template_base


def generar_html_tutor_cuenta_rechazada(nombre_tutor: str, motivo_rechazo: str, fecha_revision: str, logo_url: str) -> str:
    """
    Genera el cuerpo HTML del correo que notifica al tutor
    que su solicitud de creación de cuenta independiente fue rechazada.
    """

    contenido = f"""
    <div style="text-align:center; padding:25px;">
        <img src="{logo_url}" alt="Logo Institución" style="width:100px; border-radius:12px; margin-bottom:20px;"/>

        <h2 style="color:#f87171; font-size:24px;">⚠️ Solicitud No Aprobada</h2>
        <p style="color:#e5e7eb; font-size:17px; margin-top:10px;">
            Estimado/a <strong>{nombre_tutor}</strong>, lamentamos informarte que tu solicitud
            para crear una cuenta de <strong>Tutor Independiente</strong> en <strong>PREDU Vocacional</strong>
            <span style="color:#f87171; font-weight:bold;">no ha sido aprobada</span> en esta ocasión.
        </p>

        <div style="background:#1f2937; border-radius:12px; padding:22px; margin:25px 0; border:1px solid #374151; text-align:left;">
            <p style="color:#f87171; font-weight:bold; font-size:17px;">📋 Detalles de la Revisión</p>
            <p style="color:#e5e7eb; font-size:15px; margin:6px 0;">
                <strong>Nombre del Tutor:</strong> {nombre_tutor}
            </p>
            <p style="color:#e5e7eb; font-size:15px; margin:6px 0;">
                <strong>Fecha de Revisión:</strong> {fecha_revision}
            </p>
            <p style="color:#e5e7eb; font-size:15px; margin:6px 0;">
                <strong>Motivo del Rechazo:</strong> {motivo_rechazo}
            </p>
        </div>

        <p style="color:#d1d5db; font-size:16px;">
            Te invitamos a revisar los requisitos y volver a postular cuando consideres que cumples con los criterios solicitados.
            Nuestro equipo estará encantado de reconsiderar tu solicitud en el futuro. 🙌
        </p>

        <p style="color:#60a5fa; font-size:16px; margin-top:25px;">
            💡 Consejo: puedes reforzar tu perfil agregando experiencia educativa o certificaciones relevantes.
        </p>

        <p style="color:#ccc; font-size:14px; margin-top:30px;">
            Con aprecio,<br>
            <strong>Equipo PREDU Vocacional</strong>
        </p>
    </div>
    """

    return generar_template_base(
        titulo="⚠️ Solicitud de Tutor No Aprobada | PREDU",
        contenido_html=contenido
    )
