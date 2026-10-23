# R161DEE

## Descrição

Bs - Definições Faixas Empréstimos

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Codigo da Empresa |
| CmpDef | Date | Não | Competência das Definições |
| TipDef | Number(001,0) | Não | Tipo de Faixas |
| SeqDef | Number(002,0) | Não | Sequência das Faixas |
| VlrMin | Number(011,2) | Sim | Mínimo |
| VlrMax | Number(011,2) | Sim | Máximo |
| VlrSal | Number(011,2) | Sim | Percentual |
| VlrPar | Number(011,2) | Sim | Parcelas |

---

## Chave Primária

- NumEmp
- CmpDef
- TipDef
- SeqDef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R161DEE_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

