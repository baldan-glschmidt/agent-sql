# R057HBF

## Descrição

Histórico de Benefícios

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| CodBnf | Number(002,0) | Não | Código do Benefício Entregue no Relógio |
| DatIni | Date | Não | Data Inicial do Recebimento do Benefício |
| DatFim | Date | Sim | Data Final do Recebimento do Benefício |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodBnf
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R057HBF_003

**Tabela:** R057BNF

| Origem | Destino |
|--------|---------|
| CodBnf | CodBnf |

