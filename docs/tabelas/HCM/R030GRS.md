# R030GRS

## Descrição

Filiais da Empresa - GRCS

---

## Resumo

- Campos: 11
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| ComGrc | Date | Não | Competência GRCS |
| TipGrc | Number(002,0) | Não | Tipo da GRCS |
| CodSin | Number(004,0) | Não | Código do Sindicato |
| VlrCap | Number(011,2) | Sim | Capital Social Empresa    C33 |
| TotEmp | Number(011,2) | Sim | Total Empresa             C34 |
| TotEst | Number(011,2) | Sim | Total Estabelecimento     C35 |
| CapEst | Number(011,2) | Sim | Capital Estabelecimento   C36 |
| BasCtr | Number(011,2) | Sim | Base Cálc. Contribuição   C37 |
| ValCtr | Number(011,2) | Sim | Valor da Contribuição (C42) |

---

## Chave Primária

- NumEmp
- CodFil
- ComGrc
- TipGrc
- CodSin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030GRS_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R030GRS_004

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

