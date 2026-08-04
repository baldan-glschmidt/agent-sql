# E000NRF

## Descrição

Tabelas - Recebimento de Documentos Eletrônicos - Notas Fiscais de Entrada - Notas Referênciadas

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CgcFil | Number(015,0) | Sim | Número do cadastro nacional de pessoa jurídica da filial da empresa |
| DocIdeFil | String(014) | Sim | Número do cadastro nacional de pessoa jurídica da filial da empresa |
| CgcFor | Number(014,0) | Sim | Número do CNPJ ou CPF do fornecedor |
| DocIdeFor | String(014) | Sim | Número do CNPJ ou CPF do fornecedor |
| ChvNel | String(050) | Não | Chave de acesso da nota fiscal eletrônica |
| ChvRlc | String(050) | Não | Chave de acesso da nota fiscal eletrônica relacionada |
| IdeNfc | String(050) | Não | Identificador único alfanumérico |

---

## Chave Primária

- IdeUni

---

## Índices

### E000NRFIndice1

**Tipo:** Não unico

Campos:
- CgcFil
- CgcFor
- ChvNel

### E000NRFIndice2

**Tipo:** Não unico

Campos:
- DocIdeFil
- DocIdeFor
- ChvNel

### E000NRFIndice3

**Tipo:** Não unico

Campos:
- IdeNfc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
