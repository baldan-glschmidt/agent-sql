# R036PJD

## Descrição

Pensão Judicial - Base 13° Salário

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| CodDep | Number(002,0) | Não | Código do Dependente |
| SeqBas | Number(003,0) | Não | Sequência da base |
| SinBas | String(001) | Sim | PJ13s - Sinal Base |
| TipBas | Number(002,0) | Sim | PJ13s - Tipo Base |
| TabEve | Number(003,0) | Sim | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Sim | PJ13s - Código Evento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodDep
- SeqBas

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R036PJD_003

**Tabela:** R036DEP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodDep | CodDep |

### IR_R036PJD_007

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |

### IR_R036PJD_008

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

