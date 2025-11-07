from correos.template_base import generar_template_base


def generar_html_pago_finalizado(nombre_estudiante: str, tipo_cuenta: str, fecha_fin: str, logo_url: str) -> str:
    """
    Genera el cuerpo HTML del correo notificando que el pago o suscripción de la cuenta ha finalizado.
    """

    contenido = f"""
    <div style="text-align:center; padding:25px;">
        <img src="{logo_url}" alt="Logo PREDU" style="width:100px; border-radius:12px; margin-bottom:20px;"/>

        <h2 style="color:#facc15; font-size:24px;">⚠️ Tu suscripción ha finalizado</h2>
        <p style="color:#e5e7eb; font-size:16px; margin-top:10px;">
            Hola <strong>{nombre_estudiante}</strong>, queremos informarte que tu periodo de suscripción de la cuenta
            <strong>{tipo_cuenta}</strong> ha <span style="color:#f87171;">finalizado</span> el día <strong>{fecha_fin}</strong>.
        </p>

        <div style="background:#1f2937; border-radius:12px; padding:20px; margin:25px 0; border:1px solid #374151;">
            <p style="color:#facc15; font-weight:bold; font-size:17px;">📅 Detalles de tu cuenta</p>
            <p style="color:#e5e7eb; font-size:15px; margin:6px 0;">
                <strong>Tipo de cuenta:</strong> {tipo_cuenta}
            </p>
            <p style="color:#e5e7eb; font-size:15px; margin:6px 0;">
                <strong>Fecha de finalización:</strong> {fecha_fin}
            </p>
        </div>

        <p style="color:#d1d5db; font-size:15px;">
            Para seguir disfrutando de los beneficios de <strong>PREDU Vocacional</strong>, te invitamos a renovar tu plan.
            Mantén el acceso a tus reportes, evaluaciones y acompañamiento educativo personalizado. 🚀
        </p>

        <a href="https://predu.pe/planes" 
           style="display:inline-block; background-color:#facc15; color:#000; 
                  font-weight:bold; padding:12px 22px; border-radius:10px; 
                  margin-top:20px; text-decoration:none;">
            🔄 Renovar mi suscripción
        </a>

        <p style="color:#9ca3af; font-size:13px; margin-top:30px;">
            Si ya realizaste el pago, ignora este mensaje o comunícate con soporte.<br>
            💬 <strong>soporte@predu.pe</strong>
        </p>

        <p style="color:#ccc; font-size:14px; margin-top:30px;">
            Con aprecio,<br>
            <strong>Equipo PREDU Vocacional</strong>
        </p>
    </div>
    """

    return generar_template_base(
        titulo="⚠️ Fin de Suscripción | PREDU Vocacional",
        contenido_html=contenido
    )
