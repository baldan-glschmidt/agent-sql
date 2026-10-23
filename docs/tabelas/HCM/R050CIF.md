# R050CIF

## Descrição

DARF - Darfs Acumulados < 10 reais

---

## Resumo

- Campos: 7
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodRec | Number(004,0) | Não | Código da Receita |
| DatApu | Date | Não | Data Apuração |
| NumPar | Number(002,0) | Não | Número da Parcela |
| ApuRec | Date | Não |  |
| ParRec | Number(002,0) | Não | Número da Parcela |

---

## Chave Primária

- NumEmp
- CodFil
- CodRec
- DatApu
- NumPar
- ApuRec
- ParRec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R050CIF_004

**Tabela:** R050AIF

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CodRec | CodRec |
| DatApu | DatApu |
| NumPar | NumPar |

