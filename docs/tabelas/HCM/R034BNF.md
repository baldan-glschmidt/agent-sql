# R034BNF

## Descrição

Consumo de Benefícios

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
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
| RetBnf | String(001) | Sim | Colaborador Pode Retirar Benefício |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodBnf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034BNF_003

**Tabela:** R057BNF

| Origem | Destino |
|--------|---------|
| CodBnf | CodBnf |

