# E210LFI

## Descrição

Estoques - Conteúdo das Embalagens de Estocagem (Volume - Lotes)

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| NumEmb | String(030) | Não | Número da embalagem |
| SeqEfi | Number(004,0) | Não | Sequência do conteúdo da embalagem de estocagem |
| SeqLfi | Number(004,0) | Não | Sequência do lote na embalagem de estocagem |
| CodLot | String(050) | Sim | Código do Lote de Fabricação para estocagem |
| QtdIte | Number(014,5) | Sim | Quantidade do item na embalagem |
| PesLiq | Number(014,5) | Sim | Peso líquido do produto/embalagem |

---

## Chave Primária

- CodEmp
- NumEmb
- SeqEfi
- SeqLfi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E210LFI_001

**Tabela:** E210EMB

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| NumEmb | NumEmb |

### IR_E210LFI_002

**Tabela:** E210EFI

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| NumEmb | NumEmb |
| SeqEfi | SeqEfi |

