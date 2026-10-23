# R032COT

## Descrição

Recebimentos - Colaboradores do Tomador

---

## Resumo

- Campos: 17
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodRat | Number(009,0) | Não | Código do Rateio |
| CmpRcb | Date | Não | Competência do Recebimento |
| SeqRcb | Number(003,0) | Não | Sequência do Recebimento |
| CodOem | Number(008,0) | Não | Código do Tomador de Serviço |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| BasIns | Number(011,2) | Sim | Base de INSS/FGTS Mês |
| InsCol | Number(011,2) | Sim | Valor de INSS Mês |
| Bas13s | Number(011,2) | Sim | Base de INSS 13° Salário |
| Ins13s | Number(011,2) | Sim | Valor de INSS 13° Salário |
| BFg13s | Number(011,2) | Sim | Base de FGTS 13° Salário |
| BIn13s | Number(011,2) | Sim | Base de INSS 13° Salário Rescisão/13° Salário Complementar |
| VIn13s | Number(011,2) | Sim | Valor de INSS 13° Salário Rescisão/13° Salário Complementar |
| SalFam | Number(011,2) | Sim | Valor de Salário Família |
| CatSef | Number(002,0) | Sim | Categoria Sefip |

---

## Chave Primária

- NumEmp
- CodFil
- CodRat
- CmpRcb
- SeqRcb
- CodOem
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R032COT_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R032COT_004

**Tabela:** R032TOM

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CodRat | CodRat |
| CmpRcb | CmpRcb |
| SeqRcb | SeqRcb |

