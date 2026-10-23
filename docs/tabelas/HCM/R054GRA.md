# R054GRA

## Descrição

GPS Acumuladas - < R$ 30,00

---

## Resumo

- Campos: 14
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodRat | Number(009,0) | Não | Código do Rateio |
| ComGrp | Date | Não | Competência GRPS |
| OriSal | Number(002,0) | Não | Código de Origem |
| CodOem | Number(008,0) | Não | Código da Outra Empresa |
| SeqReg | Number(002,0) | Não | Sequência do Registro da GPS |
| SeqGrp | Number(002,0) | Não | Sequência |
| OriAnt | Number(002,0) | Sim | Origem da GPS anterior |
| OemAnt | Number(008,0) | Sim | Código da Outra Empresa |
| ComAnt | Date | Sim | Competência Anterior |
| RatAnt | Number(009,0) | Sim | Código do Rateio Anterior |
| FilAnt | Number(006,0) | Sim | Código da Filial Anterior |
| SeqAnt | Number(002,0) | Sim | Sequência do Registro da GPS Anterior |

---

## Chave Primária

- NumEmp
- CodFil
- CodRat
- ComGrp
- OriSal
- CodOem
- SeqReg
- SeqGrp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R054GRA_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R054GRA_006

**Tabela:** R054GRP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CodRat | CodRat |
| ComGrp | ComGrp |
| OriSal | OriSal |
| CodOem | CodOem |
| SeqReg | SeqReg |

### IR_R054GRA_012

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| FilAnt | CodFil |

