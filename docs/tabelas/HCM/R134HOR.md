# R134HOR

## Descrição

Turmas - Horário Curso

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da Turma |
| CodHcu | Number(006,0) | Não | Código do Horário Curso |
| CodSla | Number(004,0) | Sim | Código da Sala de Realização do Curso |
| HorCbk | Number(005,0) | Sim | Horário do Início do Coffee Break |
| DesCbk | String(030) | Sim | Descrição do Coffee Break |
| DesPro | String(500) | Sim | Providências |
| CodDis | Number(003,0) | Sim | Capacidade Máxima de Vagas |
| SeqHor | Number(003,0) | Sim | Sequência do horário |

---

## Chave Primária

- CodCua
- TmaCua
- CodHcu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134HOR_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R134HOR_002

**Tabela:** R133HCU

| Origem | Destino |
|--------|---------|
| CodHcu | CodHcu |

