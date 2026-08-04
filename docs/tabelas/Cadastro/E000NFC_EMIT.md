# E000NFC_EMIT

## Descrição

Recebimento de Documentos eletrônicos - Notas Fiscais de entrada - Emitente

---

## Resumo

- Campos: 22
- Chave Primária: 1 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CgcFil | Number(015,0) | Sim | Número do cadastro nacional de pessoa jurídica da filial da empresa |
| DocIdeFil | String(014) | Sim | Número do cadastro nacional de pessoa jurídica da filial da empresa |
| CgcFor | Number(014,0) | Sim | Número do CNPJ ou CPF do fornecedor |
| DocIdeFor | String(014) | Sim | Número do CNPJ ou CPF do fornecedor |
| ChvNel | String(050) | Não | Chave de acesso da nota fiscal eletrônica |
| NomEmi | String(100) | Sim | Nome do emitente |
| ApeEmi | String(050) | Sim | Nome fantasia do emitente |
| EndEmi | String(100) | Sim | Endereço do emitente |
| NenEmi | String(060) | Sim | Número do endereço do emitente |
| BaiEmi | String(075) | Sim | Bairro do emitente |
| CepEmi | Number(008,0) | Sim | CEP do emitente |
| CicEmi | Number(007,0) | Sim | Código Municipio do emitente |
| CixEmi | String(060) | Sim | Cidade do emitente |
| UfsEmi | String(002) | Sim | Estado do emitente |
| PacEmi | String(004) | Sim | Código do país do emitente |
| PaxEmi | String(060) | Sim | País do emitente |
| IneEmi | String(025) | Sim | Inscrição estadual do emitente |
| InmEmi | String(016) | Sim | Inscrição municipal do emitente |
| CnaEmi | Number(010,0) | Sim | Código CNAE do emitente |
| FonEmi | String(020) | Sim | Número do telefone do emitente |
| IdeUni | String(050) | Não | Identificador único alfanumérico |
| IdeNfc | String(050) | Não | Identificador único alfanumérico |

---

## Chave Primária

- IdeUni

---

## Índices

### E000NFC_EMITIndice1

**Tipo:** Não unico

Campos:
- CgcFil
- CgcFor
- ChvNel

### E000NFC_EMITIndice2

**Tipo:** Não unico

Campos:
- DocIdeFil
- DocIdeFor
- ChvNel

### E000NFC_EMITIndice3

**Tipo:** Não unico

Campos:
- IdeNfc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
