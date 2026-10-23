# R036PJN

## Descrição

Pensão Judicial - Base Normal

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| CodDep | Number(002,0) | Não | Código do Dependente |
| SeqBas | Number(003,0) | Não | Sequência da base |
| SinBas | String(001) | Sim | PJMês - Sinal Base |
| TipBas | Number(002,0) | Sim | PJMês - Tipo Base |
| TabEve | Number(003,0) | Sim | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Sim | PJMês - Código do Evento |

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

### IR_R036PJN_003

**Tabela:** R036DEP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodDep | CodDep |

### IR_R036PJN_008

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

