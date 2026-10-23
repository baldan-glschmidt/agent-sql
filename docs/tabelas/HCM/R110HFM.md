# R110HFM

## Descrição

Histórico Ficha Médica

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodFic | Number(009,0) | Não | Código Ficha Médica |
| DatTer | Date | Não | Data de Término do Histórico |
| TipAtn | Number(001,0) | Sim | Tipo Atendido |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Código do Colaborador Atendido |
| NumCan | Number(007,0) | Sim | Código do Candidato Atendido |
| CodDep | Number(002,0) | Sim | Código do Dependente Atendido |

---

## Chave Primária

- NumEmp
- CodFic
- DatTer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110HFM_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

