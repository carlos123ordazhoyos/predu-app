from correos.template_base import generar_template_base


def generar_html_actualizacion_perfil(nombre_estudiante: str, cambios_realizados: list) -> str:
    """
    Genera el cuerpo HTML del correo que notifica al estudiante
    que su perfil ha sido actualizado exitosamente.
    """

    # Convertimos la lista de cambios en un formato visual
    lista_cambios = "".join(
        [f"<li style='color:#d1d5db; font-size:15px;'>• {cambio}</li>" for cambio in cambios_realizados]
    )

    contenido = f"""
    <div style="text-align:center; padding:20px;">
        <h2 style="color:#06b6d4; font-size:22px;">🔄 Actualización de Perfil Completada</h2>

        <p style="color:#d1d5db; font-size:16px; margin-top:10px;">
            Hola <strong>{nombre_estudiante}</strong>, te informamos que se han realizado cambios en tu perfil de usuario en <strong>PREDU Vocacional</strong>.
        </p>

        <div style="background:#1a1a1a; border-radius:12px; padding:20px; margin-top:20px; border:1px solid #2d2d2d;">
            <h3 style="color:#facc15; font-size:18px; margin-bottom:10px;">📝 Cambios realizados:</h3>
            <ul style="list-style:none; padding-left:0; text-align:left; display:inline-block;">
                {lista_cambios}
            </ul>
        </div>

        <p style="color:#a5b4fc; font-size:15px; margin-top:25px;">
            Tu información ya se encuentra actualizada correctamente en nuestros registros.<br>
            Si no realizaste estos cambios, por favor comunícate con nuestro equipo de soporte.
        </p>

        <a href="https://predu.app/perfil" 
           style="display:inline-block; margin-top:20px; background:#06b6d4; color:white; 
           padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:bold;">
            Revisar Perfil Actualizado
        </a>

        <p style="color:#ccc; font-size:14px; margin-top:25px;">
            Con aprecio,<br>
            <strong>El equipo de PREDU Vocacional 💙</strong>
        </p>
    </div>
    """

    return generar_template_base(
        titulo="🔄 Actualización de Perfil — PREDU",
        contenido_html=contenido
    )
