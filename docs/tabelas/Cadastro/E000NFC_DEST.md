# E000NFC_DEST

## Descrição

Recebimento de Documentos eletrônicos - Notas Fiscais de entrada - Destinatário

---

## Resumo

- Campos: 20
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
| NomDst | String(100) | Sim | Nome do destinatário |
| EndDst | String(100) | Sim | Endereço do destinatário |
| NenDst | String(060) | Sim | Número do endereço do destinatário |
| BaiDst | String(075) | Sim | Bairro do destinatário |
| CepDst | Number(008,0) | Sim | CEP do destinatário |
| CicDst | Number(007,0) | Sim | Código Municipio do destinatário |
| CixDst | String(060) | Sim | Cidade do destinatário |
| UfsDst | String(002) | Sim | Estado do destinatário |
| PacDst | String(004) | Sim | Código do país do destinatário |
| PaxDst | String(060) | Sim | País do destinatário |
| IneDst | String(025) | Sim | Inscrição estadual do destinatário |
| InmDst | String(016) | Sim | Inscrição municipal do destinatário |
| FonDst | String(020) | Sim | Número do telefone do destinatário |
| IdeUni | String(050) | Não | Identificador único alfanumérico |
| IdeNfc | String(050) | Não | Identificador único alfanumérico |

---

## Chave Primária

- IdeUni

---

## Índices

### E000NFCDESTIndice1

**Tipo:** Não unico

Campos:
- CgcFil
- CgcFor
- ChvNel

### E000NFCDESTIndice2

**Tipo:** Não unico

Campos:
- DocIdeFil
- DocIdeFor
- ChvNel

### E000NFCDESTIndice3

**Tipo:** Não unico

Campos:
- IdeNfc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
