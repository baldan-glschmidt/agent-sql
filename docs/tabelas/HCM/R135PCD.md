# R135PCD

## Descrição

Disponibilidade Horário - Pessoa p/Competência - Períodos

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPes | Number(009,0) | Não | Código da Pessoa |
| CmpDis | Date | Não | Competência p/Disponibilidade de Horário |
| DiaSem | String(003) | Não | Dia da Semana |
| PerDia | String(003) | Não | Período Disponível do Dia |

---

## Chave Primária

- CodPes
- CmpDis
- DiaSem
- PerDia

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R135PCD_000

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

### IR_R135PCD_001

**Tabela:** R135PCO

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |
| CmpDis | CmpDis |

