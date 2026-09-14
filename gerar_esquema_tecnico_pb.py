import os
import sys
import base64
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
ASSETS_BW_DIR = os.path.join(BASE_DIR, "assets_bw")

SITE_URL = "https://brothaus-engelke.vercel.app"
print(f"[*] Gerando ESQUEMA TÉCNICO BAUHAUS para Brothaus Engelke")

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
b64_logo = to_base64(os.path.join(ASSETS_BW_DIR, "logo_bw.png"))

html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>ESQUEMA TÉCNICO • ARQUITETURA SOB MEDIDA • BROTHAUS ENGELKE</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800;900&family=Staatliches&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
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
      border-radius: 0 !important;
    }}
    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: #FFFFFF;
      color: #000000;
      -webkit-font-smoothing: antialiased;
    }}

    .page {{
      width: 210mm;
      height: 297mm;
      padding: 10mm 12mm 8mm 12mm;
      position: relative;
      background-color: #FFFFFF;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      overflow: hidden;
      border: 6px solid #000000;
    }}

    .page-inner {{
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      flex: 1;
      margin: 5px 0;
    }}

    /* TIPOGRAFIA */
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

    /* HEADER */
    .header-bauhaus {{
      display: grid;
      grid-template-columns: auto 1fr auto;
      align-items: center;
      gap: 12px;
      padding-bottom: 6px;
      border-bottom: 4px solid #000000;
    }}
    .header-logo-box {{
      width: 50px;
      height: 50px;
      border: 2px solid #000000;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 3px;
      background: #FFFFFF;
    }}
    .header-logo-box img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
    }}
    .header-title-block {{
      display: flex;
      flex-direction: column;
    }}
    .header-eyebrow {{
      font-family: 'Staatliches', sans-serif;
      font-size: 9.5px;
      letter-spacing: 1.5px;
      color: #000000;
    }}
    .header-title {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 26px;
      line-height: 0.95;
      letter-spacing: 0.02em;
      color: #000000;
    }}
    .header-sub {{
      font-family: 'Staatliches', sans-serif;
      font-size: 8.5px;
      letter-spacing: 1px;
      color: #000000;
      margin-top: 1px;
    }}
    .header-badge-solid {{
      background: #000000;
      color: #FFFFFF;
      padding: 6px 10px;
      text-align: right;
    }}
    .header-badge-solid .top {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 14px;
      line-height: 1;
      letter-spacing: 0.05em;
    }}
    .header-badge-solid .sub {{
      font-family: 'Staatliches', sans-serif;
      font-size: 8px;
      letter-spacing: 1px;
    }}

    /* MANIFESTO / TÍTULO */
    .title-banner {{
      display: grid;
      grid-template-columns: 1.5fr 1fr;
      gap: 12px;
      align-items: stretch;
      border: 2px solid #000000;
      padding: 9px 12px;
      background: #FFFFFF;
    }}
    .title-left h1 {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 26px;
      line-height: 0.95;
      text-transform: uppercase;
      letter-spacing: -0.01em;
      margin-bottom: 4px;
    }}
    .title-left p {{
      font-size: 9.5px;
      line-height: 1.35;
      color: #000000;
    }}
    .title-metrics {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 6px;
      border-left: 2px solid #000000;
      padding-left: 10px;
    }}
    .metric-box {{
      display: flex;
      flex-direction: column;
      justify-content: center;
    }}
    .metric-val {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 22px;
      line-height: 0.9;
    }}
    .metric-lbl {{
      font-family: 'Staatliches', sans-serif;
      font-size: 7.5px;
      letter-spacing: 0.5px;
      line-height: 1.1;
      margin-top: 2px;
    }}

    /* SEÇÃO BLUEPRINT */
    .blueprint-header {{
      background: #000000;
      color: #FFFFFF;
      padding: 4px 10px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 2px;
      margin-bottom: 5px;
    }}
    .blueprint-header h2 {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 15px;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      line-height: 1;
    }}
    .blueprint-header span {{
      font-family: 'Staatliches', sans-serif;
      font-size: 8.5px;
      letter-spacing: 1px;
    }}

    /* GRID DOS 4 MÓDULOS */
    .flow-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
    }}
    .flow-card {{
      border: 2px solid #000000;
      padding: 7px 9px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      background: #FFFFFF;
    }}
    .flow-card.dark {{
      background: #000000;
      color: #FFFFFF;
    }}
    .flow-card-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1.5px solid #000000;
      padding-bottom: 2px;
      margin-bottom: 4px;
    }}
    .flow-card.dark .flow-card-header {{
      border-bottom: 1.5px solid #FFFFFF;
    }}
    .flow-step-num {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 17px;
      line-height: 1;
    }}
    .flow-step-tag {{
      font-family: 'Staatliches', sans-serif;
      font-size: 7.5px;
      letter-spacing: 1px;
      padding: 1px 5px;
      background: #000000;
      color: #FFFFFF;
    }}
    .flow-card.dark .flow-step-tag {{
      background: #FFFFFF;
      color: #000000;
    }}
    .flow-card-title {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 15px;
      line-height: 1;
      text-transform: uppercase;
      margin-bottom: 2px;
    }}
    .flow-card-body {{
      font-size: 8.6px;
      line-height: 1.3;
      margin-bottom: 5px;
    }}
    .flow-card-bullets {{
      list-style: none;
      font-size: 8.2px;
      line-height: 1.25;
    }}
    .flow-card-bullets li {{
      position: relative;
      padding-left: 11px;
      margin-bottom: 2.5px;
    }}
    .flow-card-bullets li:last-child {{ margin-bottom: 0; }}
    .flow-card-bullets li::before {{
      content: "■";
      position: absolute;
      left: 0;
      font-size: 6px;
      top: 1px;
    }}
    .flow-card.dark .flow-card-bullets li::before {{
      color: #FFFFFF;
    }}

    /* TABELA COMPARATIVA */
    .compare-section {{
      border: 2px solid #000000;
      margin-top: 3px;
    }}
    .compare-title {{
      background: #000000;
      color: #FFFFFF;
      padding: 4px 10px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .compare-title h3 {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 13px;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      line-height: 1;
    }}
    .compare-title span {{
      font-family: 'Staatliches', sans-serif;
      font-size: 8px;
      letter-spacing: 1px;
    }}
    .compare-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 8.4px;
    }}
    .compare-table th {{
      background: #EEEEEE;
      text-align: left;
      padding: 3.5px 7px;
      font-family: 'Staatliches', sans-serif;
      letter-spacing: 0.5px;
      font-size: 8px;
      border-bottom: 1.5px solid #000000;
    }}
    .compare-table td {{
      padding: 3.8px 7px;
      border-bottom: 1px solid #DDDDDD;
      line-height: 1.2;
      vertical-align: middle;
    }}
    .compare-table tr:last-child td {{
      border-bottom: none;
    }}
    .compare-table td.bad {{
      color: #333333;
      background: #FAFAFA;
    }}
    .compare-table td.good {{
      font-weight: 700;
      color: #000000;
      background: #FFFFFF;
    }}
    .compare-table td.good-invert {{
      background: #000000;
      color: #FFFFFF;
      font-weight: 700;
    }}

    /* PITCH SEM PITCH */
    .pitch-synthesis {{
      border: 2.5px solid #000000;
      padding: 7px 10px;
      background: #000000;
      color: #FFFFFF;
      display: grid;
      grid-template-columns: auto 1fr;
      gap: 12px;
      align-items: center;
      margin-top: 3px;
    }}
    .pitch-synthesis .tag-big {{
      font-family: 'Big Shoulders Display', sans-serif;
      font-weight: 900;
      font-size: 24px;
      line-height: 0.88;
      text-align: center;
      border-right: 2px solid #FFFFFF;
      padding-right: 10px;
    }}
    .pitch-synthesis p {{
      font-size: 8.8px;
      line-height: 1.35;
    }}

    /* FOOTER */
    .footer-bauhaus {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 2px solid #000000;
      padding-top: 4px;
      margin-top: 3px;
      font-family: 'Staatliches', sans-serif;
      font-size: 8px;
      letter-spacing: 0.8px;
    }}
  </style>
</head>
<body>

  <div class="page">
    <!-- HEADER -->
    <div class="header-bauhaus">
      <div class="header-logo-box">
        <img src="{b64_logo}" alt="Cisne Engelke">
      </div>
      <div class="header-title-block">
        <div class="header-eyebrow">BLUEPRINT TÉCNICO • ARQUITETURA DE DADOS</div>
        <div class="header-title">BROTHAUS ENGELKE // MECÂNICA DO SISTEMA</div>
        <div class="header-sub">COMO O SITE E O BACKEND FUNCIONAM NA PRÁTICA • RIO TAVARES</div>
      </div>
      <div class="header-badge-solid">
        <div class="top">R$ 0,00 / MÊS</div>
        <div class="sub">ZERO RECORRÊNCIA</div>
      </div>
    </div>

    <div class="page-inner">
      <!-- 1. MANIFESTO / TÍTULO -->
      <div class="title-banner">
        <div class="title-left">
          <h1>ARQUITETURA DIRETA.<br>ZERO INTERMEDIÁRIOS.</h1>
          <p>
            Não usamos plataformas genéricas com dezenas de mensalidades ocultas. O sistema foi construído como um mecanismo de precisão: conecta o cliente da Servidão Elpídio da Rocha diretamente ao forno da padaria via WhatsApp, sem taxas de app e sem servidor pago.
          </p>
        </div>
        <div class="title-metrics">
          <div class="metric-box">
            <div class="metric-val">&lt; 0.8S</div>
            <div class="metric-lbl">Abertura Imediata no Celular</div>
          </div>
          <div class="metric-box">
            <div class="metric-val">0%</div>
            <div class="metric-lbl">Comissão de Vendas (vs 27% iFood)</div>
          </div>
          <div class="metric-box">
            <div class="metric-val">R$ 0</div>
            <div class="metric-lbl">Mensalidade de Servidor ou Nuvem</div>
          </div>
          <div class="metric-box">
            <div class="metric-val">100%</div>
            <div class="metric-lbl">Controle Direto no seu WhatsApp</div>
          </div>
        </div>
      </div>

      <!-- 2. O FLUXO MECÂNICO EM 4 MÓDULOS -->
      <div>
        <div class="blueprint-header">
          <h2>DIAGRAMA EM 4 TEMPOS: DA VISITA DO CLIENTE AO PÃO EMBALADO</h2>
          <span>FLUXO OPERACIONAL CONTÍNUO</span>
        </div>

        <div class="flow-grid">
          <!-- MÓDULO 01 -->
          <div class="flow-card">
            <div class="flow-card-header">
              <div class="flow-step-num">01</div>
              <div class="flow-step-tag">O CLIENTE NA BIO</div>
            </div>
            <div class="flow-card-title">Vitrine Digital de Alta Velocidade</div>
            <p class="flow-card-body">
              O cliente clica no link do Instagram ou escaneia o QR Code físico no balcão. O site abre instantaneamente.
            </p>
            <ul class="flow-card-bullets">
              <li><strong>Monograma 3D:</strong> O cisne EvS gira interativo na tela do celular sem travamento.</li>
              <li><strong>História & Tradição:</strong> Grãos Demeter, fermentação de 36h e a Sachertorte explicados.</li>
              <li><strong>Fornadas Vivas:</strong> Mostra o que está assando hoje e o que ainda dá tempo de reservar.</li>
            </ul>
          </div>

          <!-- MÓDULO 02 -->
          <div class="flow-card dark">
            <div class="flow-card-header">
              <div class="flow-step-num">02</div>
              <div class="flow-step-tag">O FECHAMENTO</div>
            </div>
            <div class="flow-card-title">Pedido Formatado no WhatsApp</div>
            <p class="flow-card-body">
              O cliente escolhe o pão e toca em "Reservar". Nada de formulários chatos ou senhas para cadastrar.
            </p>
            <ul class="flow-card-bullets">
              <li><strong>Mensagem Pronta:</strong> Abre o WhatsApp oficial já com o nome do produto e data escolhidos.</li>
              <li><strong>Zero Intermediários:</strong> A conversa e o pagamento caem direto na mão do Gustavo e da Engelke.</li>
              <li><strong>R$ 0 de Comissão:</strong> Toda a margem de venda fica 100% com a padaria.</li>
            </ul>
          </div>

          <!-- MÓDULO 03 -->
          <div class="flow-card dark">
            <div class="flow-card-header">
              <div class="flow-step-num">03</div>
              <div class="flow-step-tag">A OPERAÇÃO NO FORNO</div>
            </div>
            <div class="flow-card-title">Painel Móvel do Padeiro (PWA)</div>
            <p class="flow-card-body">
              Um aplicativo simples no próprio celular da padaria, protegido por PIN de segurança (1832).
            </p>
            <ul class="flow-card-bullets">
              <li><strong>3 Toques no Forno:</strong> Alterne o status entre "Em Fermentação", "No Forno" ou "Esgotado".</li>
              <li><strong>Planilha Opcional:</strong> Se preferir, altere direto na sua planilha do Google Drive.</li>
              <li><strong>Stories com 1 Clique:</strong> Gera a imagem da fornada já na medida certa do Instagram.</li>
            </ul>
          </div>

          <!-- MÓDULO 04 -->
          <div class="flow-card">
            <div class="flow-card-header">
              <div class="flow-step-num">04</div>
              <div class="flow-step-tag">O MOTOR INVISÍVEL</div>
            </div>
            <div class="flow-card-title">Backend Perpétuo & Nuvem Gratuita</div>
            <p class="flow-card-body">
              A inteligência que mantém o sistema funcionando 24h por dia sem nunca enviar fatura de hospedagem.
            </p>
            <ul class="flow-card-bullets">
              <li><strong>Google Sheets + Apps Script:</strong> Funciona como banco de dados e API seguro e gratuito vitalício.</li>
              <li><strong>Vercel Edge Network:</strong> Servidores globais de alta velocidade com certificado SSL HTTPS blindado.</li>
              <li><strong>Código Sob Medida:</strong> Sem WordPress ou plugins que quebram com atualizações.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- 3. TABELA COMPARATIVA DE ENGENHARIA -->
      <div class="compare-section">
        <div class="compare-title">
          <h3>TABELA DE ENGENHARIA: ARQUITETURA SOB MEDIDA VS. SISTEMAS DE MERCADO</h3>
          <span>COMPARATIVO OBJETIVO</span>
        </div>
        <table class="compare-table">
          <thead>
            <tr>
              <th style="width: 28%;">Critério Operacional</th>
              <th style="width: 36%;">Sites Convencionais (WordPress / Agências)</th>
              <th style="width: 36%;">Arquitetura Sob Medida Brothaus (Nossa Solução)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Custo Mensal de Infraestrutura</strong></td>
              <td class="bad">R$ 150 a R$ 450/mês (hospedagem + plugins em dólar)</td>
              <td class="good-invert">R$ 0,00 por mês (Google Cloud + Vercel Edge perpétuos)</td>
            </tr>
            <tr>
              <td><strong>Taxa por Pedido / Venda</strong></td>
              <td class="bad">12% a 27% em plataformas de entrega e marketplaces</td>
              <td class="good">0% de taxa (conversão direta no seu próprio WhatsApp)</td>
            </tr>
            <tr>
              <td><strong>Tempo de Carregamento</strong></td>
              <td class="bad">4 a 9 segundos (pesado, perde até 40% dos visitantes)</td>
              <td class="good">&lt; 0.8 segundo (código puro, abre no piscar de olhos)</td>
            </tr>
            <tr>
              <td><strong>Atualização do Cardápio</strong></td>
              <td class="bad">Painel complexo de computador que o padeiro nunca abre</td>
              <td class="good">No celular em 3 toques com PIN ou direto na planilha</td>
            </tr>
            <tr>
              <td><strong>Segurança & Manutenção</strong></td>
              <td class="bad">Quebra com atualizações de plugins; risco de vírus</td>
              <td class="good">Sem banco exposto; blindagem estática e SSL perpétuo</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- 4. PITCH SEM PITCH (SÍNTESE FINAL) -->
      <div class="pitch-synthesis">
        <div class="tag-big">
          POR QUE<br>ISSO<br>FUNCIONA?
        </div>
        <div>
          <p>
            <strong>A padaria não precisa de complexidade de TI; precisa de pão saindo do forno e cliente retirando no balcão.</strong>
            Eliminamos todo o intermediário técnico que só serve para cobrar mensalidade. O resultado é um site bonito, rápido e que pertence 100% à Brothaus. Você investe uma única vez na montagem e nunca mais recebe boleto de manutenção.
          </p>
        </div>
      </div>
    </div>

    <!-- FOOTER -->
    <div class="footer-bauhaus">
      <div>BROTHAUS ENGELKE • ARQUITETURA DE SISTEMAS SOB MEDIDA • SERVIDÃO ELPÍDIO DA ROCHA, 105 • RIO TAVARES</div>
      <div>CARLOS LINZMEYER // ENGENHARIA DE SOFTWARE LOCAL</div>
    </div>
  </div>

</body>
</html>
"""

html_path = os.path.join(BASE_DIR, "esquema_tecnico_brothaus_pb.html")
pdf_path = os.path.join(BASE_DIR, "esquema_tecnico_brothaus_pb.pdf")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"[OK] Arquivo HTML do Esquema Tecnico gerado com acentos: {html_path}")

edge_candidates = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "msedge"
]
edge_bin = None
for c in edge_candidates:
    if os.path.exists(c) or c == "msedge":
        edge_bin = c
        break

cmd = [
    edge_bin,
    "--headless",
    "--disable-gpu",
    "--run-all-compositor-stages-before-draw",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    html_path
]
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0:
    print(f"[OK] PDF Esquema Tecnico compilado com sucesso! ({os.path.getsize(pdf_path)/1024:.1f} KB)")

try:
    import pypdfium2 as pdfium
    pdf = pdfium.PdfDocument(pdf_path)
    page = pdf[0]
    bitmap = page.render(scale=2.0)
    pil_image = bitmap.to_pil()
    preview_path = os.path.join(BASE_DIR, "preview_esquema_tecnico_pb.png")
    pil_image.save(preview_path)
    print(f"[OK] Preview salvo com sucesso: {preview_path}")
except Exception as e:
    print(f"[!] Erro ao gerar preview: {e}")
