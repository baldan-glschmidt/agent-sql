# R032TOM

## Descrição

Recebimentos - Tomador de Serviço

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
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
| CodOem | Number(008,0) | Sim | Código do Tomador de Serviço |
| CdrFgt | Number(003,0) | Sim | Código de Recolhimento do FGTS |

---

## Chave Primária

- NumEmp
- CodFil
- CodRat
- CmpRcb
- SeqRcb

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R032TOM_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R032TOM_004

**Tabela:** R032RCB

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CodRat | CodRat |
| CmpRcb | CmpRcb |
| SeqRcb | SeqRcb |

