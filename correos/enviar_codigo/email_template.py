from correos.template_base import generar_template_base


def generar_html_codigo_acceso(nombre_estudiante: str, unique_code: str, institucion: str, region: str,
                               director_name: str, teaching_modality: str):
    """
    Genera el contenido HTML del correo para enviar el código de acceso a estudiantes
    con un diseño formal oscuro y visual moderno.
    """

    # Dividimos el código en cuadros (cada carácter dentro de un <span>)
    # Se añade el 'role="presentation"' para mejorar la accesibilidad
    codigo_formateado = "".join(
        f"<span role='presentation' style='display:inline-block; width:38px; height:38px; line-height:38px; "
        f"margin:3px; background:#111; border:1px solid #333; border-radius:8px; "
        f"font-family:\"Press Start 2P\", cursive; font-size:15px; color:#facc15; "
        f"text-shadow:0 0 6px rgba(250,204,21,0.8); text-align:center;'>{letra}</span>"
        for letra in unique_code
    )

    contenido_html = f"""
    <p style="font-size:15px; color:#e5e5e5;">
      Estimado(a) <strong>{nombre_estudiante}</strong> 👋,
    </p>

    <p style="font-size:14px; color:#cfcfcf; line-height:1.6;">
      Te damos la bienvenida a <strong>PREDU Vocacional</strong>.  
      Esta comunicación confirma tu registro desde la institución <strong>{institucion}</strong>,
      ubicada en la región <strong>{region}</strong>.
    </p>

    <div style="background:linear-gradient(145deg,#0d0d0d,#1c1c1c); 
                padding:24px; 
                border-radius:16px; 
                margin:30px 0; 
                text-align:center; 
                box-shadow:inset 0 0 20px rgba(255,255,255,0.05),
                           0 0 20px rgba(250,204,21,0.15); 
                border:1px solid #333;">

      <p style="font-size:14px; color:#ccc; margin-bottom:12px;">
        🔐 Tu código de acceso institucional:
      </p>

      <div style="margin:10px 0;">
        {codigo_formateado}
      </div>

      <p style="font-size:12px; color:#facc15; background:#1a1a1a; padding:8px; border-radius:6px; margin-top:18px;">
        ⚠️ Por favor, selecciona y copia el código para usarlo.
      </p>
      <p style="font-size:12px; color:#aaa; margin-top:12px;">
        Guarda este código. Lo necesitarás para acceder a tu panel de estudiantes.
      </p>
    </div>

    <p style="font-size:14px; color:#ccc; line-height:1.6;">
      📚 Modalidad de enseñanza: <strong>{teaching_modality.capitalize()}</strong><br>
      👨‍🏫 Director: <strong>{director_name}</strong>
    </p>

    <p style="font-size:13px; color:#888; margin-top:25px; text-align:center;">
  Si no solicitaste este acceso, puedes ignorar este mensaje.  
  Este correo fue generado automáticamente por el sistema PREDU Vocacional.
</p>

    <style>
      /* Aunque la animación CSS puede funcionar en algunos clientes, se mantiene para un mejor diseño en clientes compatibles */
      @keyframes pulseGlow {{
        0% {{ text-shadow:0 0 6px rgba(250,204,21,0.6); }}
        50% {{ text-shadow:0 0 12px rgba(250,204,21,1); }}
        100% {{ text-shadow:0 0 6px rgba(250,204,21,0.6); }}
      }}
      span.code-char {{
        animation:pulseGlow 2s infinite ease-in-out;
      }}
    </style>
    """

    return generar_template_base(
        titulo="🔑 Código de Acceso PREDU Vocacional",
        contenido_html=contenido_html
    )