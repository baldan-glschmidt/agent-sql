# R104CRD

## Descrição

JR - Calendário de Repouso - Dias

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodClr | Number(003,0) | Não | Código do calendário de repouso |
| CmpClr | Date | Não | Competência do calendário de repouso |
| DiaUti | Number(002,0) | Sim | Quantidade de dias úteis |
| DiaDSR | Number(002,0) | Sim | Quantidade de dias DSR |
| PerDia | Number(007,4) | Sim | Percentual entre dias trabalhados e dias de DSR |

---

## Chave Primária

- CodClr
- CmpClr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104CRD_000

**Tabela:** R104CLR

| Origem | Destino |
|--------|---------|
| CodClr | CodClr |

