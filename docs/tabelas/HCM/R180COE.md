# R180COE

## Descrição

Contas O. Empresa

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodOem | Number(008,0) | Não | Código da outra empresa |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodClc | Number(004,0) | Não | Código do CLC |
| HisPad | Number(004,0) | Sim | Código Histórico Padrão |
| GerGer | String(001) | Sim | Gerar Gerencial |

---

## Chave Primária

- NumEmp
- CodOem
- TabEve
- CodClc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R180COE_001

**Tabela:** R180DOE

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodOem | CodOem |

### IR_R180COE_003

**Tabela:** R048CLC

| Origem | Destino |
|--------|---------|
| TabEve | TabEve |
| CodClc | CodClc |

