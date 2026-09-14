/**
 * ============================================================================
 * BROTHAUS ENGELKE • BACKEND ULTRA-MINIMALISTA (API REST GOOGLE SHEETS)
 * ============================================================================
 */
const PIN_SEGURANCA = "1832";

function doGet(e) {
  try {
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    const sheet = ss.getSheetByName("Config") || ss.getSheets()[0];
    const rows = sheet.getDataRange().getValues();
    const config = {};

    for (let i = 1; i < rows.length; i++) {
      const chave = String(rows[i][0]).trim();
      if (chave) config[chave] = rows[i][1];
    }

    return ContentService.createTextOutput(JSON.stringify({
      success: true,
      data: { config: config }
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (erro) {
    return ContentService.createTextOutput(JSON.stringify({
      success: false,
      error: erro.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

function doPost(e) {
  try {
    if (!e || !e.postData || !e.postData.contents) {
      return ContentService.createTextOutput(JSON.stringify({ success: false, error: "Sem dados" }))
        .setMimeType(ContentService.MimeType.JSON);
    }

    const payload = JSON.parse(e.postData.contents);
    if (String(payload.pin).trim() !== PIN_SEGURANCA) {
      return ContentService.createTextOutput(JSON.stringify({ success: false, error: "PIN inválido" }))
        .setMimeType(ContentService.MimeType.JSON);
    }

    const ss = SpreadsheetApp.getActiveSpreadsheet();
    const sheet = ss.getSheetByName("Config") || ss.getSheets()[0];
    const rows = sheet.getDataRange().getValues();
    const updates = payload.config || {};
    updates.ultima_atualizacao = Utilities.formatDate(new Date(), "America/Sao_Paulo", "yyyy-MM-dd HH:mm:ss");

    for (let i = 1; i < rows.length; i++) {
      const chave = String(rows[i][0]).trim();
      if (updates[chave] !== undefined) {
        sheet.getRange(i + 1, 2).setValue(updates[chave]);
      }
    }

    return ContentService.createTextOutput(JSON.stringify({
      success: true,
      message: "Fornada atualizada na planilha!",
      updatedAt: updates.ultima_atualizacao
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (erro) {
    return ContentService.createTextOutput(JSON.stringify({
      success: false,
      error: erro.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}