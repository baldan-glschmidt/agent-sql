# E000LNS

## Descrição

Tabelas - Recebimento de Documentos Eletrônicos - Notas Fiscais de Entrada - Ligação Entre Itens Serviço Notas Fiscais de Entrada

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
| SeqLns | Number(004,0) | Não | Sequência de ligação |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Sim | Código da série da nota fiscal |
| SeqIsc | Number(003,0) | Sim | Sequência do item na nota fiscal de entrada |
| ChvRlc | String(050) | Não | Chave de acesso da nota fiscal eletrônica relacionada |
| FilRlc | Number(005,0) | Sim | Código da filial da nota fiscal entrada relacionada |
| ForRlc | Number(009,0) | Sim | Código do fornecedor da nota fiscal de entrada relacionada |
| NumRlc | Number(009,0) | Sim | Número da nota fiscal entrada relacionada |
| SnfRlc | String(003) | Sim | Série da nota fiscal entrada relacionada |
| IscRlc | Number(003,0) | Sim | Sequência do Item de Serviço Relacionado |
| IdeNfc | String(050) | Não | Identificador único alfanumérico |

---

## Chave Primária

- IdeUni

---

## Índices

### E000LNSIndice1

**Tipo:** Não unico

Campos:
- CgcFil
- CgcFor
- ChvNel
- SeqLns

### E000LNSIndice2

**Tipo:** Não unico

Campos:
- CgcFil
- CgcFor
- ChvNel

### E000LNSIndice3

**Tipo:** Não unico

Campos:
- IdeNfc

### E000LNSIndice4

**Tipo:** Não unico

Campos:
- DocIdeFil
- DocIdeFor
- ChvNel
- SeqLns

---

## Relacionamentos

Nenhum relacionamento cadastrado.
