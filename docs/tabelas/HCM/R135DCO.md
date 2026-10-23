# R135DCO

## Descrição

Disponibilidade Horário - Participante

---

## Resumo

- Campos: 5
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa do Participante |
| TipCol | Number(001,0) | Não | Tipo do Colaborador Participante |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador Participante |
| DiaSem | String(003) | Não | Dia da Semana |
| PerDia | String(003) | Não | Período Disponível do Dia |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DiaSem
- PerDia

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R135DCO_002

**Tabela:** R135OCO

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

