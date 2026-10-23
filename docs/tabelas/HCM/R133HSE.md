# R133HSE

## Descrição

Horário Semana Cursos Aperfeiçoamento

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodHcu | Number(006,0) | Não | Código Horário Curso |
| NomDia | String(003) | Não | Dia da Semana |
| HorIni | Number(005,0) | Sim | Hora de Início |
| HorFim | Number(005,0) | Sim | Hora de Fim |

---

## Chave Primária

- CodHcu
- NomDia

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R133HSE_000

**Tabela:** R133HCU

| Origem | Destino |
|--------|---------|
| CodHcu | CodHcu |

