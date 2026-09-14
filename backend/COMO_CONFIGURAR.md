# 🥐 Guia de Configuração: Backend Google Apps Script • Brothaus Engelke

Este guia explica como ativar o backend 100% gratuito e perpétuo usando **Google Sheets + Google Apps Script**. Todo o processo leva menos de **3 minutos**.

---

## Passo 1: Criar a Planilha no Google Drive

1. Abra o [Google Drive](https://drive.google.com/) ou acesse [sheets.new](https://sheets.new).
2. Renomeie a nova planilha para:
   ```text
   Fornadas Engelke
   ```

---

## Passo 2: Adicionar o Código do Apps Script

1. No menu superior da planilha, clique em:
   **Extensões** > **Apps Script**.
2. Uma nova aba será aberta com um editor de código (`Code.gs`).
3. Apague qualquer código existente no editor.
4. Abra o arquivo local [`engelke/backend/Code.gs`](file:///c:/Users/carlo/OneDrive%20-%20Carlos%20Linzmeyer/Trabalho/Carlos%20Linzmeyer/TI/WorkAround/engelke/backend/Code.gs), copie **todo o conteúdo** e cole no editor do Google.
5. Clique no ícone de **Salvar** (disquete ou `Ctrl + S`).

---

## Passo 3: Inicializar a Estrutura da Planilha (1 Clique)

1. No topo do editor, na barra de ferramentas onde diz `doGet`, mude para a função:
   `inicializarPlanilha`
2. Clique no botão **Executar** (ícone de Play ▶).
3. O Google exibirá um aviso de "Autorização necessária".
   - Clique em **Revisar permissões**.
   - Escolha sua conta Google.
   - Clique em **Avançado** (na parte inferior esquerda do pop-up).
   - Clique em **Acessar Fornadas Engelke (não seguro)**.
   - Clique em **Permitir**.
4. Volte à sua aba da planilha no Google Sheets: você verá que as abas **Config** e **Cronograma** foram criadas e estilizadas automaticamente com os dados oficiais da Engelke!

---

## Passo 4: Publicar como Web App (Gerar a URL da API)

1. No canto superior direito do editor do Apps Script, clique no botão azul **Implantar** (Deploy) > **Nova implantação**.
2. Na engrenagem ⚙️ (Selecionar tipo), escolha:
   **App da Web** (Web app).
3. Preencha os campos exatamente assim:
   - **Descrição:** `API de Fornadas Brothaus Engelke`
   - **Executar como:** `Eu (seu-email@gmail.com)`
   - **Quem pode acessar:** `Qualquer pessoa` *(Isso é necessário para que o site público possa ler os pães do dia sem exigir login do Google dos clientes)*.
4. Clique em **Implantar**.
5. O Google gerará uma **URL do app da Web** parecida com:
   ```text
   https://script.google.com/macros/s/AKfycbx.../exec
   ```
6. **Copie essa URL.**

---

## Passo 5: Conectar ao Site e ao Painel Mobile

Abra o arquivo [`engelke/config.js`](file:///c:/Users/carlo/OneDrive%20-%20Carlos%20Linzmeyer/Trabalho/Carlos%20Linzmeyer/TI/WorkAround/engelke/config.js) e cole sua URL:

```javascript
window.ENGELKE_CONFIG = {
  // Cole aqui a URL gerada pelo Google Apps Script:
  API_URL: "https://script.google.com/macros/s/SUA_URL_AQUI/exec",
  
  // PIN de acesso para os padeiros (padrão 1832 - ano da Sachertorte):
  DEFAULT_PIN: "1832"
};
```

> **Dica Prática:** No próprio painel mobile (`admin/index.html`), existe uma engrenagem ⚙️ onde você também pode colar ou alterar a URL a qualquer momento direto pelo celular!

---

## Como Funciona a Segurança

- **Leitura Pública (`GET`):** O site oficial lê os dados das fornadas de forma anônima e instantânea.
- **Gravação Segura (`POST` / `update`):** Só altera os dados quem fornecer o **PIN de 4 dígitos** (padrão: `1832`). Se alguém tentar enviar sem o PIN correto, a requisição é rejeitada.
- Para alterar o PIN no futuro, você pode mudar a constante `PIN_PADRAO` no `Code.gs` ou adicionar uma propriedade no Apps Script (**Configurações do Projeto** > **Propriedades do script** > Nome: `PIN_PADARIA`).
