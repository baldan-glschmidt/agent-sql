# R051VMC

## Descrição

Informe/DIRF - Valores Mês

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| AnoBas | Number(004,0) | Não | Ano |
| TipIns | Number(001,0) | Não | Código correspondente ao tipo de inscrição |
| NumIns | Number(015,0) | Não | Número de Inscrição |
| CmpVal | Date | Não | Competência |
| ValMes | Number(011,2) | Sim | Valor Mês |

---

## Chave Primária

- NumEmp
- CodFil
- AnoBas
- TipIns
- NumIns
- CmpVal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R051VMC_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R051VMC_004

**Tabela:** R051COT

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| AnoBas | AnoBas |
| TipIns | TipIns |
| NumIns | NumIns |

