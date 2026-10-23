# R172CCO

## Descrição

Contas Colaborador

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
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do colaborador |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodClc | Number(004,0) | Não | Código do CLC |
| HisPad | Number(004,0) | Sim | Código Histórico Padrão |
| GerGer | String(001) | Sim | Gerar Gerencial |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- TabEve
- CodClc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R172CCO_002

**Tabela:** R172DCO

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R172CCO_004

**Tabela:** R048CLC

| Origem | Destino |
|--------|---------|
| TabEve | TabEve |
| CodClc | CodClc |

