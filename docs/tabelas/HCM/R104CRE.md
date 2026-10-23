# R104CRE

## Descrição

JR - Rateio de Base Percentuais e Código de Receita

---

## Resumo

- Campos: 12
- Chave Primária: 10 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| CodPrc | Number(007,0) | Não | Código da Ação |
| DatCen | Date | Não | Data do cenário |
| SeqCen | Number(002,0) | Não | Sequência do cenário |
| EmpAut | Number(004,0) | Não | Empresa do autor |
| TipCol | Number(001,0) | Não | Tipo do colaborador autor |
| NumCad | Number(009,0) | Não | Código do colaborador autor |
| CmpPer | Date | Não | Competência de referência do percentual |
| CodMtj | Number(003,0) | Não | Código do Motivo do Pedido |
| TipRec | Number(002,0) | Não | Tipo de Receita |
| PerPed | Number(008,5) | Sim | Percentual para uso no cálculo do pedido |
| RecPre | Number(006,0) | Sim | Código de Receita - CR relativo a contribuições sociais devidas à Previdência Social e Outras Entidades e Fundos |

---

## Chave Primária

- NumEmp
- CodPrc
- DatCen
- SeqCen
- EmpAut
- TipCol
- NumCad
- CmpPer
- CodMtj
- TipRec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104CRE_008

**Tabela:** R104BPE

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |
| DatCen | DatCen |
| SeqCen | SeqCen |
| EmpAut | EmpAut |
| TipCol | TipCol |
| NumCad | NumCad |
| CmpPer | CmpPer |
| CodMtj | CodMtj |

