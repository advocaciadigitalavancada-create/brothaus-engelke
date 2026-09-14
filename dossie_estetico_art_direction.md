# 🦢 Dossiê de Direção de Arte & Arquitetura Tipográfica
## Brothaus Engelke — Transposição Estética dos 3 Elementos Reais
**Data:** Setembro de 2026  
**Diretor de Arte & Tipógrafo Responsável:** Art Director & Typographic Architect da Brothaus Engelke  
**Origem dos Ativos de Campo:** Servidão Elpídio da Rocha, Rio Tavares Central, Florianópolis - SC  

---

### Sumário Executivo & Filosofia do Design
A Brothaus Engelke não é uma padaria convencional; é um refúgio da alta panificação de raiz germânica e austro-húngara com certificação biodinâmica **Demeter (SPG/OPAC ABDSul)**. 

A partir da análise dos três novos documentos físicos e materiais enviados pelo mestre — **(1)** o cardápio com costura artesanal em linha vermelha, papel pólen cru e selo tipográfico; **(2)** a fotografia da fornada de pães com cortes diagonais rítmicos e farinha viva; e **(3)** o totem de latão esculpido em haste contínua de cisne —, este dossiê estabelece a gramática visual definitiva para a interface digital da Brothaus.

Aqui, a tecnologia é intencionalmente invisível. O design segue o rigor da escola de Ulm e da Bauhaus: **forma segue a função, honestidade intransigente com os materiais e reverência ao tempo artesanal.**

---

## 1. O Detalhe da Costura em Linha Vermelha Artesanal (#C83E36 / #D63D33)

### 1.1. Análise Material do Objeto Físico
No cardápio impresso (`cardapio_engelke_costura.png`), a encadernação não é grampeada com metal industrial nem colada com adesivo sintético. Ela é **costurada à mão** através de furos manuais no papel pólen cru, unida por um fio de algodão/linho encerado em tom vermelho carmim/coral vibrante (`#C83E36` / `#D63D33`). O nó e o laço superior ficam aparentes na lombada esquerda, revelando o gesto do artífice.

```
 [ Papel Pólen Cru #F7F5F0 ]
   |
   |-- (o)  <- Furo manual
   |    |
   |    S   <- Ponto de alfaiataria em linha vermelha viva (#C83E36)
   |    |
   |-- (o)
   |    |
   |    S
   |    |
   |-- (o)
```

### 1.2. Regras de Transposição para o Digital (Sem Skeuomorfismo Vulgar)
Para transpor este detalhe à web moderna sem cair no erro do skeuomorfismo datado (falsas texturas 3D de couro e linha):
1. **Hairline Stitching (Bordas de Alfaiataria):** O ponto de costura vira uma linha pontilhada ou tracejada cirúrgica (`stroke-dasharray` ou `repeating-linear-gradient`) de espessura de 1.5px a 2px com espaçamento rítmico de 6px a 8px.
2. **O Ponto de Arremate (Tailor's Knot):** Um micro-nó ou loop gráfico no topo da gaveta do cardápio (`menu-drawer`) ou na lombada vertical de cartões de destaque.
3. **Micro-Acentos Cromáticos:** O vermelho coral (`#C83E36`) é utilizado com extrema parcimônia e parcimônia aristocrática — ele nunca pinta botões inteiros (que permanecem no preto carvão mineral `#1A1816`), mas sim os pontos de tensão: traços de arremate, bullets de fornadas pontuais, números de série e pequenos nós decorativos.

### 1.3. Especificações Técnicas de CSS

```css
/* ==========================================================================
   COSTURA ARTESANAL EM LINHA VERMELHA (SADDLE STITCHING SYSTEM)
   Paleta: #D63D33 (Coral Iluminado) / #C83E36 (Vermelho Carmim Fio Cru)
   ========================================================================== */

:root {
  --stitch-red: #C83E36;
  --stitch-red-bright: #D63D33;
  --stitch-red-subtle: rgba(200, 62, 54, 0.12);
  --paper-polen: #F7F5F0;
  --paper-polen-deep: #ECE8DE;
}

/* 1. Lombada Costurada Vertical (Aplicada no Menu Drawer ou Cartão de Assinatura) */
.hand-stitched-spine {
  position: relative;
  padding-left: 2rem;
  border-left: 1px solid var(--border-hairline);
}

.hand-stitched-spine::before {
  content: "";
  position: absolute;
  top: 1.5rem;
  bottom: 1.5rem;
  left: 6px;
  width: 2px;
  background-image: repeating-linear-gradient(
    to bottom,
    var(--stitch-red) 0px,
    var(--stitch-red) 8px,
    transparent 8px,
    transparent 14px
  );
  box-shadow: 0 0 1px rgba(200, 62, 54, 0.35);
}

/* O Micro-Nó da Costura (Arremate Superior em Loop) */
.hand-stitched-spine::after {
  content: "";
  position: absolute;
  top: 1rem;
  left: 4px;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background-color: var(--stitch-red);
  box-shadow: 
    0 0 0 2px var(--paper-polen),
    0 1px 3px rgba(200, 62, 54, 0.4);
}

/* 2. Marcador Horizontal de Alfaiataria (Divisor de Seções no Cardápio) */
.stitch-divider {
  position: relative;
  width: 100%;
  height: 1px;
  margin: 2.5rem 0;
  background-image: repeating-linear-gradient(
    to right,
    var(--stitch-red) 0px,
    var(--stitch-red) 6px,
    transparent 6px,
    transparent 12px
  );
  opacity: 0.85;
}

.stitch-divider::after {
  content: "✦";
  position: absolute;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  font-size: 8px;
  color: var(--stitch-red);
  background: var(--bg-paper);
  padding-left: 6px;
}

/* 3. Etiqueta / Pill de Fornada com Arremate em Fio */
.stitch-tag {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-mono);
  font-size: 0.65rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--stitch-red);
  background: rgba(200, 62, 54, 0.06);
  padding: 0.3rem 0.75rem;
  border: 1px dashed var(--stitch-red);
  border-radius: 2px;
}

.stitch-tag-dot {
  width: 5px;
  height: 5px;
  background: var(--stitch-red);
  border-radius: 50%;
  display: inline-block;
}
```

---

## 2. A Recriação do Selo do Cardápio em SVG e CSS Puro

### 2.1. Anatomia do Selo Original (`cardapio_engelke_costura.png`)
O selo da capa do cardápio físico é uma aula de tipografia modernista centro-europeia:
1. **A Moldura Retangular Aberta:** Uma caixa retangular com traço hairline preto puro (`#1A1816`). A aresta superior é interrompida por um intervalo aberto centralizado.
2. **O Encaixe "Pães e Cia.":** No vão superior aberto, o texto `"Pães e Cia."` é posicionado com precisão matemática, servindo de fecho da caixa. A tipografia é uma sem-serifa elegante, equilibrada e com kerning generoso.
3. **O Monumento "ENGELKE":** O núcleo da moldura contém a palavra `ENGELKE` em corpo robusto e condensado (proporções de caracteres esguios estilo DIN 1451 Mittelschrift / Alternate Gothic / Grotesk Condensada), respirando com respiro lateral e vertical generoso.
4. **O Subtítulo Inferior:** Abaixo da moldura fechada na base:
   - `Produtos Artesanais`
   - `+` (com respiro vertical e peso idêntico)
   - `Ingredientes Orgânicos`

### 2.2. Implementação Técnica 1: Componente SVG Vetorial Cirúrgico
Este componente SVG é perfeitamente escalável, responsivo e preserva as proporções e espessuras exatas da impressão em papel pólen:

```xml
<svg class="engelke-menu-seal" viewBox="0 0 320 220" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Selo Oficial Brothaus Engelke">
  <style>
    .seal-border { stroke: #1A1816; stroke-width: 1.5; fill: none; stroke-linecap: square; }
    .seal-text-top { font-family: 'Plus Jakarta Sans', 'Helvetica Neue', sans-serif; font-size: 13.5px; font-weight: 500; fill: #1A1816; letter-spacing: 0.08em; text-anchor: middle; }
    .seal-text-main { font-family: 'League Gothic', 'Oswald', 'Bebas Neue', 'Plus Jakarta Sans', sans-serif; font-size: 44px; font-weight: 700; fill: #1A1816; letter-spacing: 0.16em; text-anchor: middle; text-transform: uppercase; }
    .seal-subtext { font-family: 'Plus Jakarta Sans', 'Inter', sans-serif; font-size: 12px; font-weight: 500; fill: #1A1816; letter-spacing: 0.05em; text-anchor: middle; }
    .seal-plus { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 12px; font-weight: 600; fill: #C83E36; text-anchor: middle; }
  </style>

  <!-- Retângulo com Topo Aberto: Coordenadas precisas
       Box: X=40 a 280 (largura 240), Y=25 a 125 (altura 100)
       Vão Superior: X=105 a 215 (largura 110) para alojar "Pães e Cia." -->
  
  <!-- Linha Superior Esquerda: de (40, 25) até (105, 25) -->
  <line x1="40" y1="25" x2="105" y2="25" class="seal-border" />
  
  <!-- Linha Superior Direita: de (215, 25) até (280, 25) -->
  <line x1="215" y1="25" x2="280" y2="25" class="seal-border" />
  
  <!-- Lateral Esquerda: de (40, 25) até (40, 125) -->
  <line x1="40" y1="25" x2="40" y2="125" class="seal-border" />
  
  <!-- Lateral Direita: de (280, 25) até (280, 125) -->
  <line x1="280" y1="25" x2="280" y2="125" class="seal-border" />
  
  <!-- Base Inferior: de (40, 125) até (280, 125) -->
  <line x1="40" y1="125" x2="280" y2="125" class="seal-border" />

  <!-- Texto Topo no Vão: "Pães e Cia." -->
  <text x="160" y="29.5" class="seal-text-top">Pães e Cia.</text>

  <!-- Núcleo Central: "ENGELKE" -->
  <text x="160" y="87" class="seal-text-main">ENGELKE</text>

  <!-- Bloco Inferior: Produtos Artesanais + Ingredientes Orgânicos -->
  <text x="160" y="162" class="seal-subtext">Produtos Artesanais</text>
  <text x="160" y="180" class="seal-plus">+</text>
  <text x="160" y="198" class="seal-subtext">Ingredientes Orgânicos</text>
</svg>
```

### 2.3. Implementação Técnica 2: Recriação em CSS Puro & HTML Semântico
Esta alternativa permite que o selo seja renderizado de forma nativa e indexável pelo Google:

```html
<div class="engelke-seal-box">
  <div class="seal-frame">
    <div class="seal-head-slot">
      <span class="seal-badge-label">Pães e Cia.</span>
    </div>
    <h1 class="seal-brand-title">ENGELKE</h1>
  </div>
  <div class="seal-footer-manifesto">
    <span class="manifesto-line">Produtos Artesanais</span>
    <span class="manifesto-plus">+</span>
    <span class="manifesto-line">Ingredientes Orgânicos</span>
  </div>
</div>
```

```css
/* Estilização do Selo em CSS Puro */
.engelke-seal-box {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  background-color: var(--bg-paper);
  padding: 2.5rem 2rem;
  max-width: 320px;
  text-align: center;
  box-sizing: border-box;
}

.seal-frame {
  position: relative;
  width: 100%;
  padding: 2.25rem 1.5rem 1.85rem 1.5rem;
  border: 1.5px solid var(--ink-primary);
  border-top: none; /* O topo é desenhado pelos pseudo-elementos com vão */
  box-sizing: border-box;
}

/* Criando o topo aberto com o vão de 120px */
.seal-frame::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: calc(50% - 60px);
  height: 1.5px;
  background: var(--ink-primary);
}

.seal-frame::after {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  width: calc(50% - 60px);
  height: 1.5px;
  background: var(--ink-primary);
}

.seal-head-slot {
  position: absolute;
  top: -10px;
  left: 50%;
  transform: translateX(-50%);
  background-color: var(--bg-paper);
  padding: 0 10px;
  white-space: nowrap;
}

.seal-badge-label {
  font-family: var(--font-sans);
  font-size: 0.82rem;
  font-weight: 500;
  color: var(--ink-primary);
  letter-spacing: 0.08em;
}

.seal-brand-title {
  font-family: 'Oswald', 'Bebas Neue', 'Plus Jakarta Sans', sans-serif;
  font-size: 2.8rem;
  font-weight: 700;
  color: var(--ink-primary);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  margin: 0;
  line-height: 1;
}

.seal-footer-manifesto {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.2rem;
  margin-top: 1.5rem;
}

.manifesto-line {
  font-family: var(--font-sans);
  font-size: 0.78rem;
  font-weight: 500;
  color: var(--ink-primary);
  letter-spacing: 0.04em;
}

.manifesto-plus {
  font-family: var(--font-sans);
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--stitch-red);
  line-height: 1.2;
}
```

---

## 3. Direção de Arte da Nova Foto: Fornada de Pães (`fornada_baguetes_linhas.png`)

### 3.1. Análise da Fotografia
- **As Lâminas Diagonais (Grignes):** Os pães revelam incisões rítmicas com angulação uniforme de ~35° a 42°. Cada corte se abriu em forno de pedra com expansão de miolo ("orelha" do pão), gerando sombras profundas e texturas estaladiças.
- **A Farinha Viva:** A farinha crua de centeio e trigo integral repousa nos vales da massa, criando um relevo topográfico branco sobre o âmbar profundo.
- **A Grelha Perfurada:** A base de metal perfurada industrial conecta o artesanato à oficina da padaria — não há cenografia falsa; é a fornada real na saída imediata do forno.

### 3.2. Curadoria & Enquadramento na Interface
1. **Seção "O Ritmo do Forno & As Lâminas do Mestre":** A imagem substitui qualquer ilustração genérica de stock photo. Ela é o testemunho fotográfico inquestionável de que os pães são produzidos no local, todos os dias.
2. **Efeito Parallax Suave com Lenis:** Durante a rolagem, a imagem desliza em velocidade ligeiramente inferior (fator 0.95), criando profundidade táctil.
3. **Overlays HUD de Precisão em Hairline:** Sobre a imagem, pequenas marcações tipográficas em `Space Mono` identificam os parâmetros de fornada:

```
+-------------------------------------------------------------+
| [ FORNADA Nº 0842 ]                    [ TEMP. LASTRO: 245°C ]
|                                                             |
|          /// CORTE RÍTMICO DE LÂMINA A 42° ///              |
|                                                             |
| [ LEVAIN SELVAGEM 36H ]          [ CERTIFICAÇÃO DEMETER SPG ]
+-------------------------------------------------------------+
```

### 3.3. Código CSS de Tratamento de Imagem (Grading Natural)

```css
/* Card Fotográfico da Fornada com Tratamento Editorial */
.fornada-art-frame {
  position: relative;
  background-color: #E6E2D8;
  border: 1px solid var(--border-hairline);
  padding: 1.25rem;
  box-shadow: 0 20px 48px rgba(26, 24, 22, 0.08);
}

.fornada-art-frame .image-container {
  position: relative;
  overflow: hidden;
  height: 480px;
  background-color: #1A1816;
}

.fornada-art-frame img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 40%;
  /* Grading Térmico Mineral: Realça a farinha sem estourar as altas luzes */
  filter: contrast(1.05) brightness(0.98) saturate(1.08);
  transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

.fornada-art-frame:hover img {
  transform: scale(1.025);
}

/* Grid de Informações Técnicas da Fornada */
.fornada-telemetry-badge {
  position: absolute;
  bottom: 1.5rem;
  left: 1.5rem;
  right: 1.5rem;
  background: rgba(247, 245, 240, 0.92);
  backdrop-filter: blur(12px);
  border: 1px solid var(--border-hairline);
  padding: 1rem 1.25rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.telemetry-item {
  display: flex;
  flex-direction: column;
}

.telemetry-kicker {
  font-family: var(--font-mono);
  font-size: 0.62rem;
  letter-spacing: 0.14em;
  color: var(--ink-tertiary);
  text-transform: uppercase;
}

.telemetry-value {
  font-family: var(--font-sans);
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--ink-primary);
  margin-top: 2px;
}
```

---

## 4. O Totem do Cisne em Latão: A Linha Contínua Dobrada (`totem_cisne_detalhe.png`)

### 4.1. Análise da Serralheria Artística
O totem real da fachada não é um desenho plano recortado a laser computadorizado. É uma **haste contínua de latão dourado cilíndrico, dobrada manualmente**:
1. O anel externo em latão abriga a escultura.
2. A haste nasce na base, sobe descrevendo a espinha do pescoço em curva contínua, curva o bico pontiagudo em direção ao peito, desce e desdobra-se em duas ondas horizontais contínuas que formam o corpo e simultaneamente o `E` cursivo de Engelke.
3. Três pequenos pinos de solda conectam o cisne ao aro, mantendo a sensação de suspensão no ar.

### 4.2. Otimização do Vetor SVG
O ícone do cisne no cabeçalho e nos selos da interface deve espelhar essa caligrafia metálica contínua, com espessura uniforme (`stroke-width: 2.2px`) e terminações arredondadas (`stroke-linecap: round`), remetendo ao tubo de latão maciço.

---

## 5. O Tom de Voz Editorial Vienense & Demeter

### 5.1. Pilares da Retórica Engelke
- **Antitrombeteiro (Anti-Hype):** Jamais use exclamações vazias, contadores de escassez falsos ("Últimas unidades! Compre agora!") ou termos como "o melhor", "imperdível", "delicioso". A excelência austríaca não pede atenção; ela é evidente.
- **Respeito aos Elementos:** Referencie farinha biodinâmica, grãos com pedigree ecológico, sal marinho não refinado, fermentação biológica e respeito às estações.
- **A Casa do Pão (Brothaus):** A Brothaus é tratada como um ateliê de ofício ancestral no coração do Rio Tavares, onde Gustavo e Engelke cultivam o diálogo comunitário.

### 5.2. Textos Prontos para a Interface

#### [HERO SECTION]
> **Kicker:** Brothaus Engelke • Rio Tavares Central  
> **Título:** A Lâmina, o Tempo e o Grão Vivo.  
> **Parágrafo:**  
> *"Nossos pães não conhecem aditivos, aceleradores ou atalhos químicos. Apenas farinhas biodinâmicas com certificação Demeter, água mineral, sal marinho e o silêncio de 36 horas de fermentação natural. Quando a crosta canta ao sair do forno de pedra, o tempo cumpriu seu ofício."*

#### [CRONOGRAMA DE FORNADAS]
> **Kicker:** Disciplina Semanal  
> **Título:** O Ritmo da Nossa Fornalha  
> **Parágrafo:**  
> *"Cada fornada exige dois dias inteiros de cuidado com o levain e modelagem manual. Por isso, nossos pães e doces são assados em momentos pontuais da semana. Recomendamos reservar antecipadamente pelo WhatsApp para retirar ainda aquecidos da pedra."*

#### [A SACHERTORE IMPERIAL]
> **Kicker:** Tradição Austríaca de 1832  
> **Título:** Sachertorte: O Clássico de Metternich  
> **Parágrafo:**  
> *"Preparada com cacau nobre a 70%, massa densa e entremeada por compota artesanal de damascos frescos cozidos lentamente em panela de cobre. Finalizada com uma ganache espelhada pura, sem açúcares excessivos. A mesma receita que encantou a corte de Viena no século XIX, servida no Rio Tavares."*

#### [CERTIFICAÇÃO DEMETER & ABDSUL]
> **Kicker:** SPG/OPAC ABDSul  
> **Título:** Agricultura que Regenera o Solo  
> **Parágrafo:**  
> *"Não chamamos nossos ingredientes de orgânicos por mero modismo de rótulo. A certificação biodinâmica Demeter garante que cada espiga de trigo e centeio foi cultivada em consonância com a vitalidade cósmica e biológica da terra, sem qualquer veneno sintético."*

---

## 6. Matriz Cromática e Tipográfica Definitiva

| Elemento | Código Hex | Papel na Composição |
| :--- | :--- | :--- |
| **Papel Pólen Cru** | `#F7F5F0` | Fundo principal da página, sem ofuscamento branco |
| **Pólen Sombra / Linho** | `#EFECE4` | Superfície secundária de cartões e gavetas |
| **Tinta Carvão Mineral** | `#1A1816` | Tipografia mestra e linhas de hairline |
| **Linha de Costura Vermelha** | `#C83E36` / `#D63D33` | Arremates de alfaiataria, nós e micro-pontos |
| **Ouro Latão Forjado** | `#9E7A3E` | Haste do Cisne Totem e kicker badges |
| **Verde Folha Demeter** | `#334436` | Pílulas de certificação biodinâmica e sanidade |
| **Crosta Dourada Maillard** | `#C89B58` / `#8C5B28` | Acentos táteis e tons terrosos |

**A Tríade Tipográfica de Ouro Definitiva (Escola Bauhaus & Editorial Vienense):**
1. **Eixo Editorial & Literário:** `Playfair Display` (Rigor e nobreza da alta confeitaria vienense de 1832; títulos display monumentais, citações e manifestos com `lining-nums`).
2. **Eixo Arquitetônico & Identitário:** `Oswald` (A grotesca condensada austera do cardápio físico real da Engelke; kickers estruturais e chapéus de seção).
3. **Eixo Funcional & Micro-Engenharia Suíça:** `Plus Jakarta Sans` (Clareza tipográfica contemporânea para corpo de texto, navegação, botões e micro-etiquetas técnicas com tracking generoso, eliminando fontes de terminal).

---
*Dossiê concluído e harmonizado com os cânones de Tschichold e Müller-Brockmann.*
