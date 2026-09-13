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
    const cardWidth = CANVAS_WIDTH - 180;
    const cardX = (CANVAS_WIDTH - cardWidth) / 2;
    const cardTop = curY;
    const cardHeight = 580;

    // Fundo do Card
    ctx.fillStyle = 'rgba(28, 24, 21, 0.94)';
    desenharRetanguloArredondado(ctx, cardX, cardTop, cardWidth, cardHeight, 16);
    ctx.fill();

    // Borda do Card
    ctx.strokeStyle = 'rgba(200, 155, 88, 0.45)';
    ctx.lineWidth = 1.5;
    desenharRetanguloArredondado(ctx, cardX, cardTop, cardWidth, cardHeight, 16);
    ctx.stroke();

    // Detalhe da Costura em Linha Vermelha Artesanal no Topo do Card
    ctx.save();
    ctx.strokeStyle = '#C83E36';
    ctx.lineWidth = 3;
    ctx.setLineDash([8, 6]);
    ctx.beginPath();
    ctx.moveTo(cardX + 24, cardTop + 14);
    ctx.lineTo(cardX + cardWidth - 24, cardTop + 14);
    ctx.stroke();
    ctx.restore();

    let insideY = cardTop + 56;

    // Kicker do Card
    ctx.font = '700 20px "Plus Jakarta Sans", sans-serif';
    ctx.fillStyle = '#C89B58';
    ctx.fillText('OFÍCIO ANCESTRAL • FERMENTAÇÃO NATURAL 36H', CANVAS_WIDTH / 2, insideY);

    insideY += 55;

    // Título do Pão em Destaque
    const paoDestaque = (state.config && state.config.pao_destaque_hoje) || 'Sourdough Tradicional Demeter';
    ctx.font = '600 44px "Playfair Display", Georgia, serif';
    ctx.fillStyle = '#FFFFFF';
    
    // Quebra de texto elegante para títulos longos
    insideY = quebrarTextoCentrado(ctx, paoDestaque, CANVAS_WIDTH / 2, insideY, cardWidth - 80, 52);

    insideY += 25;

    // Linha divisória fina de latão
    ctx.strokeStyle = 'rgba(200, 155, 88, 0.25)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(CANVAS_WIDTH / 2 - 140, insideY);
    ctx.lineTo(CANVAS_WIDTH / 2 + 140, insideY);
    ctx.stroke();

    insideY += 45;

    // Mensagem / Detalhes da Fornada
    const alertaTexto = (state.config && state.config.alerta_texto) || 'Pães de fermentação lenta de 36 horas, crosta dourada e miolo com alvéolos abertos.';
    ctx.font = '400 26px "Plus Jakarta Sans", sans-serif';
    ctx.fillStyle = '#D4CFC7';
    insideY = quebrarTextoCentrado(ctx, alertaTexto, CANVAS_WIDTH / 2, insideY, cardWidth - 100, 36);

    insideY += 35;

    // Bloco de 3 Metadados / Telemetria
    const boxY = cardTop + cardHeight - 110;
    const colW = cardWidth / 3;

    desenharColunaTelemetria(ctx, cardX, boxY, colW, 'FERMENTAÇÃO', '36h Levain Selvagem');
    desenharColunaTelemetria(ctx, cardX + colW, boxY, colW, 'CERTIFICAÇÃO', 'Demeter Biodinâmica');
    desenharColunaTelemetria(ctx, cardX + colW * 2, boxY, colW, 'MOAGEM', 'Farinha Demeter');

    // 8. Seção de Horário & Próxima Fornada
    curY = cardTop + cardHeight + 45;

    const proxFornada = (state.config && state.config.proxima_fornada) || 'Hoje • Fornada Especial';
    ctx.font = '600 22px "Plus Jakarta Sans", sans-serif';
    ctx.fillStyle = '#C89B58';
    ctx.fillText('CRONOGRAMA DO DIA', CANVAS_WIDTH / 2, curY);

    curY += 38;

    ctx.font = '700 40px "Oswald", sans-serif';
    ctx.fillStyle = '#FFFFFF';
    ctx.fillText(proxFornada.toUpperCase(), CANVAS_WIDTH / 2, curY);

    curY += 70;

    // 9. Call To Action Principal (Botão Dourado de Reserva)
    const btnWidth = cardWidth;
    const btnHeight = 100;
    const btnX = (CANVAS_WIDTH - btnWidth) / 2;
    const btnY = curY;

    // Sombra do botão
    ctx.save();
    ctx.shadowColor = 'rgba(200, 155, 88, 0.4)';
    ctx.shadowBlur = 30;
    ctx.shadowOffsetY = 8;

    // Gradiente Dourado Latão
    const btnGrad = ctx.createLinearGradient(btnX, btnY, btnX + btnWidth, btnY + btnHeight);
    btnGrad.addColorStop(0, '#E0BA7E');
    btnGrad.addColorStop(1, '#B88741');
    ctx.fillStyle = btnGrad;
    desenharRetanguloArredondado(ctx, btnX, btnY, btnWidth, btnHeight, 18);
    ctx.fill();
    ctx.restore();

    // Texto do Botão
    ctx.font = '700 32px "Oswald", sans-serif';
    ctx.fillStyle = '#141210';
    ctx.fillText('RESERVAR NO WHATSAPP • (48) 99830-1122', CANVAS_WIDTH / 2, btnY + btnHeight / 2 - 2);

    curY = btnY + btnHeight + 50;

    // 10. Rodapé Institucional
    ctx.font = '500 22px "Plus Jakarta Sans", sans-serif';
    ctx.fillStyle = '#A8A196';
    ctx.fillText('📍 Servidão Elpídio da Rocha • Rio Tavares Central, Florianópolis', CANVAS_WIDTH / 2, curY);

    curY += 34;

    ctx.font = '600 20px "Plus Jakarta Sans", sans-serif';
    ctx.fillStyle = '#C89B58';
    ctx.fillText('Acesse o cardápio completo no link da bio: @engelke_cafe', CANVAS_WIDTH / 2, curY);

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

  function desenharColunaTelemetria(ctx, x, y, width, kicker, valor) {
    ctx.textAlign = 'center';
    ctx.font = '600 16px "Plus Jakarta Sans", sans-serif';
    ctx.fillStyle = '#C89B58';
    ctx.fillText(kicker, x + width / 2, y);

    ctx.font = '600 20px "Plus Jakarta Sans", sans-serif';
    ctx.fillStyle = '#FFFFFF';
    ctx.fillText(valor, x + width / 2, y + 26);
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
