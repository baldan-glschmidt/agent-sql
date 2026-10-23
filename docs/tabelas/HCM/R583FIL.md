# R583FIL

## Descrição

GHE - Cadastro de PGR - Filiais

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| DatIni | Date | Não | Data em que a filial passa a fazer parte do PGR. |
| SeqReg | Number(002,0) | Não | Sequência |
| DatTer | Date | Sim | Data em que a filial deixa de fazer parte do PGR. |
| TabOrg | Number(004,0) | Sim | Código da Tabela do Organograma |
| NumLoc | Number(009,0) | Sim | Local do Organograma |

---

## Chave Primária

- CodPRA
- NumEmp
- CodFil
- DatIni
- SeqReg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R583FIL_000

**Tabela:** R583CAD

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |

### IR_R583FIL_002

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

