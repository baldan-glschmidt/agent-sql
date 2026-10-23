# R578LOG

## Descrição

Avaliação de Competências - Avaliação por foco - Registro de LOG

---

## Resumo

- Campos: 10
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa do Colaborador avaliado |
| TipCol | Number(001,0) | Não | Tipo do Colaborador avaliado |
| NumCad | Number(009,0) | Não | Colaborador avaliado |
| CodCic | Number(003,0) | Não | Indica a qual Ciclo esta Avaliação pertence |
| IdeAva | Number(005,0) | Não | Identificador da avaliação de competências |
| SeqAvf | Number(007,0) | Não | Sequência da avaliação por foco, dentro da avaliação do colaborador |
| DtHLog | Number(014,6) | Não | Data/Hora em que ocorreu a ação |
| CodUsu | Number(010,0) | Sim | Usuário que efetuou a ação |
| SitAva | Number(001,0) | Sim | Situação da avaliação no momento do registro do log |
| DesLog | String(8001) | Sim | Descrição da ação realizada na avaliação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCic
- IdeAva
- SeqAvf
- DtHLog

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R578LOG_005

**Tabela:** R578AVF

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodCic | CodCic |
| IdeAva | IdeAva |
| SeqAvf | SeqAvf |

