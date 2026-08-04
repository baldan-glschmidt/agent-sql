# E000LNP

## Descrição

Tabelas - Recebimento de Documentos Eletrônicos - Notas Fiscais de Entrada - Ligação Entre Itens Produto Notas Fiscais de Entrada

---

## Resumo

- Campos: 17
- Chave Primária: 1 campo(s)
- Índices: 4
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
| SeqLnp | Number(004,0) | Não | Sequência de ligação |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Sim | Código da série da nota fiscal |
| SeqIpc | Number(003,0) | Sim | Sequência do item na nota fiscal de entrada |
| ChvRlc | String(050) | Não | Chave de acesso da nota fiscal eletrônica relacionada |
| FilRlc | Number(005,0) | Sim | Código da filial da nota fiscal entrada relacionada |
| ForRlc | Number(009,0) | Sim | Código do fornecedor da nota fiscal de entrada relacionada |
| NumRlc | Number(009,0) | Sim | Número da nota fiscal entrada relacionada |
| SnfRlc | String(003) | Sim | Série da nota fiscal entrada relacionada |
| IpcRlc | Number(003,0) | Sim | Sequência do item de produto relacionado |
| IdeNfc | String(050) | Não | Identificador único alfanumérico |

---

## Chave Primária

- IdeUni

---

## Índices

### E000LNPIndice1

**Tipo:** Não unico

Campos:
- CgcFil
- CgcFor
- ChvNel
- SeqLnp

### E000LNPIndice2

**Tipo:** Não unico

Campos:
- CgcFil
- CgcFor
- ChvNel

### E000LNPIndice3

**Tipo:** Não unico

Campos:
- IdeNfc

### E000LNPIndice4

**Tipo:** Não unico

Campos:
- DocIdeFil
- DocIdeFor
- ChvNel
- SeqLnp

---

## Relacionamentos

Nenhum relacionamento cadastrado.
