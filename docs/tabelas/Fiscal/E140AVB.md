# E140AVB

## Descrição

Vendas - Notas Fiscais de Saída - Informações de seguro - Averbações

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
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqSeg | Number(004,0) | Não | Sequência do seguro da carga |
| SeqAvb | Number(004,0) | Não | Sequencia Averbação |
| NumAvb | String(060) | Sim | Número da averbação. |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqSeg
- SeqAvb

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140AVB_004

**Tabela:** E140SEG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |
| SeqSeg | SeqSeg |

