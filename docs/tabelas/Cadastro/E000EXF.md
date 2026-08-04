# E000EXF

## Descrição

Tabelas - Recebimento de Documentos Eletrônicos - Notas Fiscais de Entrada - Ligação Notas de Frete

---

## Resumo

- Campos: 17
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
| SeqExf | Number(004,0) | Não | Sequência de composição de notas fiscais de entrada |
| NumNfc | Number(009,0) | Sim | Número da nota fiscal de entrada |
| CodSnf | String(003) | Sim | Código da série da nota fiscal de entrada |
| FilRlc | Number(015,0) | Sim | Código CGC da filial da nota fiscal relacionada (entrada ou saída) |
| DocIdeRlc | String(014) | Sim | Código CGC da filial da nota fiscal relacionada (entrada ou saída) |
| ForRlc | Number(015,0) | Sim | Código CGC do fornecedor da nota fiscal de entrada relacionada |
| DocIdeFrl | String(014) | Sim | Código CGC do fornecedor da nota fiscal de entrada relacionada |
| NumRlc | Number(009,0) | Sim | Número da nota fiscal relacionada (entrada ou saída) |
| SnfRlc | String(003) | Sim | Série da nota fiscal relacionada (entrada ou saída) |
| ChvRlc | String(050) | Sim | Chave Nota Fiscal Eletrônica Relacionada |
| IdeUni | String(050) | Não | Identificador único alfanumérico |
| IdeNfc | String(050) | Não | Identificador único alfanumérico |

---

## Chave Primária

- IdeUni

---

## Índices

### E000EXFIndice1

**Tipo:** Não unico

Campos:
- DocIdeFil
- DocIdeFor
- ChvNel
- SeqExf

### E000EXFIndice2

**Tipo:** Não unico

Campos:
- CgcFil
- CgcFor
- ChvNel
- SeqExf

### E000EXFIndice3

**Tipo:** Não unico

Campos:
- IdeNfc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
