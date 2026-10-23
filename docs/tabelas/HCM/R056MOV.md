# R056MOV

## Descrição

Informações Enviadas Para o SEFIP - Movimentações

---

## Resumo

- Campos: 14
- Chave Primária: 13 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colabolador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodRat | Number(009,0) | Não | Código do Rateio |
| CodOem | Number(008,0) | Não | Tomador de Serviço/Obra Construção Civil |
| CdrFgt | Number(003,0) | Não | Código de Recolhimento do FGTS |
| CmpSef | Date | Não | Competência de Geração do SEFIP |
| NumPro | Number(011,0) | Não | Número do Processo |
| TipSef | Number(001,0) | Não | Tipo Sefip |
| SeqReg | Number(002,0) | Não | Sequência do Registro |
| DatMov | Date | Não | Data da Movimentação |
| CodMov | String(002) | Não | Código da Movimentação |
| OriReg | String(001) | Sim | Origem do Registro |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodFil
- CodRat
- CodOem
- CdrFgt
- CmpSef
- NumPro
- TipSef
- SeqReg
- DatMov
- CodMov

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R056MOV_003

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R056MOV_010

**Tabela:** R056SEF

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodFil | CodFil |
| CodRat | CodRat |
| CodOem | CodOem |
| CdrFgt | CdrFgt |
| CmpSef | CmpSef |
| NumPro | NumPro |
| TipSef | TipSef |
| SeqReg | SeqReg |

