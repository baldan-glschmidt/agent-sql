# R134HCF

## Descrição

Turmas - Horário Coffee Break

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da Turma |
| CodHcu | Number(006,0) | Não | Código do Horário Curso |
| HorCbk | Number(005,0) | Não | Horário do Início do Coffee Break |
| CodCbk | Number(003,0) | Sim | Código do Tipo de Coffee Break |
| DesPro | String(500) | Sim | Providências |

---

## Chave Primária

- CodCua
- TmaCua
- CodHcu
- HorCbk

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134HCF_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R134HCF_002

**Tabela:** R133HCU

| Origem | Destino |
|--------|---------|
| CodHcu | CodHcu |

### IR_R134HCF_004

**Tabela:** R133CBK

| Origem | Destino |
|--------|---------|
| CodCbk | CodCbk |

