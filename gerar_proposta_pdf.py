import os
import sys
import base64
import subprocess
import qrcode
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

SITE_URL = sys.argv[1] if len(sys.argv) > 1 else "https://brothaus-engelke.vercel.app"
print(f"[*] Gerando proposta RADICAL BAUHAUS para Brothaus Engelke: {SITE_URL}")

# 1. Gerar QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=14,
    border=1,
)
qr.add_data(SITE_URL)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="#111111", back_color="#FFFFFF").convert("RGBA")
qr_path = os.path.join(BASE_DIR, "temp_qrcode.png")
qr_img.save(qr_path)

def to_base64(path):
    if not os.path.exists(path):
        print(f"[!] Arquivo nao encontrado: {path}")
        return ""
    with open(path, "rb") as f:
        ext = os.path.splitext(path)[1].lower().replace(".", "")
        if ext == "svg":
            mime = "image/svg+xml"
        elif ext in ["jpg", "jpeg"]:
            mime = "image/jpeg"
        else:
            mime = "image/png"
        return f"data:{mime};base64,{base64.b64encode(f.read()).decode('utf-8')}"

# Carregar imagens em Base64
b64_logo = to_base64(os.path.join(ASSETS_DIR, "logo_cisne_bronze_3d.png"))
b64_totem = to_base64(os.path.join(ASSETS_DIR, "totem_real_foto_dusk.jpg"))
b64_fornada = to_base64(os.path.join(ASSETS_DIR, "crop_b_macro.jpg"))
b64_swan_3d = to_base64(os.path.join(BASE_DIR, "preview_cisne_3d_viewer.png"))
b64_qr = to_base64(qr_path)

html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>PROPOSTA BAUHAUS • BROTHAUS ENGELKE</title>
  <!-- Google Fonts: O Arsenal Radical Bauhaus (Big Shoulders 900 + Staatliches Weimar 1923 + Plus Jakarta Sans) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800;900&family=Staatliches&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    @page {{
      size: A4;
      margin: 0;
    }}
    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
      border-radius: 0 !important; /* REGRA BAUHAUS: ZERO BORDAS ARREDONDADAS */
    }}
    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: #F4F1EA;
      color: #111111;
      -webkit-font-smoothing: antialiased;
    }}

    /* ==========================================================================
       CANVAS A4 CONSTRUTIVISTA
       ========================================================================== */
    .page {{
      width: 210mm;
      height: 297mm;
      padding: 12mm 15mm 10mm 15mm;
      position: relative;
      page-break-after: always;
      background-color: #F4F1EA;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      overflow: hidden;
      border: 6px solid #111111;
    }}
    .page:last-child {{
      page-break-after: avoid;
    }}

    .page-inner {{
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      flex: 1;
      margin: 8px 0;
    }}

    /* ==========================================================================
       TIPOGRAFIA MONUMENTAL (BIG SHOULDERS 900 & STAATLICHES)
       ========================================================================== */
    .font-bauhaus {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      text-transform: uppercase;
      line-height: 0.92;
      letter-spacing: -0.02em;
    }}
    .font-staatliches {{
      font-family: 'Staatliches', sans-serif;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }}

    /* Linha Construtivista de Divisão */
    .bauhaus-rule {{
      display: flex;
      align-items: center;
      width: 100%;
      height: 3px;
      background: #111111;
      margin: 8px 0;
      position: relative;
    }}
    .bauhaus-rule.red {{
      background: #D63D33;
    }}
    .bauhaus-rule-split {{
      display: grid;
      grid-template-columns: 2fr 1fr;
      height: 3px;
      margin: 8px 0;
    }}
    .rule-black {{ background: #111111; height: 100%; }}
    .rule-red {{ background: #D63D33; height: 100%; }}

    /* ==========================================================================
       CABEÇALHO MONUMENTAL
       ========================================================================== */
    .header-bauhaus {{
      display: grid;
      grid-template-columns: auto 1fr auto;
      align-items: center;
      gap: 16px;
      padding-bottom: 6px;
    }}
    .header-logo-box {{
      width: 64px;
      height: 64px;
      background: #FFFFFF;
      border: 2.5px solid #111111;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 3px;
    }}
    .header-logo-box img {{
      width: 100%;
      height: 100%;
      object-fit: contain;
    }}
    .header-title-block {{
      display: flex;
      flex-direction: column;
    }}
    .header-eyebrow {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 9px;
      font-weight: 800;
      letter-spacing: 0.22em;
      color: #D63D33;
      text-transform: uppercase;
      margin-bottom: 2px;
    }}
    .header-title {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 42px;
      line-height: 0.88;
      letter-spacing: -0.01em;
      color: #111111;
    }}
    .header-title span {{
      color: #D63D33;
    }}
    .header-sub {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 9px;
      font-weight: 700;
      letter-spacing: 0.12em;
      color: #666056;
      text-transform: uppercase;
      margin-top: 3px;
    }}
    .header-badge-solid {{
      background: #111111;
      color: #F4F1EA;
      padding: 6px 14px;
      text-align: right;
      border-left: 4px solid #D63D33;
    }}
    .header-badge-solid .top {{
      font-family: 'Staatliches', sans-serif;
      font-size: 14px;
      letter-spacing: 1.5px;
      color: #FFFFFF;
    }}
    .header-badge-solid .sub {{
      font-size: 8px;
      font-weight: 700;
      color: #D63D33;
      letter-spacing: 1px;
      text-transform: uppercase;
    }}

    /* ==========================================================================
       BLOCO 1: O MANIFESTO MONUMENTAL
       ========================================================================== */
    .manifesto-monumental {{
      display: grid;
      grid-template-columns: 1.25fr 1fr;
      gap: 18px;
      background: #FFFFFF;
      border: 3px solid #111111;
      padding: 16px 20px;
      position: relative;
    }}
    .manifesto-monumental::before {{
      content: "";
      position: absolute;
      top: -3px;
      left: -3px;
      width: 14px;
      height: 14px;
      background: #D63D33;
    }}
    .manifesto-left h2 {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 36px;
      line-height: 0.92;
      color: #111111;
      text-transform: uppercase;
      letter-spacing: -0.01em;
      margin-bottom: 8px;
    }}
    .manifesto-left h2 span {{
      color: #D63D33;
    }}
    .manifesto-left p {{
      font-size: 11.5px;
      line-height: 1.55;
      color: #33302B;
      font-weight: 500;
    }}
    .manifesto-left p strong {{
      color: #111111;
      font-weight: 800;
    }}

    /* 4 Números Monumentais */
    .stat-quad {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      background: #F4F1EA;
      padding: 12px;
      border: 2px solid #111111;
    }}
    .stat-item {{
      border-left: 3px solid #111111;
      padding-left: 10px;
    }}
    .stat-item.highlight {{
      border-left-color: #D63D33;
    }}
    .stat-val {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 38px;
      line-height: 0.85;
      color: #111111;
    }}
    .stat-item.highlight .stat-val {{
      color: #D63D33;
    }}
    .stat-lbl {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 8.5px;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: #555047;
      margin-top: 2px;
      line-height: 1.2;
    }}

    /* ==========================================================================
       BLOCO 2: DIAGNÓSTICO VS. ARQUITETURA (CONSTRUTIVISMO BRUTO)
       ========================================================================== */
    .contrast-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
    }}
    .contrast-box {{
      border: 2.5px solid #111111;
      background: #FFFFFF;
      padding: 14px 16px;
    }}
    .contrast-box.bad {{
      border-top: 6px solid #D63D33;
    }}
    .contrast-box.good {{
      border-top: 6px solid #111111;
    }}
    .contrast-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
      padding-bottom: 5px;
      border-bottom: 1.5px solid #E2DDD2;
    }}
    .contrast-header h3 {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 20px;
      letter-spacing: 0.02em;
      text-transform: uppercase;
      color: #111111;
      line-height: 1;
    }}
    .contrast-box.bad .contrast-header h3 {{ color: #D63D33; }}
    .contrast-tag {{
      font-family: 'Staatliches', sans-serif;
      font-size: 10px;
      letter-spacing: 1px;
      padding: 2px 6px;
      color: #FFFFFF;
      background: #111111;
    }}
    .contrast-box.bad .contrast-tag {{ background: #D63D33; }}
    .contrast-list {{
      list-style: none;
      font-size: 10.5px;
      color: #33302B;
    }}
    .contrast-list li {{
      margin-bottom: 8px;
      position: relative;
      padding-left: 18px;
      line-height: 1.45;
    }}
    .contrast-list li:last-child {{ margin-bottom: 0; }}
    .contrast-box.bad li::before {{
      content: "✕";
      position: absolute;
      left: 0;
      color: #D63D33;
      font-weight: 900;
      font-size: 11px;
    }}
    .contrast-box.good li::before {{
      content: "■";
      position: absolute;
      left: 0;
      color: #111111;
      font-size: 9px;
      top: 1px;
    }}

    /* ==========================================================================
       BLOCO 3: OS 3 ELEMENTOS REAIS (POSTER BAUHAUS)
       ========================================================================== */
    .section-banner-title {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: #111111;
      color: #FFFFFF;
      padding: 6px 14px;
      margin-bottom: 8px;
    }}
    .section-banner-title h3 {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 18px;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      line-height: 1;
    }}
    .section-banner-title span {{
      font-family: 'Staatliches', sans-serif;
      font-size: 11px;
      color: #D63D33;
      letter-spacing: 1.5px;
    }}
    .showcase-bauhaus {{
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 12px;
    }}
    .showcase-card {{
      background: #FFFFFF;
      border: 2.5px solid #111111;
      padding: 6px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .showcase-img-box {{
      position: relative;
      width: 100%;
      height: 136px;
      overflow: hidden;
      border: 1px solid #111111;
      background: #111111;
    }}
    .showcase-img-box img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }}
    .showcase-number {{
      position: absolute;
      top: 0;
      left: 0;
      background: #D63D33;
      color: #FFFFFF;
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 18px;
      line-height: 1;
      padding: 4px 8px;
    }}
    .showcase-text {{
      padding: 8px 4px 2px 4px;
    }}
    .showcase-text strong {{
      display: block;
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 15px;
      color: #111111;
      text-transform: uppercase;
      letter-spacing: 0.02em;
      line-height: 1.1;
      margin-bottom: 2px;
    }}
    .showcase-text p {{
      font-size: 9.8px;
      color: #555047;
      line-height: 1.35;
    }}

    /* ==========================================================================
       BLOCO 4: OS 5 CAPÍTULOS (BARRA INDUSTRIAL)
       ========================================================================== */
    .chapters-strip {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 6px;
      background: #111111;
      padding: 6px;
      border: 2.5px solid #111111;
    }}
    .chapter-block {{
      background: #FFFFFF;
      padding: 6px 4px;
      text-align: center;
      border-top: 3px solid #D63D33;
    }}
    .chapter-idx {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 18px;
      line-height: 0.9;
      color: #D63D33;
    }}
    .chapter-label {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 9px;
      font-weight: 800;
      color: #111111;
      text-transform: uppercase;
      line-height: 1.15;
      margin-top: 2px;
    }}

    /* ==========================================================================
       RODAPÉ CONSTRUTIVISTA
       ========================================================================== */
    .footer-bauhaus {{
      display: grid;
      grid-template-columns: 1fr auto;
      align-items: center;
      padding-top: 6px;
      border-top: 3px solid #111111;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 9.5px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: #444039;
    }}
    .footer-right {{
      font-family: 'Staatliches', sans-serif;
      font-size: 12px;
      letter-spacing: 2px;
      color: #D63D33;
    }}

    /* ==========================================================================
       PÁGINA 2: QR HERO, PLANOS MONUMENTAIS & FECHAMENTO
       ========================================================================== */
    .qr-constructivist {{
      display: grid;
      grid-template-columns: 140px 1fr auto;
      align-items: center;
      gap: 18px;
      background: #FFFFFF;
      border: 3.5px solid #111111;
      padding: 14px 18px;
      position: relative;
    }}
    .qr-constructivist::after {{
      content: "";
      position: absolute;
      bottom: -3.5px;
      right: -3.5px;
      width: 20px;
      height: 20px;
      background: #D63D33;
    }}
    .qr-frame {{
      width: 124px;
      height: 124px;
      border: 3px solid #111111;
      padding: 4px;
      background: #FFFFFF;
      position: relative;
    }}
    .qr-frame img {{
      width: 100%;
      height: 100%;
      display: block;
    }}
    .qr-triangle-accent {{
      width: 0;
      height: 0;
      border-left: 35px solid transparent;
      border-right: 35px solid transparent;
      border-bottom: 60px solid #D63D33; /* O Triângulo Vermelho Kandinsky da referência! */
      margin: 0 auto;
    }}
    .qr-text-block h2 {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 32px;
      line-height: 0.95;
      color: #111111;
      text-transform: uppercase;
      letter-spacing: -0.01em;
      margin-bottom: 6px;
    }}
    .qr-text-block h2 span {{
      color: #D63D33;
    }}
    .qr-text-block p {{
      font-size: 10.5px;
      line-height: 1.4;
      color: #33302B;
      font-weight: 500;
      margin-bottom: 8px;
    }}
    .qr-pill-black {{
      display: inline-block;
      background: #111111;
      color: #FFFFFF;
      font-family: 'Staatliches', sans-serif;
      font-size: 13px;
      letter-spacing: 1.5px;
      padding: 4px 12px;
    }}

    /* Planos de Preço Monumentais */
    .plans-constructivist {{
      display: grid;
      grid-template-columns: 1fr 1.05fr;
      gap: 14px;
    }}
    .plan-box {{
      background: #FFFFFF;
      border: 3px solid #111111;
      padding: 14px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
    }}
    .plan-box.featured {{
      border: 3.5px solid #D63D33;
      background: #FAF8F2;
    }}
    .plan-corner-tag {{
      position: absolute;
      top: -12px;
      right: 14px;
      background: #D63D33;
      color: #FFFFFF;
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 13px;
      letter-spacing: 1.5px;
      padding: 2px 10px;
      text-transform: uppercase;
    }}
    .plan-name {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 26px;
      line-height: 0.95;
      color: #111111;
      text-transform: uppercase;
      letter-spacing: 0.01em;
    }}
    .plan-desc {{
      font-size: 10px;
      font-weight: 700;
      color: #D63D33;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-top: 2px;
      margin-bottom: 10px;
    }}
    .plan-items {{
      list-style: none;
      font-size: 10px;
      color: #33302B;
      margin-bottom: 12px;
    }}
    .plan-items li {{
      margin-bottom: 5px;
      position: relative;
      padding-left: 16px;
      line-height: 1.35;
    }}
    .plan-items li:last-child {{ margin-bottom: 0; }}
    .plan-items li::before {{
      content: "■";
      position: absolute;
      left: 0;
      color: #111111;
      font-size: 9px;
      top: 1px;
    }}
    .plan-box.featured .plan-items li::before {{
      color: #D63D33;
    }}

    .price-monumental {{
      border-top: 3px solid #111111;
      padding-top: 8px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }}
    .price-monumental .lbl {{
      font-family: 'Staatliches', sans-serif;
      font-size: 11px;
      letter-spacing: 1.2px;
      color: #666056;
    }}
    .price-monumental .val {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 38px;
      line-height: 0.85;
      color: #111111;
      letter-spacing: -0.02em;
      white-space: nowrap;
    }}
    .plan-box.featured .price-monumental .val {{
      color: #D63D33;
    }}
    .price-monumental .terms {{
      font-size: 9.5px;
      font-weight: 700;
      color: #666056;
      text-align: right;
      max-width: 120px;
      line-height: 1.25;
      text-transform: uppercase;
    }}

    /* Faixa de Parceria Construtivista */
    .barter-strip {{
      display: grid;
      grid-template-columns: auto 1fr auto;
      align-items: center;
      gap: 14px;
      background: #FFFFFF;
      border: 3px solid #111111;
      padding: 12px 16px;
    }}
    .barter-badge {{
      background: #D63D33;
      color: #FFFFFF;
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 26px;
      line-height: 0.9;
      padding: 6px 10px;
      text-align: center;
      letter-spacing: 0.05em;
    }}
    .barter-text strong {{
      display: block;
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 18px;
      color: #111111;
      letter-spacing: 0.04em;
      line-height: 1;
      text-transform: uppercase;
      margin-bottom: 2px;
    }}
    .barter-text p {{
      font-size: 10.5px;
      line-height: 1.45;
      color: #33302B;
    }}
    .barter-roi {{
      background: #111111;
      color: #FFFFFF;
      font-family: 'Staatliches', sans-serif;
      font-size: 13px;
      letter-spacing: 1.5px;
      padding: 8px 12px;
      text-align: center;
      line-height: 1.2;
    }}
    .barter-roi span {{
      color: #D63D33;
      display: block;
      font-size: 9px;
      letter-spacing: 1px;
    }}

    /* Bloco de Assinatura */
    .author-constructivist {{
      display: grid;
      grid-template-columns: 1fr auto;
      align-items: center;
      background: #111111;
      color: #FFFFFF;
      padding: 14px 20px;
      border-left: 6px solid #D63D33;
    }}
    .author-title {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 26px;
      line-height: 0.95;
      letter-spacing: 0.02em;
      text-transform: uppercase;
      color: #FFFFFF;
    }}
    .author-title span {{
      color: #D63D33;
    }}
    .author-sub {{
      font-size: 10px;
      font-weight: 600;
      letter-spacing: 0.12em;
      color: #BBB4A4;
      text-transform: uppercase;
      margin-top: 3px;
    }}
    .author-cta-btn {{
      background: #D63D33;
      color: #FFFFFF;
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 18px;
      letter-spacing: 1.5px;
      padding: 8px 18px;
      text-transform: uppercase;
      text-decoration: none;
    }}
  </style>
</head>
<body>

  <!-- =========================================================================
       PÁGINA 1: O MANIFESTO BAUHAUS ENGELKE
       ========================================================================= -->
  <div class="page">
    <!-- Header -->
    <div class="header-bauhaus">
      <div class="header-logo-box">
        <img src="{b64_logo}" alt="Cisne Engelke">
      </div>
      <div class="header-title-block">
        <div class="header-eyebrow">ARQUITETURA DIGITAL ARTESANAL • RIO TAVARES CENTRAL</div>
        <div class="header-title">BROTHAUS <span>ENGELKE</span></div>
        <div class="header-sub">CAFÉ & PÃES ARTESANAIS DEMETER • DESDE 2013</div>
      </div>
      <div class="header-badge-solid">
        <div class="top">PROPOSTA 2026</div>
        <div class="sub">DIRETO AO BALCÃO</div>
      </div>
    </div>

    <div class="bauhaus-rule-split">
      <div class="rule-black"></div>
      <div class="rule-red"></div>
    </div>

    <!-- Corpo Página 1 -->
    <div class="page-inner">
      <!-- 1. Manifesto Monumental com 4 Estatísticas de Peso -->
      <div class="manifesto-monumental">
        <div class="manifesto-left">
        <h2>O PÃO VIVO NÃO ACEITA PRESSA.<br><span>SEU SITE TAMBÉM NÃO.</span></h2>
        <p>
          A Brothaus Engelke não usa melhorador químico industrial: vocês levam <strong>36 horas fermentando grãos Demeter</strong> e cuidam de cada detalhe com dedicação manual. Assim como vocês fazem pães vivos, este site é um <strong>produto artesanal esculpido em código aqui no Rio Tavares</strong>.
        </p>
      </div>
        <div class="stat-quad">
          <div class="stat-item highlight">
            <div class="stat-val">36H</div>
            <div class="stat-lbl">Fermentação Natural Lenta</div>
          </div>
          <div class="stat-item">
            <div class="stat-val">100%</div>
            <div class="stat-lbl">Grãos Demeter Orgânicos</div>
          </div>
          <div class="stat-item">
            <div class="stat-val">0%</div>
            <div class="stat-lbl">Aditivos ou Conservantes</div>
          </div>
          <div class="stat-item highlight">
            <div class="stat-val">2013</div>
            <div class="stat-lbl">Padaria no Rio Tavares</div>
          </div>
        </div>
      </div>

      <!-- 2. O Choque de Realidade (Diagnóstico Construtivista) -->
      <div class="contrast-grid">
        <div class="contrast-box bad">
          <div class="contrast-header">
            <h3>O Gargalo Atual na Bio</h3>
            <div class="contrast-tag">PERDA DE VALOR</div>
          </div>
          <ul class="contrast-list">
            <li><strong>Link genérico (bit.ly):</strong> Endereço frio e sem catálogo fotográfico.</li>
            <li><strong>Link quebrado do Wix:</strong> Aponta para artigo longo da certificadora sem conversão.</li>
            <li><strong>Invisibilidade:</strong> Quem passa na servidão não sabe da autêntica Sachertorte vienense e do centeio Demeter.</li>
          </ul>
        </div>
        <div class="contrast-box good">
          <div class="contrast-header">
            <h3>A Solução no Ar (Já Pronta)</h3>
            <div class="contrast-tag">NO TOQUE</div>
          </div>
          <ul class="contrast-list">
            <li><strong>Totem do Cisne 3D:</strong> A escultura de latão da servidão interativa em WebGL.</li>
            <li><strong>Apresentação dos Grãos:</strong> Capítulos editoriais com alma e autoridade artesanal.</li>
            <li><strong>Venda Direta no Balcão:</strong> Botão WhatsApp com pedido formatado, sem taxas de iFood ou Wix.</li>
          </ul>
        </div>
      </div>

      <!-- 3. A Transposição Estética dos 3 Elementos Reais -->
      <div>
        <div class="section-banner-title">
          <h3>A TRANSPOSIÇÃO DOS 3 ELEMENTOS REAIS DA LOJA</h3>
          <span>CONSTRUÇÃO VISUAL PURA</span>
        </div>
        <div class="showcase-bauhaus">
          <div class="showcase-card">
            <div class="showcase-img-box">
              <span class="showcase-number">01</span>
              <img src="{b64_totem}" alt="Totem Real">
            </div>
            <div class="showcase-text">
              <strong>O TOTEM DA SERVIDÃO</strong>
              <p>A placa iluminada real com o cisne no crepúsculo da Servidão Elpídio da Rocha.</p>
            </div>
          </div>
          <div class="showcase-card">
            <div class="showcase-img-box">
              <span class="showcase-number">02</span>
              <img src="{b64_swan_3d}" alt="Cisne 3D">
            </div>
            <div class="showcase-text">
              <strong>O CISNE 3D NO CELULAR</strong>
              <p>O totem forjado em latão transposto para Three.js interativo na mão do cliente.</p>
            </div>
          </div>
          <div class="showcase-card">
            <div class="showcase-img-box">
              <span class="showcase-number">03</span>
              <img src="{b64_fornada}" alt="Fornada Real">
            </div>
            <div class="showcase-text">
              <strong>A FORNADA DE 36 HORAS</strong>
              <p>A crosta dourada e os cortes do pão vivo em alta definição para encomenda direta no balcão.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- 4. Os 5 Capítulos Narrativos (Barra Industrial) -->
      <div>
        <div class="chapters-strip">
          <div class="chapter-block">
            <div class="chapter-idx">01</div>
            <div class="chapter-label">Proêmio & Cisne 3D</div>
          </div>
          <div class="chapter-block">
            <div class="chapter-idx">02</div>
            <div class="chapter-label">Terra & Demeter</div>
          </div>
          <div class="chapter-block">
            <div class="chapter-idx">03</div>
            <div class="chapter-label">Fogo & Levain 36h</div>
          </div>
          <div class="chapter-block">
            <div class="chapter-idx">04</div>
            <div class="chapter-label">Sachertorte 1832</div>
          </div>
          <div class="chapter-block">
            <div class="chapter-idx">05</div>
            <div class="chapter-label">Fornada no Zap</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Rodapé Página 1 -->
    <div class="footer-bauhaus">
      <div>BROTHAUS ENGELKE • SERVIDÃO ELPÍDIO DA ROCHA, 105 • RIO TAVARES CENTRAL</div>
      <div class="footer-right">PÁGINA 01 // 02</div>
    </div>
  </div>

  <!-- =========================================================================
       PÁGINA 2: QR HERO, PLANOS MONUMENTAIS & INVESTIMENTO
       ========================================================================= -->
  <div class="page">
    <!-- Header Página 2 -->
    <div class="header-bauhaus">
      <div class="header-logo-box">
        <img src="{b64_logo}" alt="Cisne Engelke">
      </div>
      <div class="header-title-block">
        <div class="header-eyebrow">DEMONSTRAÇÃO PRÁTICA AO VIVO NO BALCÃO</div>
        <div class="header-title">INVESTIMENTO <span>& RETORNO</span></div>
        <div class="header-sub">SEM MENSALIDADES OU TAXAS • PAGAMENTO ÚNICO</div>
      </div>
      <div class="header-badge-solid">
        <div class="top">SEM MENSALIDADE</div>
        <div class="sub">ZERO RECORRÊNCIA</div>
      </div>
    </div>

    <div class="bauhaus-rule-split">
      <div class="rule-black"></div>
      <div class="rule-red"></div>
    </div>

    <!-- Corpo Página 2 -->
    <div class="page-inner">
      <!-- 1. Hero do QR Code Construtivista -->
      <div class="qr-constructivist">
        <div class="qr-frame">
          <img src="{b64_qr}" alt="QR Code">
        </div>
        <div class="qr-text-block">
          <h2>EXPERIMENTE O SITE<br><span>NO SEU PRÓPRIO CELULAR</span></h2>
          <p>
            Aponte a câmera do seu telefone para o código. O site já está construído e rodando ao vivo, com o cisne em 3D, a história biodinâmica, as fornadas e o botão direto para o WhatsApp da Brothaus.
          </p>
          <div class="qr-pill-black">🔗 {SITE_URL}</div>
        </div>
        <div>
          <!-- O Triângulo Vermelho Kandinsky da Referência -->
          <div class="qr-triangle-accent"></div>
        </div>
      </div>

      <!-- 2. Grid de Planos Monumentais -->
      <div class="plans-constructivist">
        <!-- Plano 1 -->
        <div class="plan-box">
          <div>
            <div class="plan-name">PLANO 01 // NA BIO HOJE</div>
            <div class="plan-desc">Implementação imediata no Instagram da Brothaus</div>
            <ul class="plan-items">
              <li><strong>Seção de Encomendas:</strong> Reserva de fornadas e pães no WhatsApp.</li>
              <li>Site completo publicado em infraestrutura de alta velocidade.</li>
              <li>Totem do Cisne 3D interativo (Three.js/WebGL).</li>
              <li>Capítulos dos Pães Demeter, Levain 36h e Confeitaria.</li>
              <li><strong>Ajustes e melhorias inclusos:</strong> Acompanhamento e pequenos ajustes na semana seguinte sem custo extra.</li>
              <li><strong>Zero mensalidades de software ou plataforma.</strong></li>
              <li>Link no ar no balcão em 15 minutos.</li>
            </ul>
          </div>
          <div class="price-monumental">
            <div>
              <div class="lbl">PAGAMENTO ÚNICO</div>
              <div class="val">R$ 380</div>
            </div>
            <div class="terms">PIX (OU R$ 285 + R$ 95 EM CONSUMAÇÃO)</div>
          </div>
        </div>

        <!-- Plano 2 -->
        <div class="plan-box featured">
          <div class="plan-corner-tag">MAIS COMPLETO</div>
          <div>
            <div class="plan-name">PLANO 02 // BOUTIQUE COMPLETA</div>
            <div class="plan-desc">Identidade completa com domínio próprio e suporte</div>
            <ul class="plan-items">
              <li><strong>Tudo incluso no Plano 01.</strong></li>
              <li>Registro e configuração de domínio oficial (<code>brothausengelke.com.br</code>).</li>
              <li>QR Code em vetor de alta resolução para impressão de plaquinhas de mesa e balcão físico.</li>
              <li>Atualizações de fotos e fornadas sazonais inclusas por 6 meses.</li>
              <li>Otimização para buscas locais no Google Maps.</li>
            </ul>
          </div>
          <div class="price-monumental">
            <div>
              <div class="lbl">PAGAMENTO ÚNICO</div>
              <div class="val">R$ 680</div>
            </div>
            <div class="terms">OU 2X R$ 350 (OU ATÉ 25% EM CONSUMAÇÃO)</div>
          </div>
        </div>
      </div>

      <!-- 3. Parceria de Vizinhança (25% em Consumação) -->
      <div class="barter-strip">
        <div class="barter-badge">25%<br><span style="font-size: 10px; display:block; font-weight:700;">PERMUTA</span></div>
        <div class="barter-text">
          <strong>CONDIÇÃO ESPECIAL DE VIZINHANÇA: 25% EM CONSUMAÇÃO</strong>
          <p>
            Se for conveniente para vocês, <strong>até 25% do valor pode ser pago em consumo</strong> de pães, cafés ou doces na própria Brothaus (ex: R$ 285 no PIX + R$ 95 em produtos), com prazos e regras definidos livremente por vocês.
          </p>
        </div>
        <div class="barter-roi">
          ~3 TORTAS<br>
          <span>EQUIVALE À SACHERTORTE</span>
        </div>
      </div>

      <!-- 4. Bloco de Assinatura do Artífice -->
      <div class="author-constructivist">
        <div>
          <div class="author-title">CARLOS LINZMEYER <span>• SOFTWARE ARTESANAL</span></div>
          <div class="author-sub">Morador e desenvolvedor no Rio Tavares, Florianópolis - SC • Ajustes presenciais inclusos</div>
        </div>
        <div>
          <span class="author-cta-btn">SUBIR NA BIO HOJE →</span>
        </div>
      </div>
    </div>

    <!-- Rodapé Página 2 -->
    <div class="footer-bauhaus">
      <div>BROTHAUS ENGELKE • ATENDIMENTO DIRETO: (48) 99830-1122</div>
      <div class="footer-right">PÁGINA 02 // 02</div>
    </div>
  </div>

</body>
</html>
"""

html_path = os.path.join(BASE_DIR, "proposta_comercial_engelke.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[OK] Arquivo HTML Bauhaus gerado: {html_path}")

pdf_path = os.path.join(BASE_DIR, "proposta_editorial_brothaus_engelke.pdf")
if os.path.exists(pdf_path):
    try:
        os.remove(pdf_path)
    except Exception as e:
        print(f"[!] Aviso: {e}")

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_path):
    edge_path = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

print(f"[*] Compilando PDF Bauhaus via Edge Headless...")
cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    html_path
]

res = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 0:
    print(f"[OK] PDF Bauhaus compilado com sucesso! ({os.path.getsize(pdf_path)/1024:.1f} KB)")
else:
    print(f"[!] Erro ao compilar PDF: {res.stderr}")

try:
    import pypdfium2 as pdfium
    pdf = pdfium.PdfDocument(pdf_path)
    for i, page in enumerate(pdf):
        image = page.render(scale=2).to_pil()
        image.save(os.path.join(BASE_DIR, f"preview_proposta_page_{i+1}.png"))
    print(f"[OK] Previews atualizados com sucesso ({len(pdf)} páginas).")
except Exception as e:
    print(f"[!] Erro ao gerar previews: {e}")

if os.path.exists(qr_path):
    os.remove(qr_path)
