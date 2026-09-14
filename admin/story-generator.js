/**
 * ============================================================================
 * BROTHAUS ENGELKE • GERADOR DE STORIES PARA INSTAGRAM (CANVAS 1080x1920)
 * ============================================================================
 * 
 * Gera instantaneamente uma imagem de alta resolução (1080x1920 px, 9:16)
 * com as fontes oficiais (Playfair Display, Oswald, Plus Jakarta Sans),
 * paleta institucional (Carvão, Latão, Farinha Crua, Verde Demeter e Costura Vermelha)
 * e o totem do Cisne Dourado para postar nos Stories do Instagram.
 */

window.EngelkeStoryGenerator = (function() {
  const CANVAS_WIDTH = 1080;
  const CANVAS_HEIGHT = 1920;

  /**
   * Gera o canvas com a arte do Story
   * @param {Object} state - Estado atual contendo { config, cronograma }
   * @returns {Promise<HTMLCanvasElement>}
   */
  async function gerarCanvasStory(state) {
    // 1. Aguarda as fontes web carregarem completamente
    if (document.fonts && document.fonts.ready) {
      await document.fonts.ready;
    }

    const canvas = document.createElement('canvas');
    canvas.width = CANVAS_WIDTH;
    canvas.height = CANVAS_HEIGHT;
    const ctx = canvas.getContext('2d');

    // Ativa máxima qualidade de renderização de imagem e texto
    ctx.imageSmoothingEnabled = true;
    ctx.imageSmoothingQuality = 'high';

    // 2. Fundo: Carvão Mineral Nobre com Gradiente Quente Central
    const bgGrad = ctx.createRadialGradient(
      CANVAS_WIDTH / 2, 750, 80,
      CANVAS_WIDTH / 2, 960, 1100
    );
    bgGrad.addColorStop(0, '#231D18'); // Brilho quente sutil no centro
    bgGrad.addColorStop(0.55, '#161311'); // Carvão institucional
    bgGrad.addColorStop(1, '#0F0D0C'); // Borda mais profunda
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);

    // 3. Grid Suíço Arquitetônico de Fundo (Linhas ultra-discretas)
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.025)';
    ctx.lineWidth = 1;
    const gridSize = 90;
    for (let x = gridSize; x < CANVAS_WIDTH; x += gridSize) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, CANVAS_HEIGHT);
      ctx.stroke();
    }
    for (let y = gridSize; y < CANVAS_HEIGHT; y += gridSize) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(CANVAS_WIDTH, y);
      ctx.stroke();
    }

    // 4. Moldura Dupla de Latão Polido & Cantos Bauhaus
    const mOut = 55;
    const mIn = 72;
    
    // Borda Externa
    ctx.strokeStyle = 'rgba(200, 155, 88, 0.4)';
    ctx.lineWidth = 2;
    ctx.strokeRect(mOut, mOut, CANVAS_WIDTH - mOut * 2, CANVAS_HEIGHT - mOut * 2);

    // Borda Interna Fina
    ctx.strokeStyle = 'rgba(200, 155, 88, 0.18)';
    ctx.lineWidth = 1;
    ctx.strokeRect(mIn, mIn, CANVAS_WIDTH - mIn * 2, CANVAS_HEIGHT - mIn * 2);

    // Cantos Arquitetônicos de Latão
    desenharCantosLatão(ctx, mIn, CANVAS_WIDTH - mIn, mIn, CANVAS_HEIGHT - mIn);

    // 5. Cabeçalho Superior: Kicker & Totem do Cisne
    let curY = 155;

    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    // Kicker Superior
    ctx.font = '600 20px "Plus Jakarta Sans", sans-serif';
    ctx.fillStyle = '#C89B58';
    ctx.fillText('• BROTHAUS ENGELKE • RIO TAVARES CENTRAL •', CANVAS_WIDTH / 2, curY);

    curY += 60;

    // Totem do Cisne Dourado em Vetor Puro (sem caixa cinza de fundo)
    const totemRadius = 70;
    desenharTotemCisneVetorial(ctx, CANVAS_WIDTH / 2, curY + totemRadius, totemRadius);
    curY += totemRadius * 2 + 35;

    // Título Principal da Marca
    ctx.font = '700 58px "Oswald", sans-serif';
    ctx.fillStyle = '#FFFFFF';
    ctx.fillText('BROTHAUS ENGELKE', CANVAS_WIDTH / 2, curY);

    curY += 42;

    // Subtítulo
    ctx.font = '500 21px "Plus Jakarta Sans", sans-serif';
    ctx.fillStyle = '#A8A196';
    ctx.fillText('BOUTIQUE DE PÃES VIVOS & CONFEITARIA AUST RÍACA • DESDE 2013', CANVAS_WIDTH / 2, curY);

    curY += 75;

    // 6. Badge de Status da Fornada (Pill Dinâmico)
    const statusForno = (state.config && state.config.status_forno) || 'saindo_agora';
    curY = desenharBadgeStatus(ctx, statusForno, curY);

    curY += 50;

    // 7. Cartão Arquitetônico Central (A Fornada & Pães)
    const cardWidth = CANVAS_WIDTH - 160; // 920px
    const cardX = (CANVAS_WIDTH - cardWidth) / 2; // 80px
    const cardTop = curY + 12;
    const cardHeight = 495;

    // Fundo do Card com sutil profundidade e textura nobre
    const cardGrad = ctx.createLinearGradient(cardX, cardTop, cardX, cardTop + cardHeight);
    cardGrad.addColorStop(0, 'rgba(28, 24, 20, 0.98)');
    cardGrad.addColorStop(1, 'rgba(17, 14, 12, 0.99)');
    ctx.fillStyle = cardGrad;
    desenharRetanguloArredondado(ctx, cardX, cardTop, cardWidth, cardHeight, 18);
    ctx.fill();

    // Borda do Card em Latão Nobre
    ctx.strokeStyle = 'rgba(200, 155, 88, 0.42)';
    ctx.lineWidth = 1.5;
    desenharRetanguloArredondado(ctx, cardX, cardTop, cardWidth, cardHeight, 18);
    ctx.stroke();

    // Borda interna tênue de respiro
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.035)';
    ctx.lineWidth = 1;
    desenharRetanguloArredondado(ctx, cardX + 6, cardTop + 6, cardWidth - 12, cardHeight - 12, 14);
    ctx.stroke();

    // Detalhe da Costura em Linha Vermelha Artesanal no Topo do Card
    ctx.save();
    ctx.strokeStyle = '#C83E36';
    ctx.lineWidth = 2.5;
    ctx.setLineDash([7, 6]);
    ctx.beginPath();
    ctx.moveTo(cardX + 28, cardTop + 14);
    ctx.lineTo(cardX + cardWidth - 28, cardTop + 14);
    ctx.stroke();
    ctx.restore();

    let insideY = cardTop + 48;

    // Kicker do Card (Caixa Alta Condensada com Tracking Generoso)
    ctx.font = '700 17px "Plus Jakarta Sans", sans-serif';
    ctx.fillStyle = '#C89B58';
    ctx.letterSpacing = '3px';
    ctx.fillText('OFÍCIO ANCESTRAL • LEVAIN SELVAGEM 36H', CANVAS_WIDTH / 2, insideY);
    ctx.letterSpacing = '0px';

    insideY += 50;

    // Título do Pão em Destaque (Playfair Display com Presença Imperial)
    const paoDestaque = (state.config && state.config.pao_destaque_hoje) || 'Sourdough Tradicional Demeter';
    ctx.font = '600 48px "Playfair Display", Georgia, serif';
    ctx.fillStyle = '#FFFFFF';
    insideY = quebrarTextoCentrado(ctx, paoDestaque, CANVAS_WIDTH / 2, insideY, cardWidth - 90, 54);

    // Respiro milimétrico após o título para nunca colidir com descendentes
    insideY += 38;

    // Filete de Latão com Losango Dourado Central
    desenharDivisorJoalheria(ctx, CANVAS_WIDTH / 2, insideY, 190);

    insideY += 34;

    // Mensagem da Fornada (Tratamento Literário e Poético)
    let alertaTexto = (state.config && state.config.alerta_texto) || 'Pães de fermentação lenta de 36 horas, crosta dourada e miolo aromático.';
    alertaTexto = alertaTexto.replace(/^🔥\s*/, '');
    
    ctx.font = 'italic 400 25px "Playfair Display", Georgia, serif';
    ctx.fillStyle = '#E8E2D8';
    insideY = quebrarTextoCentrado(ctx, `“${alertaTexto}”`, CANVAS_WIDTH / 2, insideY, cardWidth - 110, 36);

    insideY += 34;

    // Faixa Intermediária: Pilares de Pureza Artesanal (Estética Bauhaus & Escola Suíça)
    desenharFaixaPilaresPureza(ctx, CANVAS_WIDTH / 2, insideY, cardWidth - 80);

    // Cartuchos de Telemetria Suíça (3 Caixas Nobres na Base do Card)
    const boxMargin = 26;
    const boxGap = 14;
    const boxY = cardTop + cardHeight - 112;
    const boxH = 88;
    const totalBoxW = cardWidth - (boxMargin * 2);
    const itemW = (totalBoxW - (boxGap * 2)) / 3;

    desenharCartuchoTelemetria(ctx, cardX + boxMargin, boxY, itemW, boxH, 'FERMENTAÇÃO', '36h Levain');
    desenharCartuchoTelemetria(ctx, cardX + boxMargin + itemW + boxGap, boxY, itemW, boxH, 'CERTIFICAÇÃO', 'Demeter SPG');
    desenharCartuchoTelemetria(ctx, cardX + boxMargin + (itemW + boxGap) * 2, boxY, itemW, boxH, 'FORNO', 'Lastro Refratário');

    // 8. Seção de Horário & Próxima Fornada
    curY = cardTop + cardHeight + 46;

    const proxFornada = (state.config && state.config.proxima_fornada) || 'Hoje • Fornada Especial';
    ctx.font = '600 20px "Plus Jakarta Sans", sans-serif';
    ctx.fillStyle = '#C89B58';
    ctx.letterSpacing = '2.5px';
    ctx.fillText('CRONOGRAMA DO DIA', CANVAS_WIDTH / 2, curY);
    ctx.letterSpacing = '0px';

    curY += 40;

    ctx.font = '700 46px "Oswald", sans-serif';
    ctx.fillStyle = '#FFFFFF';
    ctx.fillText(proxFornada.toUpperCase(), CANVAS_WIDTH / 2, curY);

    curY += 66;

    // 9. Call To Action Principal (Botão Dourado de Reserva)
    const btnWidth = cardWidth;
    const btnHeight = 98;
    const btnX = (CANVAS_WIDTH - btnWidth) / 2;
    const btnY = curY;

    // Sombra do botão
    ctx.save();
    ctx.shadowColor = 'rgba(200, 155, 88, 0.42)';
    ctx.shadowBlur = 28;
    ctx.shadowOffsetY = 8;

    // Gradiente Dourado Latão Champanhe
    const btnGrad = ctx.createLinearGradient(btnX, btnY, btnX + btnWidth, btnY + btnHeight);
    btnGrad.addColorStop(0, '#E6C48B');
    btnGrad.addColorStop(0.5, '#C89B58');
    btnGrad.addColorStop(1, '#B07E35');
    ctx.fillStyle = btnGrad;
    desenharRetanguloArredondado(ctx, btnX, btnY, btnWidth, btnHeight, 18);
    ctx.fill();
    ctx.restore();

    // Borda superior sutil de brilho no botão
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.35)';
    ctx.lineWidth = 1;
    desenharRetanguloArredondado(ctx, btnX + 1, btnY + 1, btnWidth - 2, btnHeight - 2, 17);
    ctx.stroke();

    // Texto do Botão
    ctx.font = '700 30px "Oswald", sans-serif';
    ctx.fillStyle = '#14110E';
    ctx.letterSpacing = '1px';
    ctx.fillText('RESERVAR NO WHATSAPP • (48) 99830-1122', CANVAS_WIDTH / 2, btnY + btnHeight / 2);
    ctx.letterSpacing = '0px';

    curY = btnY + btnHeight + 52;

    // 10. Rodapé Institucional
    ctx.font = '500 21px "Plus Jakarta Sans", sans-serif';
    ctx.fillStyle = '#A8A196';
    ctx.fillText('📍 Servidão Elpídio da Rocha, 40 • Rio Tavares Central, Florianópolis', CANVAS_WIDTH / 2, curY);

    curY += 34;

    ctx.font = '600 19px "Plus Jakarta Sans", sans-serif';
    ctx.fillStyle = '#C89B58';
    ctx.fillText('Acesse o cardápio completo no link da bio: @engelke_cafe', CANVAS_WIDTH / 2, curY);

    curY += 32;

    ctx.font = '600 14px "Plus Jakarta Sans", sans-serif';
    ctx.fillStyle = 'rgba(200, 155, 88, 0.55)';
    ctx.letterSpacing = '3px';
    ctx.fillText('ORGANISMO CERTIFICADO SPG / OPAC ABDSUL • DEMETER BRASIL', CANVAS_WIDTH / 2, curY);
    ctx.letterSpacing = '0px';

    return canvas;
  }

  // --------------------------------------------------------------------------
  // Utilitários de Desenho
  // --------------------------------------------------------------------------

  function desenharBadgeStatus(ctx, status, y) {
    let texto = '🔥 FORNADA SAINDO DO FORNO';
    let bg = 'rgba(214, 61, 51, 0.22)';
    let border = '#D63D33';
    let textColor = '#FF7B73';

    if (status === 'ativo' || status === 'disponivel') {
      texto = '🥖 PÃES FRESCOS NO BALCÃO';
      bg = 'rgba(66, 91, 70, 0.35)';
      border = '#5C7F62';
      textColor = '#4ADE80';
    } else if (status === 'preparando') {
      texto = '⏳ FORNADA NO FORNO';
      bg = 'rgba(200, 155, 88, 0.25)';
      border = '#C89B58';
      textColor = '#FCD34D';
    } else if (status === 'ultimas_unidades') {
      texto = '⚠️ RESTAM POUCAS UNIDADES';
      bg = 'rgba(217, 119, 6, 0.28)';
      border = '#D97706';
      textColor = '#FBBF24';
    } else if (status === 'pausado' || status === 'esgotado') {
      texto = '🌙 FORNADA ENCERRADA POR HOJE';
      bg = 'rgba(122, 114, 104, 0.3)';
      border = '#7A7268';
      textColor = '#D4CFC7';
    }

    ctx.font = '700 28px "Oswald", sans-serif';
    const textMetrics = ctx.measureText(texto);
    const pillWidth = textMetrics.width + 60;
    const pillHeight = 56;
    const pillX = (CANVAS_WIDTH - pillWidth) / 2;

    ctx.fillStyle = bg;
    desenharRetanguloArredondado(ctx, pillX, y, pillWidth, pillHeight, 28);
    ctx.fill();

    ctx.strokeStyle = border;
    ctx.lineWidth = 1.5;
    desenharRetanguloArredondado(ctx, pillX, y, pillWidth, pillHeight, 28);
    ctx.stroke();

    ctx.fillStyle = textColor;
    ctx.fillText(texto, CANVAS_WIDTH / 2, y + pillHeight / 2);

    return y + pillHeight;
  }

  function desenharDivisorJoalheria(ctx, cx, cy, width) {
    const half = width / 2;
    const gap = 14;

    ctx.save();
    ctx.strokeStyle = 'rgba(200, 155, 88, 0.35)';
    ctx.lineWidth = 1;

    // Linha esquerda
    ctx.beginPath();
    ctx.moveTo(cx - half, cy);
    ctx.lineTo(cx - gap, cy);
    ctx.stroke();

    // Linha direita
    ctx.beginPath();
    ctx.moveTo(cx + gap, cy);
    ctx.lineTo(cx + half, cy);
    ctx.stroke();

    // Losango central de latão
    ctx.fillStyle = '#C89B58';
    ctx.beginPath();
    ctx.moveTo(cx, cy - 4.5);
    ctx.lineTo(cx + 4.5, cy);
    ctx.lineTo(cx, cy + 4.5);
    ctx.lineTo(cx - 4.5, cy);
    ctx.closePath();
    ctx.fill();
    ctx.restore();
  }

  function desenharFaixaPilaresPureza(ctx, cx, cy, maxWidth) {
    const boxH = 46;
    const boxW = Math.min(maxWidth, 780);
    const boxX = cx - (boxW / 2);
    const boxY = cy - (boxH / 2);

    ctx.save();
    // Cápsula sutil de fundo
    ctx.fillStyle = 'rgba(200, 155, 88, 0.04)';
    desenharRetanguloArredondado(ctx, boxX, boxY, boxW, boxH, 10);
    ctx.fill();

    ctx.strokeStyle = 'rgba(200, 155, 88, 0.18)';
    ctx.lineWidth = 1;
    desenharRetanguloArredondado(ctx, boxX, boxY, boxW, boxH, 10);
    ctx.stroke();

    // Texto dos pilares em tipografia suíça refinada
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.font = '700 13px "Plus Jakarta Sans", sans-serif';
    ctx.fillStyle = '#C89B58';
    ctx.letterSpacing = '2px';

    const textoCompleto = 'FARINHAS BIODINÂMICAS   •   LEVAIN SELVAGEM 36H   •   FORNO DE LASTRO';
    ctx.fillText(textoCompleto, cx, cy);
    ctx.letterSpacing = '0px';
    ctx.restore();
  }

  function desenharCartuchoTelemetria(ctx, x, y, width, height, kicker, valor) {
    ctx.save();
    // Fundo do cartucho
    ctx.fillStyle = 'rgba(200, 155, 88, 0.06)';
    desenharRetanguloArredondado(ctx, x, y, width, height, 14);
    ctx.fill();

    // Borda de latão
    ctx.strokeStyle = 'rgba(200, 155, 88, 0.28)';
    ctx.lineWidth = 1;
    desenharRetanguloArredondado(ctx, x, y, width, height, 14);
    ctx.stroke();

    // Top highlight tênue
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(x + 14, y + 1);
    ctx.lineTo(x + width - 14, y + 1);
    ctx.stroke();

    // Rótulo da Telemetria (Caixa Alta com Tracking)
    ctx.textAlign = 'center';
    ctx.font = '700 13px "Plus Jakarta Sans", sans-serif';
    ctx.fillStyle = '#C89B58';
    ctx.letterSpacing = '2px';
    ctx.fillText(kicker, x + width / 2, y + 28);
    ctx.letterSpacing = '0px';

    // Valor da Telemetria (Firme e Límpido)
    ctx.font = '600 19px "Plus Jakarta Sans", sans-serif';
    ctx.fillStyle = '#FFFFFF';
    ctx.fillText(valor, x + width / 2, y + 60);

    ctx.restore();
  }

  function desenharCantosLatão(ctx, left, right, top, bottom) {
    const len = 20;
    ctx.strokeStyle = '#C89B58';
    ctx.lineWidth = 2.5;

    // Top-Left
    ctx.beginPath();
    ctx.moveTo(left, top + len);
    ctx.lineTo(left, top);
    ctx.lineTo(left + len, top);
    ctx.stroke();

    // Top-Right
    ctx.beginPath();
    ctx.moveTo(right - len, top);
    ctx.lineTo(right, top);
    ctx.lineTo(right, top + len);
    ctx.stroke();

    // Bottom-Left
    ctx.beginPath();
    ctx.moveTo(left, bottom - len);
    ctx.lineTo(left, bottom);
    ctx.lineTo(left + len, bottom);
    ctx.stroke();

    // Bottom-Right
    ctx.beginPath();
    ctx.moveTo(right - len, bottom);
    ctx.lineTo(right, bottom);
    ctx.lineTo(right, bottom - len);
    ctx.stroke();
  }

  function desenharRetanguloArredondado(ctx, x, y, width, height, radius) {
    ctx.beginPath();
    ctx.moveTo(x + radius, y);
    ctx.lineTo(x + width - radius, y);
    ctx.quadraticCurveTo(x + width, y, x + width, y + radius);
    ctx.lineTo(x + width, y + height - radius);
    ctx.quadraticCurveTo(x + width, y + height, x + width - radius, y + height);
    ctx.lineTo(x + radius, y + height);
    ctx.quadraticCurveTo(x, y + height, x, y + height - radius);
    ctx.lineTo(x, y + radius);
    ctx.quadraticCurveTo(x, y, x + radius, y);
    ctx.closePath();
  }

  function quebrarTextoCentrado(ctx, text, x, y, maxWidth, lineHeight) {
    const words = text.split(' ');
    let line = '';
    let curY = y;

    for (let n = 0; n < words.length; n++) {
      const testLine = line + words[n] + ' ';
      const metrics = ctx.measureText(testLine);
      if (metrics.width > maxWidth && n > 0) {
        ctx.fillText(line.trim(), x, curY);
        line = words[n] + ' ';
        curY += lineHeight;
      } else {
        line = testLine;
      }
    }
    ctx.fillText(line.trim(), x, curY);
    return curY;
  }

  function desenharTotemCisneVetorial(ctx, cx, cy, r) {
    ctx.save();
    ctx.strokeStyle = '#C89B58';
    ctx.fillStyle = '#C89B58';
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';

    // Aro Externo e Interno Duplo
    ctx.beginPath();
    ctx.arc(cx, cy, r, 0, Math.PI * 2);
    ctx.lineWidth = 3.5;
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(cx, cy, r * 0.9, 0, Math.PI * 2);
    ctx.lineWidth = 1.8;
    ctx.strokeStyle = 'rgba(200, 155, 88, 0.6)';
    ctx.stroke();

    // Pescoço e Cabeça do Cisne
    ctx.strokeStyle = '#E0BA7E';
    const scale = (r * 0.85) / 50;
    ctx.beginPath();
    ctx.moveTo(cx + (66 - 50) * scale, cy + (33 - 50) * scale);
    ctx.bezierCurveTo(
      cx + (65 - 50) * scale, cy + (24 - 50) * scale,
      cx + (59 - 50) * scale, cy + (20 - 50) * scale,
      cx + (55 - 50) * scale, cy + (21 - 50) * scale
    );
    ctx.bezierCurveTo(
      cx + (51.5 - 50) * scale, cy + (22.5 - 50) * scale,
      cx + (52 - 50) * scale, cy + (30 - 50) * scale,
      cx + (53.5 - 50) * scale, cy + (38 - 50) * scale
    );
    ctx.bezierCurveTo(
      cx + (55.5 - 50) * scale, cy + (48 - 50) * scale,
      cx + (62 - 50) * scale, cy + (58 - 50) * scale,
      cx + (70 - 50) * scale, cy + (67 - 50) * scale
    );
    ctx.bezierCurveTo(
      cx + (75 - 50) * scale, cy + (72.5 - 50) * scale,
      cx + (77.8 - 50) * scale, cy + (75.8 - 50) * scale,
      cx + (78.5 - 50) * scale, cy + (77.5 - 50) * scale
    );
    ctx.lineWidth = 4;
    ctx.stroke();

    // Corpo e Asas em 'E' Caligráfico Contínuo
    ctx.beginPath();
    ctx.moveTo(cx + (59 - 50) * scale, cy + (55 - 50) * scale);
    ctx.bezierCurveTo(
      cx + (44 - 50) * scale, cy + (54 - 50) * scale,
      cx + (28 - 50) * scale, cy + (55 - 50) * scale,
      cx + (23 - 50) * scale, cy + (60 - 50) * scale
    );
    ctx.bezierCurveTo(
      cx + (20.5 - 50) * scale, cy + (62.5 - 50) * scale,
      cx + (21.5 - 50) * scale, cy + (65.5 - 50) * scale,
      cx + (26 - 50) * scale, cy + (66.5 - 50) * scale
    );
    ctx.bezierCurveTo(
      cx + (36 - 50) * scale, cy + (67.5 - 50) * scale,
      cx + (46 - 50) * scale, cy + (68 - 50) * scale,
      cx + (47.5 - 50) * scale, cy + (68.5 - 50) * scale
    );
    ctx.bezierCurveTo(
      cx + (36 - 50) * scale, cy + (71 - 50) * scale,
      cx + (23 - 50) * scale, cy + (73.5 - 50) * scale,
      cx + (21.5 - 50) * scale, cy + (77 - 50) * scale
    );
    ctx.bezierCurveTo(
      cx + (20.5 - 50) * scale, cy + (80 - 50) * scale,
      cx + (23.5 - 50) * scale, cy + (81.5 - 50) * scale,
      cx + (33 - 50) * scale, cy + (81.5 - 50) * scale
    );
    ctx.bezierCurveTo(
      cx + (48 - 50) * scale, cy + (81.5 - 50) * scale,
      cx + (68 - 50) * scale, cy + (80.5 - 50) * scale,
      cx + (78.5 - 50) * scale, cy + (77.5 - 50) * scale
    );
    ctx.lineWidth = 4;
    ctx.stroke();

    ctx.restore();
  }

  function carregarImagem(src) {
    return new Promise((resolve, reject) => {
      const img = new Image();
      img.crossOrigin = 'anonymous';
      img.onload = () => resolve(img);
      img.onerror = reject;
      img.src = src;
    });
  }

  /**
   * Dispara o download automático do PNG para o celular
   */
  async function baixarStoryPNG(state, nomeArquivo) {
    const canvas = await gerarCanvasStory(state);
    const dataUrl = canvas.toDataURL('image/png');

    const link = document.createElement('a');
    link.download = nomeArquivo || `story-fornada-engelke-${Date.now()}.png`;
    link.href = dataUrl;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    return { canvas, dataUrl };
  }

  /**
   * Abre o menu nativo de compartilhamento do celular se suportado
   */
  async function compartilharStoryNativo(state) {
    const canvas = await gerarCanvasStory(state);
    
    return new Promise((resolve, reject) => {
      canvas.toBlob(async (blob) => {
        if (!blob) {
          reject(new Error('Falha ao gerar imagem do Story.'));
          return;
        }

        const file = new File([blob], `story-fornada-engelke.png`, { type: 'image/png' });
        
        if (navigator.canShare && navigator.canShare({ files: [file] })) {
          try {
            await navigator.share({
              files: [file],
              title: 'Fornada Brothaus Engelke',
              text: 'Fornada saindo fresca agora na Brothaus Engelke!'
            });
            resolve({ shared: true });
          } catch (err) {
            resolve({ shared: false, cancelled: true });
          }
        } else {
          // Se não suportar Web Share API com arquivos, baixa automaticamente
          baixarStoryPNG(state);
          resolve({ shared: false, downloaded: true });
        }
      }, 'image/png');
    });
  }

  return {
    gerarCanvasStory: gerarCanvasStory,
    baixarStoryPNG: baixarStoryPNG,
    compartilharStoryNativo: compartilharStoryNativo
  };
})();
