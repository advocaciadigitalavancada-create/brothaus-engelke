/**
 * ============================================================================
 * BROTHAUS ENGELKE • CONFIGURAÇÃO CENTRAL DE FORNADAS
 * ============================================================================
 */
(function() {
  const LOCAL_STORAGE_KEY_API = "engelke_fornadas_api_url";
  const LOCAL_STORAGE_KEY_CACHE = "engelke_fornadas_cache";

  // URL padrão da API (pode ser sobrescrita pelo painel de admin ou colada aqui)
  const DEFAULT_API_URL = "";

  window.ENGELKE_CONFIG = {
    // Retorna a URL configurada localmente ou a URL padrão
    getApiUrl: function() {
      return localStorage.getItem(LOCAL_STORAGE_KEY_API) || DEFAULT_API_URL;
    },
    setApiUrl: function(url) {
      if (url) {
        localStorage.setItem(LOCAL_STORAGE_KEY_API, url.trim());
      } else {
        localStorage.removeItem(LOCAL_STORAGE_KEY_API);
      }
    },
    
    // Dados de fallback caso a rede esteja offline ou a planilha não esteja configurada ainda
    DEFAULT_DATA: {
      config: {
        status_forno: "saindo_agora",
        alerta_ativo: true,
        alerta_texto: "🔥 Fornada de Sourdough Demeter acabou de sair do forno!",
        alerta_tipo: "fornada_quente",
        proxima_fornada: "Hoje às 15h30",
        pao_destaque_hoje: "Sourdough Tradicional Demeter & Ciabatta de Oliva",
        ultima_atualizacao: new Date().toISOString()
      },
      cronograma: [
        {
          id: "qua",
          dia_semana: "Quarta-feira",
          horarios: "07h30 • 15h30",
          paes: "Sourdough Tradicional Demeter & Ciabatta de Azeite Extra Virgem",
          status: "saindo_agora",
          nota: "Fermentação lenta de 36 horas"
        },
        {
          id: "qui",
          dia_semana: "Quinta-feira",
          horarios: "07h30 • 15h30",
          paes: "Pão 100% Centeio Alemão Roggenbrot & Multigrãos Germinados",
          status: "disponivel",
          nota: "Centeio puro"
        },
        {
          id: "sex",
          dia_semana: "Sexta-feira",
          horarios: "07h30 • 15h30",
          paes: "Pão de Nozes com Figos Turcos, Baguetes Francesas & Brioches",
          status: "disponivel",
          nota: "Fornada da tarde"
        },
        {
          id: "fim",
          dia_semana: "Sábado & Domingo",
          horarios: "08h00 Especial",
          paes: "Sachertorte Imperial em fatias, Cestas de Café da Manhã & Cinnamon Rolls",
          status: "ultimas_unidades",
          nota: "Edição de fim de semana"
        }
      ]
    },

    // Cache local de alta velocidade (Stale-While-Revalidate)
    getCachedData: function() {
      try {
        const cached = localStorage.getItem(LOCAL_STORAGE_KEY_CACHE);
        if (cached) {
          return JSON.parse(cached);
        }
      } catch (e) {
        console.warn("Falha ao ler cache local:", e);
      }
      return null;
    },

    setCachedData: function(data) {
      try {
        localStorage.setItem(LOCAL_STORAGE_KEY_CACHE, JSON.stringify(data));
      } catch (e) {
        console.warn("Falha ao salvar cache local:", e);
      }
    }
  };
})();
