# R006HOR

## Descrição

Horários da Escala

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEsc | Number(009,0) | Não | Código da Escala |
| SeqReg | Number(003,0) | Não | Sequência do Registro |
| CodHor | Number(004,0) | Sim | Código do Horário Base |
| HorBu1 | Number(004,0) | Sim | Código do Horário Opcional 1 |
| HorBu2 | Number(004,0) | Sim | Código do Horário Opcional 2 |
| HorBu3 | Number(004,0) | Sim | Código do Horário Opcional 3 |
| HorBu4 | Number(004,0) | Sim | Código do Horário Opcional 4 |
| HorBu5 | Number(004,0) | Sim | Código do Horário Opcional  5 |
| HorDup | Number(004,0) | Sim | Código do Horário de Turno Duplo |

---

## Chave Primária

- CodEsc
- SeqReg

---

## Índices

### R006HORIndice2

**Tipo:** Não unico

Campos:
- CodHor

---

## Relacionamentos

### IR_R006HOR_000

**Tabela:** R006ESC

| Origem | Destino |
|--------|---------|
| CodEsc | CodEsc |

### IR_R006HOR_002

**Tabela:** R004HOR

| Origem | Destino |
|--------|---------|
| CodHor | CodHor |

