# R135DCC

## Descrição

Disponibilidade Horário - Participante p/Competência

---

## Resumo

- Campos: 6
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa do Participante |
| TipCol | Number(001,0) | Não | Tipo do Colaborador Participante |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador Participante |
| CmpDis | Date | Não | Competência p/Disponibilidade de Horário |
| DiaSem | String(003) | Não | Dia da Semana |
| PerDia | String(003) | Não | Período Disponível do Dia |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpDis
- DiaSem
- PerDia

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R135DCC_003

**Tabela:** R135OCC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CmpDis | CmpDis |

