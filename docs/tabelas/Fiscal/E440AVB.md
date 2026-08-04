# E440AVB

## Descrição

Compras - Notas Fiscais de Entrada - Seguro da Carga - Averbação

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| SeqSeg | Number(004,0) | Não | Sequência do seguro da carga |
| SeqAvb | Number(004,0) | Não | Sequencia Averbação |
| NumAvb | String(060) | Sim | Número da averbação. |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfc
- SeqSeg
- SeqAvb

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440AVB_004

**Tabela:** E440SEG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfc | NumNfc |
| SeqSeg | SeqSeg |

