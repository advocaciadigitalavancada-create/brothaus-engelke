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

# Carregar imagens em Base64 (Edição Radical Bauhaus Typofoto)
b64_logo = to_base64(os.path.join(BASE_DIR, "assets_bw", "logo_bw.png"))
b64_totem = to_base64(os.path.join(BASE_DIR, "assets_bw", "totem_bw.jpg"))
b64_costura = to_base64(os.path.join(BASE_DIR, "assets_bw", "costura_bw.png"))
b64_swan_3d = to_base64(os.path.join(BASE_DIR, "assets_bw", "cisne_3d_bw.png"))
b64_qr = to_base64(qr_path)

html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>PROPOSTA RADICAL BAUHAUS • BROTHAUS ENGELKE</title>
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
      background-color: #FFFFFF;
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
      background-color: #FFFFFF;
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
      background: #111111;
    }}
    .bauhaus-rule-split {{
      display: grid;
      grid-template-columns: 2fr 1fr;
      height: 3px;
      margin: 8px 0;
    }}
    .rule-black {{ background: #111111; height: 100%; }}
    .rule-red {{ background: #111111; height: 100%; }}

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
      color: #111111;
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
      color: #111111;
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
      color: #FFFFFF;
      padding: 6px 14px;
      text-align: right;
      border-left: 4px solid #111111;
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
      color: #111111;
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
      background: #111111;
    }}
    .manifesto-left h2 {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 42px;
      line-height: 0.88;
      color: #111111;
      text-transform: uppercase;
      letter-spacing: -0.01em;
      margin-bottom: 8px;
    }}
    .manifesto-left h2 span {{
      color: #111111;
      display: block;
    }}
    .manifesto-left p {{
      font-size: 12.5px;
      line-height: 1.45;
      color: #222222;
      font-weight: 600;
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
      background: #FFFFFF;
      padding: 12px;
      border: 2px solid #111111;
    }}
    .stat-item {{
      border-left: 4px solid #111111;
      padding-left: 10px;
    }}
    .stat-item.highlight {{
      border-left-color: #111111;
    }}
    .stat-val {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 44px;
      line-height: 0.82;
      color: #111111;
    }}
    .stat-item.highlight .stat-val {{
      color: #111111;
    }}
    .stat-lbl {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 8.5px;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: #444444;
      margin-top: 3px;
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
      border: 3px solid #111111;
      background: #FFFFFF;
      padding: 14px 16px;
    }}
    .contrast-box.bad {{
      border-top: 8px solid #111111;
    }}
    .contrast-box.good {{
      background: #111111;
      color: #FFFFFF;
      border: 3px solid #111111;
      border-top: 8px solid #111111;
    }}
    .contrast-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
      padding-bottom: 5px;
      border-bottom: 2px solid #111111;
    }}
    .contrast-box.good .contrast-header {{
      border-bottom: 2px solid #333333;
    }}
    .contrast-header h3 {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 22px;
      letter-spacing: 0.02em;
      text-transform: uppercase;
      color: #111111;
      line-height: 1;
    }}
    .contrast-box.bad .contrast-header h3 {{ color: #111111; }}
    .contrast-box.good .contrast-header h3 {{ color: #FFFFFF; }}
    .contrast-tag {{
      font-family: 'Staatliches', sans-serif;
      font-size: 10px;
      letter-spacing: 1px;
      padding: 2px 8px;
      color: #FFFFFF;
      background: #111111;
    }}
    .contrast-box.good .contrast-tag {{
      background: #FFFFFF;
      color: #111111;
    }}
    .contrast-list {{
      list-style: none;
      font-size: 11.5px;
      color: #222222;
    }}
    .contrast-box.good .contrast-list {{
      color: #EEEEEE;
    }}
    .contrast-box.good .contrast-list strong {{
      color: #FFFFFF;
    }}
    .contrast-list li {{
      margin-bottom: 6px;
      position: relative;
      padding-left: 18px;
      line-height: 1.4;
    }}
    .contrast-list li:last-child {{ margin-bottom: 0; }}
    .contrast-box.bad li::before {{
      content: "✕";
      position: absolute;
      left: 0;
      color: #111111;
      font-weight: 900;
      font-size: 12px;
    }}
    .contrast-box.good li::before {{
      content: "■";
      position: absolute;
      left: 0;
      color: #FFFFFF;
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
      color: #FFFFFF;
      letter-spacing: 1.5px;
    }}
    .showcase-bauhaus {{
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 12px;
    }}
    .showcase-card {{
      background: #FFFFFF;
      border: 3px solid #111111;
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
      border: 1.5px solid #111111;
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
      background: #111111;
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
      color: #444444;
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
      border: 3px solid #111111;
    }}
    .chapter-block {{
      background: #FFFFFF;
      padding: 6px 4px;
      text-align: center;
      border-top: 3px solid #111111;
    }}
    .chapter-block:nth-child(even) {{
      background: #111111;
      color: #FFFFFF;
      border-top: 3px solid #FFFFFF;
    }}
    .chapter-idx {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 20px;
      line-height: 0.9;
      color: #111111;
    }}
    .chapter-block:nth-child(even) .chapter-idx {{
      color: #FFFFFF;
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
    .chapter-block:nth-child(even) .chapter-label {{
      color: #FFFFFF;
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
      color: #111111;
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
      background: #111111;
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
      border-bottom: 60px solid #111111; /* O Triângulo Vermelho Kandinsky da referência! */
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
      color: #111111;
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
      border: 3.5px solid #111111;
      background: #111111;
      color: #FFFFFF;
    }}
    .plan-box.featured .plan-name {{
      color: #FFFFFF;
    }}
    .plan-box.featured .plan-desc {{
      color: #CCCCCC;
    }}
    .plan-box.featured .plan-items {{
      color: #EEEEEE;
    }}
    .plan-box.featured .plan-items strong {{
      color: #FFFFFF;
    }}
    .plan-box.featured .plan-items li::before {{
      color: #FFFFFF;
    }}
    .plan-box.featured .plan-items code {{
      background: #2A2A2A;
      color: #FFFFFF;
      padding: 1px 4px;
    }}
    .plan-box.featured .price-monumental {{
      border-top: 3px solid #333333;
    }}
    .plan-box.featured .price-monumental .lbl {{
      color: #AAAAAA;
    }}
    .plan-box.featured .price-monumental .val {{
      color: #FFFFFF;
    }}
    .plan-box.featured .price-monumental .terms {{
      color: #CCCCCC;
    }}
    .plan-corner-tag {{
      position: absolute;
      top: -12px;
      right: 14px;
      background: #FFFFFF;
      color: #111111;
      border: 2px solid #111111;
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
      color: #111111;
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
      color: #111111;
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
      color: #FFFFFF !important;
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
      background: #111111;
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
      color: #CCCCCC;
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
      padding: 12px 18px;
      border: 3px solid #111111;
    }}
    .author-title {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 24px;
      line-height: 0.95;
      letter-spacing: 0.02em;
      text-transform: uppercase;
      color: #FFFFFF;
    }}
    .author-title span {{
      color: #CCCCCC;
    }}
    .author-sub {{
      font-size: 10px;
      font-weight: 600;
      letter-spacing: 0.12em;
      color: #CCCCCC;
      text-transform: uppercase;
      margin-top: 3px;
    }}
    .author-cta-btn {{
      background: #FFFFFF;
      color: #111111;
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 15px;
      letter-spacing: 1.2px;
      padding: 6px 14px;
      display: inline-block;
      text-transform: uppercase;
    }}
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
        <div class="header-eyebrow">DESENVOLVIMENTO DE SITES SOB MEDIDA • RIO TAVARES</div>
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
          <h2>PÃO ARTESANAL.<br><span>SITE SOB MEDIDA.</span></h2>
          <p>
            Fermentação lenta de 36h e grãos Demeter. Um site direto no Rio Tavares para ver o cardápio e pedir no balcão.
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
            <h3>Hoje na Bio</h3>
            <div class="contrast-tag">PERDA DE VENDA</div>
          </div>
          <ul class="contrast-list">
            <li><strong>Link genérico:</strong> Sem fotos dos pães e doces.</li>
            <li><strong>Página antiga:</strong> Não gera pedidos no WhatsApp.</li>
            <li><strong>Invisibilidade:</strong> O cliente não vê a Sachertorte.</li>
          </ul>
        </div>
        <div class="contrast-box good">
          <div class="contrast-header">
            <h3>No Ar Hoje</h3>
            <div class="contrast-tag">VENDA DIRETA</div>
          </div>
          <ul class="contrast-list">
            <li><strong>Cisne 3D:</strong> A escultura da entrada no celular.</li>
            <li><strong>Cardápio Visual:</strong> Pães Demeter e fornadas do dia.</li>
            <li><strong>WhatsApp Direto:</strong> Pedidos formatados sem taxas.</li>
          </ul>
        </div>
      </div>

      <!-- 3. A Transposição Estética dos 3 Elementos Reais -->
      <div>
        <div class="section-banner-title">
          <h3>DETALHES REAIS DA PADARIA NO SITE</h3>
          <span>IDENTIDADE LOCAL</span>
        </div>
        <div class="showcase-bauhaus">
          <div class="showcase-card">
            <div class="showcase-img-box">
              <span class="showcase-number">01</span>
              <img src="{b64_totem}" alt="Totem Real">
            </div>
            <div class="showcase-text">
              <strong>O TOTEM DA SERVIDÃO</strong>
              <p>A placa com o cisne na Servidão Elpídio da Rocha fotografada no local.</p>
            </div>
          </div>
          <div class="showcase-card">
            <div class="showcase-img-box">
              <span class="showcase-number">02</span>
              <img src="{b64_swan_3d}" alt="Cisne 3D">
            </div>
            <div class="showcase-text">
              <strong>O CISNE 3D NO CELULAR</strong>
              <p>O monograma EvS (von Schwanenflügel: asas de cisnes) esculpido em 3D.</p>
            </div>
          </div>
          <div class="showcase-card">
            <div class="showcase-img-box">
              <span class="showcase-number">03</span>
              <img src="{b64_costura}" alt="Costura Real">
            </div>
            <div class="showcase-text">
              <strong>A COSTURA MANUAL</strong>
              <p>O acabamento em linha vermelha do cardápio físico refletido no visual do site.</p>
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
          <div class="author-title">CARLOS LINZMEYER <span>• SITES SOB MEDIDA</span></div>
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

html_path = os.path.join(BASE_DIR, "proposta_comercial_engelke_pb.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[OK] Arquivo HTML Bauhaus gerado: {html_path}")

pdf_path = os.path.join(BASE_DIR, "proposta_editorial_engelke_preto_e_branco.pdf")
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
        image.save(os.path.join(BASE_DIR, f"preview_pb_page_{i+1}.png"))
    print(f"[OK] Previews atualizados com sucesso ({len(pdf)} páginas).")
except Exception as e:
    print(f"[!] Erro ao gerar previews: {e}")

if os.path.exists(qr_path):
    os.remove(qr_path)
