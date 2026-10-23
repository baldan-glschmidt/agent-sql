# R155CTB

## Descrição

Contabilização Agrupada

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CmpCtb | Date | Não | Competência |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodGru | Number(004,0) | Não | Código do Agrupador |
| SeqCtb | Number(007,0) | Não | Sequência |
| CodCcu | String(018) | Sim | Centro de Custo (Padrão) |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador |
| ValLan | Number(014,2) | Sim | Valor |
| CodClc | Number(004,0) | Sim | Código Lançamento Contábil |

---

## Chave Primária

- NumEmp
- CmpCtb
- TabEve
- CodGru
- SeqCtb

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R155CTB_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

