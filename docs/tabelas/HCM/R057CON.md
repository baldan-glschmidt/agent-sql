# R057CON

## Descrição

Consumo de Benefícios

---

## Resumo

- Campos: 13
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| CodBnf | Number(002,0) | Não | Código do Benefício Entregue no Relógio |
| DatCon | Date | Não | Data do Consumo do Benefício |
| HorCon | Number(005,0) | Não | Hora de Consumo do Benefício |
| SeqCon | Number(002,0) | Não | Sequência do Registro |
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodRlg | Number(005,0) | Sim | Código do Coletor que Retirou o Benefício |
| QtdCon | Number(002,0) | Sim | Qtde Consumida do Benefício |
| GerCon | Number(001,0) | Sim | Geração do Consumo |
| DatIni | Date | Sim | Data Inicial da Distribuição |
| HorIni | Number(005,0) | Sim | Hora Inicial da Distribuição |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodBnf
- DatCon
- HorCon
- SeqCon

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R057CON_003

**Tabela:** R057BNF

| Origem | Destino |
|--------|---------|
| CodBnf | CodBnf |

### IR_R057CON_007

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R057CON_008

**Tabela:** R058RLG

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodRlg | CodRlg |

