def generar_template_base(titulo: str, contenido_html: str) -> str:
    """Plantilla base oscura con estilo vocacional tipo PREDU"""
    return f"""
    <html>
      <head>
        <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
      </head>
      <body style="font-family: 'Segoe UI', Arial, sans-serif; background-color:#0d0d0d; color:#f1f1f1; padding:40px;">
        <div style="max-width:600px; margin:auto; background-color:#1a1a1a; border-radius:12px; box-shadow:0 0 20px rgba(255,255,255,0.05); padding:25px;">

          <!-- Encabezado -->
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
  <!-- Logo -->
  <img src="https://firebasestorage.googleapis.com/v0/b/studio-545694841-babc5.firebasestorage.app/o/logo%2Fgraduation.png?alt=media&token=27270fcc-3d39-430d-a1ab-e872e340e4b0" 
       alt="Logo PREDU" style="height:50px; margin-right:20px;">

  <!-- Círculos de colores alineados a la derecha -->
  <div style="display:flex; justify-content:flex-end; gap:16px; margin-left:auto;">
    <div style="width:10px; height:10px; border-radius:50%; background-color:#ff5f56;"></div>
    <div style="width:10px; height:10px; border-radius:50%; background-color:#ffbd2e;"></div>
    <div style="width:10px; height:10px; border-radius:50%; background-color:#27c93f;"></div>
  </div>
</div>


          <h2 style="text-align:center; color:#facc15; font-family:'Press Start 2P', cursive; font-size:14px; letter-spacing:1px;">
            {titulo}
          </h2>

          <div style="margin-top:25px; color:#ddd; line-height:1.6;">
            {contenido_html}
          </div>

          <hr style="border:none; border-top:1px solid #333; margin:30px 0;">

          <p style="font-size:11px; color:#888; text-align:center; line-height:1.5;">
            Plataforma educativa de Orientación Vocacional | <strong>PREDU</strong>.<br>
            Soporte y desarrollo <strong>Grupo Herrera C&T</strong>.<br>
            © 2025 Todos los derechos reservados.
          </p>

        </div>

        <!-- Mensaje flotante centrado -->
        <div style="position:fixed; bottom:20px; left:50%; transform:translateX(-50%); 
                    background-color:#1f1f1f; border:1px solid #333; padding:14px 18px; 
                    border-radius:10px; font-size:11px; color:#bbb; text-align:center;
                    box-shadow:0 0 10px rgba(255,255,255,0.1); font-family:'Press Start 2P', cursive;
                    line-height:1.6;">
          ✉️ Este mensaje fue generado automáticamente por PREDU.<br>
          <strong>No respondas a este correo.</strong><br>
          Cada resultado te acerca más a tu verdadera vocación. 🚀
        </div>
      </body>
    </html>
    """

