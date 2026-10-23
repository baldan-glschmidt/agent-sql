# R057DIB

## Descrição

Distribuição da Entrega de Benefícios

---

## Resumo

- Campos: 13
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| CodBnf | Number(002,0) | Não | Código do Benefício Entregue no Relógio |
| DatIni | Date | Não | Data Inicial do Período de Retirada |
| HorIni | Number(005,0) | Não | Hora Inicial do Período de Retirada |
| DatFim | Date | Sim | Data Final do Período de Retirada |
| HorFim | Number(005,0) | Sim | Hora Final do Período de Retirada |
| QtdEnB | Number(002,0) | Sim | Qtde de Entregas do Benefício no Período |
| QtdReB | Number(002,0) | Sim | Qtde de Retiradas do Benefício no Período |
| MesCmp | Number(002,0) | Sim | Mês de Competência para Folha |
| StaAcc | Number(001,0) | Sim | Status da Atualização na Tabela CONTROLE (Acesso On-Line) |
| StaDib | Number(001,0) | Sim | Status da Distribuição para Controle de Colaboradores Afastados |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodBnf
- DatIni
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R057DIB_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R057DIB_003

**Tabela:** R057BNF

| Origem | Destino |
|--------|---------|
| CodBnf | CodBnf |

