# R135PED

## Descrição

Disponibilidade Horário - Pessoa - Períodos

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPes | Number(009,0) | Não | Código da Pessoa |
| DiaSem | String(003) | Não | Dia da Semana |
| PerDia | String(003) | Não | Período Disponível do Dia |

---

## Chave Primária

- CodPes
- DiaSem
- PerDia

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R135PED_000

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

