# E440DDC

## Descrição

Compras - Notas Fiscais de Entrada - Taxas e Contribuições Cana de Açúcar

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| SeqDdc | Number(002,0) | Não | Sequência da Dedução de Cana |
| DesDdc | String(060) | Não | Descrição da Dedução de Cana |
| VlrDed | Number(015,2) | Sim | Valor Total da Dedução |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqDdc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440DDC_002

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

### IR_E440DDC_004

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

